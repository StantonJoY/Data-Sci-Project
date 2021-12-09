Module(
    body=[
        ImportFrom(
            module='itertools',
            names=[alias(name='chain', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='_boundaries',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='intervals', annotation=None, type_comment=None),
                    arg(arg='opening', annotation=None, type_comment=None),
                    arg(arg='closing', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Iterate on the boundaries of intervals. ', kind=None),
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='start', ctx=Store()),
                            Name(id='stop', ctx=Store()),
                            Name(id='recs', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='intervals', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='start', ctx=Load()),
                                ops=[Lt()],
                                comparators=[Name(id='stop', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Tuple(
                                            elts=[
                                                Name(id='start', ctx=Load()),
                                                Name(id='opening', ctx=Load()),
                                                Name(id='recs', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                                Expr(
                                    value=Yield(
                                        value=Tuple(
                                            elts=[
                                                Name(id='stop', ctx=Load()),
                                                Name(id='closing', ctx=Load()),
                                                Name(id='recs', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
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
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='WorkIntervals',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n        This class is a modified copy of the ``Intervals`` class in the resource module.\n        A generic solution to handle intervals should probably be developped the day a similar\n        class is needed elsewhere.\n\n        This implementation differs from the resource implementation in its management\n        of two continuous intervals. Here, continuous intervals are not merged together\n        while they are merged in resource.\n        e.g.:\n        In resource: (1, 4, rec1) and (4, 10, rec2) are merged into (1, 10, rec1 | rec2)\n        Here: they remain two different intervals.\n        To implement this behaviour, the main implementation change is the way boundaries are sorted.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='intervals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Tuple(elts=[], ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_items',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='intervals', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='append', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_items',
                                            ctx=Load(),
                                        ),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='starts', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='recses', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='value', ctx=Store()),
                                            Name(id='flag', ctx=Store()),
                                            Name(id='recs', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_boundaries', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='sorted', ctx=Load()),
                                                        args=[Name(id='intervals', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='stop', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='i', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Subscript(
                                                        value=Name(id='i', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='flag', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='start', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='starts', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='recses', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='recs', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='starts', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='starts', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='append', ctx=Load()),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='start', ctx=Load()),
                                                                            Name(id='value', ctx=Load()),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='recses', ctx=Load()),
                                                                                        slice=Constant(value=0, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='union',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Starred(
                                                                                        value=Name(id='recses', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
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
                                                                    value=Name(id='recses', ctx=Load()),
                                                                    attr='clear',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
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
                FunctionDef(
                    name='__bool__',
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
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_items',
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
                    name='__len__',
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
                        Return(
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_items',
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
                    name='__iter__',
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
                        Return(
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_items',
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
                    name='__reversed__',
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
                        Return(
                            value=Call(
                                func=Name(id='reversed', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_items',
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
                    name='__or__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the union of two sets of intervals. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='WorkIntervals', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='chain', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_items',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='other', ctx=Load()),
                                                attr='_items',
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='__and__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the intersection of two sets of intervals. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_merge',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='other', ctx=Load()),
                                    Constant(value=False, kind=None),
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
                    name='__sub__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the difference of two sets of intervals. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_merge',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='other', ctx=Load()),
                                    Constant(value=True, kind=None),
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
                    name='_merge',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                            arg(arg='difference', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the difference or intersection of two sets of intervals. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='WorkIntervals', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='append', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='_items',
                                    ctx=Load(),
                                ),
                                attr='append',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bounds1', ctx=Store())],
                            value=Call(
                                func=Name(id='_boundaries', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value='start', kind=None),
                                    Constant(value='stop', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bounds2', ctx=Store())],
                            value=Call(
                                func=Name(id='_boundaries', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='other', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value='switch', kind=None),
                                    Constant(value='switch', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recs1', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='enabled', ctx=Store())],
                            value=Name(id='difference', ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='value', ctx=Store()),
                                    Name(id='flag', ctx=Store()),
                                    Name(id='recs', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='chain', ctx=Load()),
                                        args=[
                                            Name(id='bounds1', ctx=Load()),
                                            Name(id='bounds2', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='i', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Name(id='i', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='flag', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='start', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='start', ctx=Store())],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='recs1', ctx=Store())],
                                            value=Name(id='recs', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='flag', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='stop', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='enabled', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='start', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='value', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='append', ctx=Load()),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='start', ctx=Load()),
                                                                            Name(id='value', ctx=Load()),
                                                                            Name(id='recs1', ctx=Load()),
                                                                        ],
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
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='enabled', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Name(id='start', ctx=Load()),
                                                                ops=[IsNot()],
                                                                comparators=[Constant(value=None, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='start', ctx=Store())],
                                                            value=Name(id='value', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='enabled', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='start', ctx=Load()),
                                                                ops=[IsNot()],
                                                                comparators=[Constant(value=None, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='start', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='value', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='append', ctx=Load()),
                                                                args=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='start', ctx=Load()),
                                                                            Name(id='value', ctx=Load()),
                                                                            Name(id='recs1', ctx=Load()),
                                                                        ],
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
                                                    targets=[Name(id='enabled', ctx=Store())],
                                                    value=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='enabled', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
