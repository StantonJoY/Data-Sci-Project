Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='misc', asname=None),
                alias(name='date_utils', asname=None),
                alias(name='file_open', asname=None),
                alias(name='file_path', asname=None),
                alias(name='merge_sequences', asname=None),
                alias(name='remove_accents', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='BaseCase', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestCountingStream',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_empty_stream',
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
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='CountingStream',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='iter', ctx=Load()),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_single',
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
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='CountingStream',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
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
                FunctionDef(
                    name='test_full',
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
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='CountingStream',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=42, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='_', ctx=Store()),
                            iter=Name(id='s', ctx=Load()),
                            body=[Pass()],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
                                    ),
                                    Constant(value=42, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_repeated',
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
                            value=Constant(value=' Once the CountingStream has stopped iterating, the index should not\n        increase anymore (the internal state should not be allowed to change)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='s', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='CountingStream',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='iter', ctx=Load()),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='s', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='s', ctx=Load()),
                                        attr='index',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
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
            name='TestMergeSequences',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_merge_sequences',
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
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Name(id='merge_sequences', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='seq', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Name(id='merge_sequences', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='Z', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='seq', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                            Constant(value='Z', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Name(id='merge_sequences', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='Y', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='seq', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='Y', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Name(id='merge_sequences', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='X', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='seq', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='X', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='seq', ctx=Store())],
                            value=Call(
                                func=Name(id='merge_sequences', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='Z', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='Y', kind=None),
                                            Constant(value='C', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='X', kind=None),
                                            Constant(value='Y', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='seq', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='A', kind=None),
                                            Constant(value='B', kind=None),
                                            Constant(value='X', kind=None),
                                            Constant(value='Y', kind=None),
                                            Constant(value='C', kind=None),
                                            Constant(value='Z', kind=None),
                                        ],
                                        ctx=Load(),
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
            decorator_list=[],
        ),
        ClassDef(
            name='TestDateRangeFunction',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test on date_range generator. ', kind=None),
                ),
                FunctionDef(
                    name='test_date_range_with_naive_datetimes',
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
                            value=Constant(value=' Check date_range with naive datetimes. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1985, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1986, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1986, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dates', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='date', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='date', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='date_utils', ctx=Load()),
                                                attr='date_range',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='start', ctx=Load()),
                                                Name(id='end', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dates', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_date_range_with_timezone_aware_datetimes_other_than_utc',
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
                            value=Constant(value=' Check date_range with timezone-aware datetimes other than UTC.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='timezone', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pytz', ctx=Load()),
                                    attr='timezone',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Europe/Brussels', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1985, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1986, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timezone', ctx=Load()),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='start', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='timezone', ctx=Load()),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='end', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1985, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=1986, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='timezone', ctx=Load()),
                                        attr='localize',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='e', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Name(id='expected', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dates', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='date', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='date', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='date_utils', ctx=Load()),
                                                attr='date_range',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='start', ctx=Load()),
                                                Name(id='end', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='expected', ctx=Load()),
                                    Name(id='dates', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_date_range_with_mismatching_zones',
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
                            value=Constant(value=' Check date_range with mismatching zone should raise an exception.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='start_timezone', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pytz', ctx=Load()),
                                    attr='timezone',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Europe/Brussels', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_timezone', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pytz', ctx=Load()),
                                    attr='timezone',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='America/Recife', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1985, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1986, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='start_timezone', ctx=Load()),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='start', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='end_timezone', ctx=Load()),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='end', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='dates', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='date', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='date', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='date_utils', ctx=Load()),
                                                        attr='date_range',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='start', ctx=Load()),
                                                        Name(id='end', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_date_range_with_inconsistent_datetimes',
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
                            value=Constant(value=' Check date_range with a timezone-aware datetime and a naive one.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='context_timezone', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pytz', ctx=Load()),
                                    attr='timezone',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Europe/Brussels', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1985, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1986, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context_timezone', ctx=Load()),
                                    attr='localize',
                                    ctx=Load(),
                                ),
                                args=[Name(id='end', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValueError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='dates', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='date', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='date', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='date_utils', ctx=Load()),
                                                        attr='date_range',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='start', ctx=Load()),
                                                        Name(id='end', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_date_range_with_hour',
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
                            value=Constant(value=' Test date range with hour and naive datetime.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=25, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='datetime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2018, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=26, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='step', ctx=Store())],
                            value=Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='hours',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=18, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=19, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=21, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=22, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=25, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=26, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dates', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='date', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='date', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='date_utils', ctx=Load()),
                                                attr='date_range',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='start', ctx=Load()),
                                                Name(id='end', ctx=Load()),
                                                Name(id='step', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dates', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
            name='TestFormatLangDate',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_00_accepted_types',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Europe/Brussels', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='datetime_str', ctx=Store())],
                            value=Constant(value='2017-01-31 12:00:00', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_datetime', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='datetime',
                                        ctx=Load(),
                                    ),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='datetime_str', ctx=Load()),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date_datetime', ctx=Load()),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_str', ctx=Store())],
                            value=Constant(value='2017-01-31', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_part', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=16, kind=None),
                                    Constant(value=30, kind=None),
                                    Constant(value=22, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_datetime', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='01/31/2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_date', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='01/31/2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='01/31/2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_datetime', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Jan 31, 2017, 1:00:00 PM', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Jan 31, 2017, 1:00:00 PM', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='4:30:22 PM', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_code_and_format',
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
                            targets=[Name(id='date_str', ctx=Store())],
                            value=Constant(value='2017-01-31', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.lang', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lang', ctx=Load()),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lang', ctx=Load()),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='zh_CN', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='31/01/2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lang', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='31/01/2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lang', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='date_format',
                                                value=Constant(value='MMM d, y', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Jan 31, 2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='31/01/2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='date_format',
                                                value=Constant(value='MMM d, y', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='1月 31, 2017', kind='u'),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lang', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                            keyword(
                                                arg='date_format',
                                                value=Constant(value='MMM d, y', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='janv. 31, 2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                            keyword(
                                                arg='date_format',
                                                value=Constant(value='MMM d, y', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Jan 31, 2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='datetime_str', ctx=Store())],
                            value=Constant(value='2017-01-31 10:33:00', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Constant(value='Europe/Brussels', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='31 janv. 2017 à 11:33:00', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Constant(value='America/New_York', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='2017年1月31日 上午5:33:00', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Constant(value='America/New_York', kind=None),
                                            ),
                                            keyword(
                                                arg='dt_format',
                                                value=Constant(value='short', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='31/01/2017 05:33', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='en_US', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Constant(value='Europe/Brussels', kind=None),
                                            ),
                                            keyword(
                                                arg='dt_format',
                                                value=Constant(value='MMM d, y', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Jan 31, 2017', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lang', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Constant(value='Europe/Brussels', kind=None),
                                            ),
                                            keyword(
                                                arg='dt_format',
                                                value=Constant(value='long', kind=None),
                                            ),
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='31 janvier 2017 à 11:33:00 +0100', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Constant(value='Europe/Brussels', kind=None),
                                            ),
                                            keyword(
                                                arg='dt_format',
                                                value=Constant(value='long', kind=None),
                                            ),
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='January 31, 2017 at 11:33:00 AM +0100', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time_part', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=16, kind=None),
                                    Constant(value=30, kind=None),
                                    Constant(value=22, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_part_tz', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=16, kind=None),
                                    Constant(value=30, kind=None),
                                    Constant(value=22, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='timezone',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='US/Eastern', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='16:30:22', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='下午4:30:22', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='short', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='16:30', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='short', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='下午4:30', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part_tz', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='long', kind=None),
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='16:30:22 -0504', kind=None),
                                            Constant(value='16:30:22 HNE', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part_tz', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='full', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='北美东部标准时间 下午4:30:22', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='long', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='11:33:00 +0100', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='datetime_str', ctx=Load()),
                                            Constant(value='US/Eastern', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='long', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='05:33:00 HNE', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='fr_FR', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='short', kind=None),
                                            ),
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='zh_CN', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='下午4:30', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='format_time',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='lang', ctx=Load()),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lang',
                                                            value=Constant(value='zh_CN', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='time_part', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='time_format',
                                                value=Constant(value='medium', kind=None),
                                            ),
                                            keyword(
                                                arg='lang_code',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='16:30:22', kind=None),
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
            name='TestCallbacks',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_callback',
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
                            targets=[Name(id='log', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='callbacks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='Callbacks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='foo',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='log', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='foo', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[Name(id='foo', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='bar',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='log', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='bar', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[Name(id='foo', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='log', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='bar', kind=None),
                                            Constant(value='foo', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='log', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='bar', kind=None),
                                            Constant(value='foo', kind=None),
                                        ],
                                        ctx=Load(),
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
                FunctionDef(
                    name='test_aggregate',
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
                            targets=[Name(id='log', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='callbacks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='Callbacks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='foo',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='log', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='callbacks', ctx=Load()),
                                                    attr='data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='foo', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='callbacks', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='foo', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='callbacks', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='foo', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=2, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='callbacks', ctx=Load()),
                                                attr='data',
                                                ctx=Load(),
                                            ),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='foo', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=3, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='log', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='callbacks', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='log', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
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
                FunctionDef(
                    name='test_reentrant',
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
                            targets=[Name(id='log', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='callbacks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='misc', ctx=Load()),
                                    attr='Callbacks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='foo',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='log', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='foo1', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='callbacks', ctx=Load()),
                                            attr='run',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='log', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='foo2', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='bar',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='log', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='bar', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='log', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='foo1', kind=None),
                                            Constant(value='bar', kind=None),
                                            Constant(value='foo2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='callbacks', ctx=Load()),
                                    attr='run',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='log', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='foo1', kind=None),
                                            Constant(value='bar', kind=None),
                                            Constant(value='foo2', kind=None),
                                        ],
                                        ctx=Load(),
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
            decorator_list=[],
        ),
        ClassDef(
            name='TestRemoveAccents',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_empty_string',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value=False, kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value='', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value=None, kind=None)],
                                        keywords=[],
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
                FunctionDef(
                    name='test_latin',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value='Niño Hernández', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='Nino Hernandez', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value='Anaïs Clémence', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='Anais Clemence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_non_latin',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value='العربية', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='العربية', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='remove_accents', ctx=Load()),
                                        args=[Constant(value='русский алфавит', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='русскии алфавит', kind=None),
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
            name='TestAddonsFileAccess',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='assertCannotAccess',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='ExceptionType', annotation=None, type_comment=None),
                            arg(arg='filter_ext', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Name(id='FileNotFoundError', ctx=Load()),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ExceptionType', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Name(id='filter_ext', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertCanRead',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='needle', annotation=None, type_comment=None),
                            arg(arg='mode', annotation=None, type_comment=None),
                            arg(arg='filter_ext', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value='r', kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='file_open', ctx=Load()),
                                        args=[
                                            Name(id='path', ctx=Load()),
                                            Name(id='mode', ctx=Load()),
                                            Name(id='filter_ext', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='needle', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertCannotRead',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='ExceptionType', annotation=None, type_comment=None),
                            arg(arg='filter_ext', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Name(id='FileNotFoundError', ctx=Load()),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ExceptionType', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='file_open', ctx=Load()),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Name(id='filter_ext', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_file_path',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='__file__', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='__file__', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='__file__', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Tuple(
                                                    elts=[Constant(value='.py', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
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
                                            attr='dirname',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='__file__', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
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
                                                    Name(id='__file__', ctx=Load()),
                                                    Constant(value='..', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='relpath', ctx=Store())],
                            value=Call(
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
                                    Starred(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='__file__', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='sep',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Slice(
                                                lower=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=3, kind=None),
                                                ),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='relpath', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='relpath', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='filter_ext',
                                                value=Tuple(
                                                    elts=[Constant(value='.py', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Constant(value='addons/web/__init__.py', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='relpath', ctx=Store())],
                            value=Call(
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
                                    Constant(value='addons', kind=None),
                                    Name(id='relpath', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Name(id='relpath', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='file_path', ctx=Load()),
                                        args=[Constant(value='tools/misc.py', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/doesnt/exist', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/tmp', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='../../../../../../../../../tmp', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
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
                                            Name(id='__file__', ctx=Load()),
                                            Constant(value='../../../../../', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='data_dir', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Name(id='ValueError', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='filter_ext',
                                        value=Tuple(
                                            elts=[Constant(value='.png', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotAccess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='__file__', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.py', kind=None),
                                            Constant(value='.foo', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='ValueError', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='filter_ext',
                                        value=Tuple(
                                            elts=[Constant(value='.png', kind=None)],
                                            ctx=Load(),
                                        ),
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
                    name='test_file_open',
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
                            targets=[Name(id='test_needle', ctx=Store())],
                            value=Constant(value='A needle with non-ascii bytes: ♥', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Name(id='test_needle', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='test_needle', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='rb', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='test_needle', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='rb', kind=None),
                                    ),
                                    keyword(
                                        arg='filter_ext',
                                        value=Tuple(
                                            elts=[Constant(value='.py', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='FileNotFoundError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='file_open', ctx=Load()),
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
                                                    Name(id='__file__', ctx=Load()),
                                                    Constant(value='..', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='relpath', ctx=Store())],
                            value=Call(
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
                                    Starred(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='__file__', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='sep',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            slice=Slice(
                                                lower=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=3, kind=None),
                                                ),
                                                upper=None,
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='relpath', ctx=Load()),
                                    Name(id='test_needle', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='relpath', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='test_needle', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='rb', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='relpath', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='test_needle', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mode',
                                        value=Constant(value='rb', kind=None),
                                    ),
                                    keyword(
                                        arg='filter_ext',
                                        value=Tuple(
                                            elts=[Constant(value='.py', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='addons/web/__init__.py', kind=None),
                                    Constant(value='import', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='relpath', ctx=Store())],
                            value=Call(
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
                                    Constant(value='addons', kind=None),
                                    Name(id='relpath', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='relpath', ctx=Load()),
                                    Name(id='test_needle', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCanRead',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tools/misc.py', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/doesnt/exist', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/tmp', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='../../../../../../../../../tmp', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
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
                                            Name(id='__file__', ctx=Load()),
                                            Constant(value='../../../../../', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='config', ctx=Load()),
                                        slice=Constant(value='data_dir', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='__file__', ctx=Load()),
                                    Name(id='ValueError', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='filter_ext',
                                        value=Tuple(
                                            elts=[Constant(value='.png', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertCannotRead',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='__file__', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.py', kind=None),
                                            Constant(value='.foo', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='ValueError', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='filter_ext',
                                        value=Tuple(
                                            elts=[Constant(value='.png', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
