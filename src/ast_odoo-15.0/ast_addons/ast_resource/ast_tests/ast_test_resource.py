Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='pytz',
            names=[
                alias(name='timezone', asname=None),
                alias(name='utc', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.resource.models.resource',
            names=[alias(name='Intervals', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.resource.tests.common',
            names=[alias(name='TestResourceCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='datetime_tz',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='year', annotation=None, type_comment=None),
                    arg(arg='month', annotation=None, type_comment=None),
                    arg(arg='day', annotation=None, type_comment=None),
                    arg(arg='hour', annotation=None, type_comment=None),
                    arg(arg='minute', annotation=None, type_comment=None),
                    arg(arg='second', annotation=None, type_comment=None),
                    arg(arg='microsecond', annotation=None, type_comment=None),
                    arg(arg='tzinfo', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a `datetime` object with a given timezone (if given). ', kind=None),
                ),
                Assign(
                    targets=[Name(id='dt', ctx=Store())],
                    value=Call(
                        func=Name(id='datetime', ctx=Load()),
                        args=[
                            Name(id='year', ctx=Load()),
                            Name(id='month', ctx=Load()),
                            Name(id='day', ctx=Load()),
                            Name(id='hour', ctx=Load()),
                            Name(id='minute', ctx=Load()),
                            Name(id='second', ctx=Load()),
                            Name(id='microsecond', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Name(id='tzinfo', ctx=Load()),
                        body=Call(
                            func=Attribute(
                                value=Call(
                                    func=Name(id='timezone', ctx=Load()),
                                    args=[Name(id='tzinfo', ctx=Load())],
                                    keywords=[],
                                ),
                                attr='localize',
                                ctx=Load(),
                            ),
                            args=[Name(id='dt', ctx=Load())],
                            keywords=[],
                        ),
                        orelse=Name(id='dt', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='datetime_str',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='year', annotation=None, type_comment=None),
                    arg(arg='month', annotation=None, type_comment=None),
                    arg(arg='day', annotation=None, type_comment=None),
                    arg(arg='hour', annotation=None, type_comment=None),
                    arg(arg='minute', annotation=None, type_comment=None),
                    arg(arg='second', annotation=None, type_comment=None),
                    arg(arg='microsecond', annotation=None, type_comment=None),
                    arg(arg='tzinfo', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a fields.Datetime value with the given timezone. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='dt', ctx=Store())],
                    value=Call(
                        func=Name(id='datetime', ctx=Load()),
                        args=[
                            Name(id='year', ctx=Load()),
                            Name(id='month', ctx=Load()),
                            Name(id='day', ctx=Load()),
                            Name(id='hour', ctx=Load()),
                            Name(id='minute', ctx=Load()),
                            Name(id='second', ctx=Load()),
                            Name(id='microsecond', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='tzinfo', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='timezone', ctx=Load()),
                                                args=[Name(id='tzinfo', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='localize',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='dt', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='utc', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='fields', ctx=Load()),
                                attr='Datetime',
                                ctx=Load(),
                            ),
                            attr='to_string',
                            ctx=Load(),
                        ),
                        args=[Name(id='dt', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='TestIntervals',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='ints',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pairs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='recs', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='base', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Name(id='a', ctx=Load()),
                                        Name(id='b', ctx=Load()),
                                        Name(id='recs', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='a', ctx=Store()),
                                                Name(id='b', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Name(id='pairs', ctx=Load()),
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
                    name='test_union',
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
                        FunctionDef(
                            name='check',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='a', annotation=None, type_comment=None),
                                    arg(arg='b', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='a', ctx=Store()),
                                                Name(id='b', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='a', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='b', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
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
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='Intervals', ctx=Load()),
                                                        args=[Name(id='a', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='b', ctx=Load()),
                                        ],
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
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
                    name='test_intersection',
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
                        FunctionDef(
                            name='check',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='a', annotation=None, type_comment=None),
                                    arg(arg='b', annotation=None, type_comment=None),
                                    arg(arg='c', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='a', ctx=Store()),
                                                Name(id='b', ctx=Store()),
                                                Name(id='c', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='a', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='b', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='c', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
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
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='Intervals', ctx=Load()),
                                                            args=[Name(id='a', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=BitAnd(),
                                                        right=Call(
                                                            func=Name(id='Intervals', ctx=Load()),
                                                            args=[Name(id='b', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='c', ctx=Load()),
                                        ],
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=20, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=20, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=30, kind=None),
                                                    Constant(value=35, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=9, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=13, kind=None),
                                                    Constant(value=17, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=22, kind=None),
                                                    Constant(value=23, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=24, kind=None),
                                                    Constant(value=40, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=13, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=22, kind=None),
                                                    Constant(value=23, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=24, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=30, kind=None),
                                                    Constant(value=35, kind=None),
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
                    name='test_difference',
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
                        FunctionDef(
                            name='check',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='a', annotation=None, type_comment=None),
                                    arg(arg='b', annotation=None, type_comment=None),
                                    arg(arg='c', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='a', ctx=Store()),
                                                Name(id='b', ctx=Store()),
                                                Name(id='c', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='a', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='b', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ints',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='c', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
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
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='Intervals', ctx=Load()),
                                                            args=[Name(id='a', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='Intervals', ctx=Load()),
                                                            args=[Name(id='b', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='c', ctx=Load()),
                                        ],
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=5, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=18, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=15, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=20, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
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
                                func=Name(id='check', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=20, kind=None),
                                                    Constant(value=25, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=30, kind=None),
                                                    Constant(value=35, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=9, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=13, kind=None),
                                                    Constant(value=17, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=22, kind=None),
                                                    Constant(value=23, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=24, kind=None),
                                                    Constant(value=40, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=5, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=12, kind=None),
                                                    Constant(value=13, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=20, kind=None),
                                                    Constant(value=22, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=23, kind=None),
                                                    Constant(value=24, kind=None),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestErrors',
            bases=[Name(id='TestResourceCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestErrors', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_create_negative_leave',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='resource.calendar.leaves', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='resource_id', kind=None),
                                                    Constant(value='calendar_id', kind=None),
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='date_to', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='error cannot return in the past', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='calendar_jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='datetime_str', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value=20, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='tzinfo',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='jean',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='tz',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='datetime_str', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='tzinfo',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='jean',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='tz',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='resource.calendar.leaves', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='resource_id', kind=None),
                                                    Constant(value='calendar_id', kind=None),
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='date_to', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='error caused by timezones', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='calendar_jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='datetime_str', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value=10, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='tzinfo',
                                                                value=Constant(value='UTC', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Name(id='datetime_str', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value=12, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='tzinfo',
                                                                value=Constant(value='Etc/GMT-6', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestCalendar',
            bases=[Name(id='TestResourceCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestCalendar', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_get_work_hours_count',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Global Leave', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=59, kind=None),
                                                    Constant(value=59, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='leave for Jean', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=5, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=5, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=59, kind=None),
                                                    Constant(value=59, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=32, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=40, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero_length', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_patel',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_patel',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=35, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero_length', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_patel',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_patel',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=32, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero_length', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_patel',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_patel',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=35, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='no timezone', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_patel',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_patel',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=28, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_patel',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jules',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=30, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jules',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=30, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jules',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=16, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Leave Jules week 2', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jules',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=11, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jules',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jules',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jules',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=16, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Leave Jules week 2', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jules',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jules',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=59, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jules',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jules',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jules',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=8, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='small leave', kind=None),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='patel',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hours', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_patel',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='patel',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='hours', ctx=Load()),
                                    Constant(value=32, kind=None),
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
                    name='test_calendar_working_hours_count',
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
                            targets=[Name(id='calendar', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='resource.resource_calendar_std_35h', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='calendar', ctx=Load()),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='UTC', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='calendar', ctx=Load()),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2017-05-03 14:03:00', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='2017-05-04 11:03:00', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='res', ctx=Load()),
                                    Constant(value=5.0, kind=None),
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
                    name='test_calendar_working_hours_24',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='att_4',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.attendance', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='dayofweek', kind=None),
                                            Constant(value='hour_from', kind=None),
                                            Constant(value='hour_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Att4', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='2', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=24, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=19, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=21, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='res', ctx=Load()),
                                    Constant(value=24.0, kind=None),
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
                    name='test_plan_hours',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='global', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=11, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=11, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=59, kind=None),
                                                    Constant(value=59, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=20, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=5, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=10, kind=None),
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0.0002, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=720000, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=3000, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2019, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                    name='test_plan_days',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='global', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=11, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=11, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=59, kind=None),
                                                    Constant(value=59, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=3, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=4, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=10, kind=None),
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=27, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0.0002, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='time', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=3000, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='compute_leaves',
                                        value=Constant(value=False, kind=None),
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
                                    Name(id='time', ctx=Load()),
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
                    name='test_closest_time',
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
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=2, kind=None),
                                    Constant(value=7, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='calendar_dt', ctx=Load()),
                                    Constant(value='It should not return any value for unattended days', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=7, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='range_start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=8, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='range_end', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=19, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='search_range',
                                        value=Tuple(
                                            elts=[
                                                Name(id='range_start', ctx=Load()),
                                                Name(id='range_end', ctx=Load()),
                                            ],
                                            ctx=Load(),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='calendar_dt', ctx=Load()),
                                    Constant(value='It should not return any value if dt outside of range', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=7, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=8, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='start', ctx=Load()),
                                    Constant(value='It should return the start of the day', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=10, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=8, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='start', ctx=Load()),
                                    Constant(value='It should return the start of the closest attendance', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=7, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=13, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='match_end',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                    Constant(value='It should return the end of the closest attendance', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=14, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=13, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='match_end',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                    Constant(value='It should return the end of the closest attendance', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=8, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='start', ctx=Load()),
                                    Constant(value='It should return the start of the closest attendance', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=23, kind=None),
                                    Constant(value=59, kind=None),
                                    Constant(value=59, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=23, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='match_end',
                                        value=Constant(value=True, kind=None),
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                    Constant(value='It should return the end of the closest attendance', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.attendance', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='dayofweek', kind=None),
                                            Constant(value='hour_from', kind=None),
                                            Constant(value='hour_to', kind=None),
                                            Constant(value='resource_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Att4', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_john',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='4', kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=6, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=8, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='start', ctx=Load()),
                                    Constant(value='It should not take into account resouce specific attendances', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=5, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='resource',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='resource_id',
                                            ctx=Load(),
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='start', ctx=Load()),
                                    Constant(value="It should have taken john's specific attendances", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Constant(value='UTC', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime_tz', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=4, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=16, kind=None),
                                    Constant(value=0, kind=None),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='tz',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_john',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_work_time',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dt', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='resource',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='john',
                                                ctx=Load(),
                                            ),
                                            attr='resource_id',
                                            ctx=Load(),
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
                                    Name(id='calendar_dt', ctx=Load()),
                                    Name(id='start', ctx=Load()),
                                    Constant(value='It should have found the attendance on the 3rd April', kind=None),
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
            name='TestResMixin',
            bases=[Name(id='TestResourceCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_adjust_calendar',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paul',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Constant(value='UTC', kind=None),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Constant(value='UTC', kind=None),
                                            ),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='paul',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Constant(value='UTC', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_tz', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Constant(value='UTC', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='It should have found the start and end of the shift on the same day on April 2nd, 2020', kind=None),
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
                    name='test_adjust_calendar_timezone_after',
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
                            targets=[Name(id='tz', ctx=Store())],
                            value=Constant(value='Europe/Brussels', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='tz', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=21, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='It should have found a starting time the 3rd', kind=None),
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
                    name='test_work_days_data',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=5, kind=None),
                                            Constant(value=40, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=4.5, kind=None),
                                            Constant(value=36, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=4.875, kind=None),
                                            Constant(value=39, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1.4375, kind=None),
                                            Constant(value=13, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1.1875, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=2, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='calendar',
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='calendar_jean',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=5, kind=None),
                                            Constant(value=40, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='half', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=14, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=4.5, kind=None),
                                            Constant(value=36, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='calendar',
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='calendar_jean',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=5, kind=None),
                                            Constant(value=40, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=5, kind=None),
                                            Constant(value=40, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='small', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='days', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='hours', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=40, kind=None),
                                    Constant(value=2, kind=None),
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
                    name='test_leaves_days_data',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean is visiting India', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean is comming in USA', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=12, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='datas', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='patel',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='patel',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='calendar',
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='calendar_jean',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='patel',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Subscript(
                                        value=Name(id='datas', ctx=Load()),
                                        slice=Constant(value='days', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='datas', ctx=Load()),
                                        slice=Constant(value='hours', kind=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='John is sick', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=20, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='John goes to holywood', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=7, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='john',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='john',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0.9375, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='half', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=14, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0.5, kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='small', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jean',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='days', kind=None),
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='hours', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_list_leaves',
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
                            targets=[Name(id='jean_leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value="Jean's son is sick", kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=59, kind=None),
                                                    Constant(value=59, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='leaves', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                    Name(id='jean_leave', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='half', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=14, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='leaves', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=4, kind=None),
                                                    Name(id='leave', ctx=Load()),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='small', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='leaves', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='leaves', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='leaves', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value=2, kind=None),
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
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='leaves', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='leave', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='leaves', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_list_work_time_per_day',
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
                            targets=[Name(id='working_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='working_time', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=13, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=12, kind=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Europe/Brussels', kind=None),
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='john',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Europe/Brussels', kind=None),
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='calendar_john',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    Constant(value='America/Los_Angeles', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='working_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='john',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=59, kind=None),
                                            Constant(value=59, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='john',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='working_time', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=13, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=12, kind=None),
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
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='small', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=14, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='working_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='working_time', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=3, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=4, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=6, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='small', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='working_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='working_time', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='working_time', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='working_time', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=8, kind=None),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='zero', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='jean',
                                                                ctx=Load(),
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='working_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=23, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tz',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='working_time', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=3, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=4, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=5, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=6, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
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
            name='TestTimezones',
            bases=[Name(id='TestResourceCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestTimezones', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tz1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Etc/GMT+6', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tz2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Europe/Brussels', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tz3',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Etc/GMT-10', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='tz4',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Etc/GMT+10', kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_work_hours_count',
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
                            targets=[Name(id='count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                                    Name(id='count', ctx=Load()),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='count', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='count', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='get_work_hours_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='count', ctx=Load()),
                                    Constant(value=8, kind=None),
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
                    name='test_plan_hours',
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
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                                    Name(id='dt', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_hours',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=10, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='dt', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=22, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                    name='test_plan_days',
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
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                                    Name(id='dt', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_jean',
                                        ctx=Load(),
                                    ),
                                    attr='plan_days',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=2, kind=None),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='dt', ctx=Load()),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=12, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                    name='test_work_data',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=8, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=4.75, kind=None),
                                            Constant(value=38, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=8, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz3',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz3',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=4, kind=None),
                                            Constant(value=32, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=8, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz2',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz4',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=5, kind=None),
                                            Constant(value=40, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jules',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=6, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jules',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=4, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jules',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=2, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=14, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jules',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=6, kind=None),
                                            Constant(value=46, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jules',
                                            ctx=Load(),
                                        ),
                                        attr='_get_work_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2014, kind=None),
                                                Constant(value=12, kind=None),
                                                Constant(value=29, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2019, kind=None),
                                                Constant(value=12, kind=None),
                                                Constant(value=27, kind=None),
                                                Constant(value=23, kind=None),
                                                Constant(value=59, kind=None),
                                                Constant(value=59, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jules',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=784, kind=None),
                                            Constant(value=6010, kind=None),
                                        ],
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
                    name='test_leave_data',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tz2',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=14, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tz2',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=8, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0.5, kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=8, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz3',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz3',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0.75, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jean',
                                            ctx=Load(),
                                        ),
                                        attr='_get_leave_days_data_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=9, kind=None),
                                                Constant(value=8, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz2',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Call(
                                            func=Name(id='datetime_tz', ctx=Load()),
                                            args=[
                                                Constant(value=2018, kind=None),
                                                Constant(value=4, kind=None),
                                                Constant(value=13, kind=None),
                                                Constant(value=16, kind=None),
                                                Constant(value=0, kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='tz4',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
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
                                    Name(id='data', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='days', kind=None),
                                            Constant(value='hours', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0.75, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
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
                    name='test_leaves',
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
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar.leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='resource_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                        ],
                                        values=[
                                            Constant(value='', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='jean',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tz2',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='datetime_str', ctx=Load()),
                                                args=[
                                                    Constant(value=2018, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=14, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='tzinfo',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tz2',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                                    Name(id='leaves', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=9, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=4, kind=None),
                                                    Name(id='leave', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='leaves', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=9, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=6, kind=None),
                                                    Name(id='leave', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_leaves',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='leaves', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=9, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=6, kind=None),
                                                    Name(id='leave', ctx=Load()),
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
                    name='test_works',
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
                            targets=[Name(id='work', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
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
                                    Name(id='work', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=9, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=6, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=11, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=12, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=13, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
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
                        Assign(
                            targets=[Name(id='work', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='work', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
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
                                    Name(id='work', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=9, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=11, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=12, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
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
                        Assign(
                            targets=[Name(id='work', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jean',
                                        ctx=Load(),
                                    ),
                                    attr='list_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=9, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='datetime_tz', ctx=Load()),
                                        args=[
                                            Constant(value=2018, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tz4',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                                    Name(id='work', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=9, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=11, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=12, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='date', ctx=Load()),
                                                        args=[
                                                            Constant(value=2018, kind=None),
                                                            Constant(value=4, kind=None),
                                                            Constant(value=13, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=8, kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
