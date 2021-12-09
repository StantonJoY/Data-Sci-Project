Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='time', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.rrule',
            names=[
                alias(name='rrule', asname=None),
                alias(name='DAILY', asname=None),
                alias(name='WEEKLY', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='itertools',
            names=[alias(name='chain', asname=None)],
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
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.res_partner',
            names=[alias(name='_tz_get', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_round', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='date_utils', asname=None),
                alias(name='float_utils', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='resource_mixin',
            names=[alias(name='timezone_datetime', asname=None)],
            level=1,
        ),
        Assign(
            targets=[Name(id='HOURS_PER_DAY', ctx=Store())],
            value=Constant(value=8, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='ROUNDING_FACTOR', ctx=Store())],
            value=Constant(value=16, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='make_aware',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='dt', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return ``dt`` with an explicit timezone, together with a function to\n        convert a datetime to the same (naive or aware) timezone as ``dt``.\n    ', kind=None),
                ),
                If(
                    test=Attribute(
                        value=Name(id='dt', ctx=Load()),
                        attr='tzinfo',
                        ctx=Load(),
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='dt', ctx=Load()),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='val', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='val', ctx=Load()),
                                                attr='astimezone',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='dt', ctx=Load()),
                                                    attr='tzinfo',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='dt', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='val', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='val', ctx=Load()),
                                                        attr='astimezone',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='utc', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='replace',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='tzinfo',
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='string_to_datetime',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='value', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert the given string value to a datetime in UTC. ', kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='utc', ctx=Load()),
                            attr='localize',
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
                                args=[Name(id='value', ctx=Load())],
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
            name='datetime_to_string',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='dt', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert the given datetime (converted in UTC) to a string value. ', kind=None),
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
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='dt', ctx=Load()),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[Name(id='utc', ctx=Load())],
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
            name='float_to_time',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='hours', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert a number of hours into a time object. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='hours', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value=24.0, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Name(id='time', ctx=Load()),
                                attr='max',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='fractional', ctx=Store()),
                                Name(id='integral', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=Name(id='math', ctx=Load()),
                            attr='modf',
                            ctx=Load(),
                        ),
                        args=[Name(id='hours', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='time', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='integral', ctx=Load())],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value=60, kind=None),
                                                op=Mult(),
                                                right=Name(id='fractional', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
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
            name='Intervals',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Collection of ordered disjoint intervals with some associated records.\n        Each interval is a triple ``(start, stop, records)``, where ``records``\n        is a recordset.\n    ', kind=None),
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
                                                    Name(id='intervals', ctx=Load()),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='stop', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
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
                                func=Name(id='Intervals', ctx=Load()),
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
                                func=Name(id='Intervals', ctx=Load()),
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
                                    Name(id='self', ctx=Load()),
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
                                    Name(id='other', ctx=Load()),
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
                                keywords=[],
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
        ClassDef(
            name='ResourceCalendar',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Calendar model for a resource. It has\n\n     - attendance_ids: list of resource.calendar.attendance that are a working\n                       interval in a given weekday.\n     - leave_ids: list of leaves linked to this calendar. A leave can be general\n                  or linked to a specific resource, depending on its resource_id.\n\n    All methods in this class use intervals. An interval is a tuple holding\n    (begin_datetime, end_datetime). A list of intervals is therefore a list of\n    tuples, holding several intervals of work or leaves. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='resource.calendar', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Resource Working Time', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceCalendar', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
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
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='name', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='company_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Working Hours of %s', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.company', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Constant(value='company_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='attendance_ids', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='attendance_ids', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='company_id', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='company_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company_attendance_ids', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='resource_calendar_id',
                                            ctx=Load(),
                                        ),
                                        attr='attendance_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='company_attendance_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='attendance_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='dayofweek', kind=None),
                                                                Constant(value='hour_from', kind=None),
                                                                Constant(value='hour_to', kind=None),
                                                                Constant(value='day_period', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='attendance', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='attendance', ctx=Load()),
                                                                    attr='dayofweek',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='attendance', ctx=Load()),
                                                                    attr='hour_from',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='attendance', ctx=Load()),
                                                                    attr='hour_to',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='attendance', ctx=Load()),
                                                                    attr='day_period',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='attendance', ctx=Store()),
                                                        iter=Name(id='company_attendance_ids', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='attendance_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Monday Morning', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='0', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Monday Afternoon', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='0', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Tuesday Morning', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='1', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Tuesday Afternoon', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='1', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Wednesday Morning', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='2', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Wednesday Afternoon', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='2', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Thursday Morning', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='3', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Thursday Afternoon', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='3', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Friday Morning', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='4', kind=None),
                                                                    Constant(value=8, kind=None),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value='morning', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='dayofweek', kind=None),
                                                                    Constant(value='hour_from', kind=None),
                                                                    Constant(value='hour_to', kind=None),
                                                                    Constant(value='day_period', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Friday Afternoon', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value='4', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=17, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If the active field is set to false, it will allow you to hide the Working Time without removing it.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='Company', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attendance_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.calendar.attendance', kind=None),
                            Constant(value='calendar_id', kind=None),
                            Constant(value='Working Time', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_attendance_ids', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='leave_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.calendar.leaves', kind=None),
                            Constant(value='calendar_id', kind=None),
                            Constant(value='Time Off', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='global_leave_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.calendar.leaves', kind=None),
                            Constant(value='calendar_id', kind=None),
                            Constant(value='Global Time Off', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_global_leave_ids', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='resource_id', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='hours_per_day', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Average Hour per Day', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Name(id='HOURS_PER_DAY', ctx=Load()),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Average hours per day a resource is supposed to work with this calendar.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tz', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_tz_get', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Timezone', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='tz', kind=None)],
                                                keywords=[],
                                            ),
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
                                                ctx=Load(),
                                            ),
                                            Constant(value='UTC', kind=None),
                                        ],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is used in order to define in which timezone the resources will work.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tz_offset', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_tz_offset', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Timezone offset', kind=None),
                            ),
                            keyword(
                                arg='invisible',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='two_weeks_calendar', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Calendar in 2 weeks mode', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='two_weeks_explanation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Explanation', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_two_weeks_explanation', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_attendance_ids',
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
                        For(
                            target=Name(id='calendar', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='c', ctx=Load()),
                                                        attr='_origin',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='c', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='c', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_calendar', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='two_weeks_calendar', kind=None),
                                                    Constant(value='hours_per_day', kind=None),
                                                    Constant(value='tz', kind=None),
                                                    Constant(value='attendance_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='company_calendar', ctx=Load()),
                                                        attr='two_weeks_calendar',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='company_calendar', ctx=Load()),
                                                        attr='hours_per_day',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='company_calendar', ctx=Load()),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value=5, kind=None),
                                                                        Constant(value=0, kind=None),
                                                                        Constant(value=0, kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=ListComp(
                                                            elt=Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='attendance', ctx=Load()),
                                                                            attr='_copy_attendance_vals',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='attendance', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Name(id='company_calendar', ctx=Load()),
                                                                        attr='attendance_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ifs=[
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='attendance', ctx=Load()),
                                                                                attr='resource_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_global_leave_ids',
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
                        For(
                            target=Name(id='calendar', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='c', ctx=Load()),
                                                        attr='_origin',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='c', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='c', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='global_leave_ids', kind=None)],
                                                values=[
                                                    BinOp(
                                                        left=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value=5, kind=None),
                                                                        Constant(value=0, kind=None),
                                                                        Constant(value=0, kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=ListComp(
                                                            elt=Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='leave', ctx=Load()),
                                                                            attr='_copy_leave_vals',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='leave', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='calendar', ctx=Load()),
                                                                                attr='company_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='resource_calendar_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='global_leave_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_tz_offset',
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
                        For(
                            target=Name(id='calendar', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='tz_offset',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='timezone', ctx=Load()),
                                                        args=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='calendar', ctx=Load()),
                                                                        attr='tz',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='GMT', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='strftime',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='%z', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='tz', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='default', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='default', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='name', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='default', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='%s (copy)', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceCalendar', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='returns',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self', kind=None),
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_attendance_ids',
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
                        For(
                            target=Name(id='resource', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='resource', ctx=Load()),
                                                attr='two_weeks_calendar',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='resource', ctx=Load()),
                                                        attr='attendance_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='a', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='a', ctx=Load()),
                                                                attr='display_type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='line_section', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='resource', ctx=Load()),
                                                                    attr='attendance_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sorted',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='sequence', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='display_type',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='In a calendar with 2 weeks mode, all periods need to be in the sections.', kind=None)],
                                                        keywords=[],
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='attendance_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_two_weeks_explanation',
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
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='week_type', ctx=Store())],
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
                                    attr='get_week_type',
                                    ctx=Load(),
                                ),
                                args=[Name(id='today', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='week_type_str', ctx=Store())],
                            value=IfExp(
                                test=Name(id='week_type', ctx=Load()),
                                body=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='second', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='first', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_day', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date_utils', ctx=Load()),
                                    attr='start_of',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='today', ctx=Load()),
                                    Constant(value='week', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_day', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date_utils', ctx=Load()),
                                    attr='end_of',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='today', ctx=Load()),
                                    Constant(value='week', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='two_weeks_explanation',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[
                                    Constant(value='The current week (from %s to %s) correspond to the  %s one.', kind=None),
                                    Name(id='first_day', ctx=Load()),
                                    Name(id='last_day', ctx=Load()),
                                    Name(id='week_type_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='two_weeks_calendar', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_global_attendances',
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
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='attendance_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='attendance', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='date_from',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='date_to',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='resource_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='display_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
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
                    name='_compute_hours_per_day',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attendances', annotation=None, type_comment=None),
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
                                operand=Name(id='attendances', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=0, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='hour_count', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attendance', ctx=Store()),
                            iter=Name(id='attendances', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='hour_count', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='attendance', ctx=Load()),
                                            attr='hour_to',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='attendance', ctx=Load()),
                                            attr='hour_from',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='two_weeks_calendar',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='number_of_days', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='attendances', ctx=Load()),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='cal', annotation=None, type_comment=None)],
                                                                            vararg=None,
                                                                            kwonlyargs=[],
                                                                            kw_defaults=[],
                                                                            kwarg=None,
                                                                            defaults=[],
                                                                        ),
                                                                        body=Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='cal', ctx=Load()),
                                                                                attr='week_type',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value='1', kind=None)],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='dayofweek', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='number_of_days', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='attendances', ctx=Load()),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='cal', annotation=None, type_comment=None)],
                                                                            vararg=None,
                                                                            kwonlyargs=[],
                                                                            kw_defaults=[],
                                                                            kwarg=None,
                                                                            defaults=[],
                                                                        ),
                                                                        body=Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='cal', ctx=Load()),
                                                                                attr='week_type',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value='0', kind=None)],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='dayofweek', kind=None)],
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
                            orelse=[
                                Assign(
                                    targets=[Name(id='number_of_days', ctx=Store())],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='attendances', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='dayofweek', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='float_round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='hour_count', ctx=Load()),
                                        op=Div(),
                                        right=Call(
                                            func=Name(id='float', ctx=Load()),
                                            args=[Name(id='number_of_days', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_digits',
                                        value=Constant(value=2, kind=None),
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
                    name='_onchange_hours_per_day',
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
                            targets=[Name(id='attendances', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_global_attendances',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='hours_per_day',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_hours_per_day',
                                    ctx=Load(),
                                ),
                                args=[Name(id='attendances', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='attendance_ids', kind=None),
                                Constant(value='two_weeks_calendar', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='switch_calendar_type',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='two_weeks_calendar',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='attendance_ids',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
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
                                            attr='attendance_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='dayofweek', kind=None),
                                                            Constant(value='sequence', kind=None),
                                                            Constant(value='hour_from', kind=None),
                                                            Constant(value='day_period', kind=None),
                                                            Constant(value='week_type', kind=None),
                                                            Constant(value='hour_to', kind=None),
                                                            Constant(value='display_type', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='First week', kind=None),
                                                            Constant(value='0', kind=None),
                                                            Constant(value='0', kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='morning', kind=None),
                                                            Constant(value='0', kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='line_section', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='dayofweek', kind=None),
                                                            Constant(value='sequence', kind=None),
                                                            Constant(value='hour_from', kind=None),
                                                            Constant(value='day_period', kind=None),
                                                            Constant(value='week_type', kind=None),
                                                            Constant(value='hour_to', kind=None),
                                                            Constant(value='display_type', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Second week', kind=None),
                                                            Constant(value='0', kind=None),
                                                            Constant(value='25', kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='morning', kind=None),
                                                            Constant(value='1', kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='line_section', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='two_weeks_calendar',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='default_attendance', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='default_get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='attendance_ids', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='attendance_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='idx', ctx=Store()),
                                            Name(id='att', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='default_attendance', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='att', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='week_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='0', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='att', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sequence', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Name(id='idx', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='attendance_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='default_attendance', ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='idx', ctx=Store()),
                                            Name(id='att', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='default_attendance', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='att', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='week_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='1', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='att', ctx=Load()),
                                                        slice=Constant(value=2, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sequence', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Name(id='idx', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=26, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='attendance_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='default_attendance', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='two_weeks_calendar',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='attendance_ids',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
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
                                            attr='attendance_ids',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='default_get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='attendance_ids', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='attendance_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_onchange_hours_per_day',
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
                    name='_onchange_attendance_ids',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='two_weeks_calendar',
                                    ctx=Load(),
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='even_week_seq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='attendance_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='att', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='att', ctx=Load()),
                                                        attr='display_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='line_section', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='att', ctx=Load()),
                                                        attr='week_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='0', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='odd_week_seq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='attendance_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='att', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='att', ctx=Load()),
                                                        attr='display_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='line_section', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='att', ctx=Load()),
                                                        attr='week_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='1', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
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
                                            args=[Name(id='even_week_seq', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='odd_week_seq', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You can't delete section between weeks.", kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='even_week_seq', ctx=Store())],
                            value=Attribute(
                                value=Name(id='even_week_seq', ctx=Load()),
                                attr='sequence',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='odd_week_seq', ctx=Store())],
                            value=Attribute(
                                value=Name(id='odd_week_seq', ctx=Load()),
                                attr='sequence',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='attendance_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='att', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='att', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Is()],
                                            comparators=[Constant(value=False, kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='even_week_seq', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Name(id='odd_week_seq', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='week_type',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Name(id='even_week_seq', ctx=Load()),
                                                    ops=[Gt()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='sequence',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                body=Constant(value='1', kind=None),
                                                orelse=Constant(value='0', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='week_type',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Name(id='odd_week_seq', ctx=Load()),
                                                    ops=[Gt()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='sequence',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                body=Constant(value='0', kind=None),
                                                orelse=Constant(value='1', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='attendance_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_overlap',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attendance_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' attendance_ids correspond to attendance of a week,\n            will check for each day of week that there are no superimpose. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attendance', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='attendance_ids', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='att', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='att', ctx=Load()),
                                                        attr='date_from',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='att', ctx=Load()),
                                                        attr='date_to',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='attendance', ctx=Load()),
                                                                            attr='dayofweek',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                op=Mult(),
                                                                right=Constant(value=24, kind=None),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='attendance', ctx=Load()),
                                                                attr='hour_from',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=1e-06, kind=None),
                                                    ),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='attendance', ctx=Load()),
                                                                        attr='dayofweek',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            op=Mult(),
                                                            right=Constant(value=24, kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Name(id='attendance', ctx=Load()),
                                                            attr='hour_to',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='attendance', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='Intervals', ctx=Load()),
                                            args=[Name(id='result', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='result', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Attendances can't overlap.", kind=None)],
                                                keywords=[],
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
                    name='_check_attendance',
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
                        For(
                            target=Name(id='calendar', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='attendance_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='calendar', ctx=Load()),
                                                attr='attendance_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='attendance', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='attendance', ctx=Load()),
                                                                attr='resource_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='attendance', ctx=Load()),
                                                                attr='display_type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Is()],
                                                            comparators=[Constant(value=False, kind=None)],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='two_weeks_calendar',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_check_overlap',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='attendance_ids', ctx=Load()),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='attendance', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='attendance', ctx=Load()),
                                                                        attr='week_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='0', kind=None)],
                                                                ),
                                                            ),
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
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_check_overlap',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='attendance_ids', ctx=Load()),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='attendance', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='attendance', ctx=Load()),
                                                                        attr='week_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='1', kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_check_overlap',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attendance_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='attendance_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_attendance_intervals_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='resources', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Return the attendance intervals in the given datetime range.\n            The returned intervals are expressed in specified tz or in the resource's timezone.\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='resources', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Name(id='resources', ctx=Load()),
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='resource.resource', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Name(id='resources', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='start_dt', ctx=Load()),
                                        attr='tzinfo',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='end_dt', ctx=Load()),
                                        attr='tzinfo',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combine', ctx=Store())],
                            value=Attribute(
                                value=Name(id='datetime', ctx=Load()),
                                attr='combine',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resources_list', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='resources', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='resource.resource', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resource_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources_list', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='domain', ctx=Load()),
                                    ops=[IsNot()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Name(id='domain', ctx=Load()),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='calendar_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='resource_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='resource_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='display_type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cache_dates', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cache_deltas', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='dict', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attendance', ctx=Store()),
                            iter=Call(
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='resource', ctx=Store()),
                                    iter=Name(id='resources_list', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tz', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='tz', ctx=Load()),
                                                body=Name(id='tz', ctx=Load()),
                                                orelse=Call(
                                                    func=Name(id='timezone', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='resource', ctx=Load()),
                                                                    Name(id='self', ctx=Load()),
                                                                ],
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Tuple(
                                                    elts=[
                                                        Name(id='tz', ctx=Load()),
                                                        Name(id='start_dt', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='cache_dates', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='cache_dates', ctx=Load()),
                                                        slice=Tuple(
                                                            elts=[
                                                                Name(id='tz', ctx=Load()),
                                                                Name(id='start_dt', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='start_dt', ctx=Load()),
                                                            attr='astimezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tz', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='cache_dates', ctx=Load()),
                                                            slice=Tuple(
                                                                elts=[
                                                                    Name(id='tz', ctx=Load()),
                                                                    Name(id='start_dt', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='start', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Tuple(
                                                    elts=[
                                                        Name(id='tz', ctx=Load()),
                                                        Name(id='end_dt', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='cache_dates', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='end', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='cache_dates', ctx=Load()),
                                                        slice=Tuple(
                                                            elts=[
                                                                Name(id='tz', ctx=Load()),
                                                                Name(id='end_dt', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='end', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='end_dt', ctx=Load()),
                                                            attr='astimezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tz', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='cache_dates', ctx=Load()),
                                                            slice=Tuple(
                                                                elts=[
                                                                    Name(id='tz', ctx=Load()),
                                                                    Name(id='end_dt', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='end', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='start', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='start', ctx=Load()),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='attendance', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            Name(id='start', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='attendance', ctx=Load()),
                                                                attr='date_from',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='until', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='end', ctx=Load()),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='attendance', ctx=Load()),
                                                attr='date_to',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='until', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='min', ctx=Load()),
                                                        args=[
                                                            Name(id='until', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='attendance', ctx=Load()),
                                                                attr='date_to',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='attendance', ctx=Load()),
                                                attr='week_type',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='start_week_type', ctx=Store())],
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
                                                            attr='get_week_type',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='start', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='start_week_type', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='attendance', ctx=Load()),
                                                                        attr='week_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='start', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='start', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='weeks',
                                                                            value=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='weekday', ctx=Store())],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='dayofweek',
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
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='two_weeks_calendar',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='week_type',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='days', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='rrule', ctx=Load()),
                                                        args=[
                                                            Name(id='WEEKLY', ctx=Load()),
                                                            Name(id='start', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='interval',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='until',
                                                                value=Name(id='until', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='byweekday',
                                                                value=Name(id='weekday', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='days', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='rrule', ctx=Load()),
                                                        args=[
                                                            Name(id='DAILY', ctx=Load()),
                                                            Name(id='start', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='until',
                                                                value=Name(id='until', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='byweekday',
                                                                value=Name(id='weekday', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        For(
                                            target=Name(id='day', ctx=Store()),
                                            iter=Name(id='days', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='hour_from', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='hour_from',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Tuple(
                                                            elts=[
                                                                Name(id='tz', ctx=Load()),
                                                                Name(id='day', ctx=Load()),
                                                                Name(id='hour_from', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='cache_deltas', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='dt0', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='cache_deltas', ctx=Load()),
                                                                slice=Tuple(
                                                                    elts=[
                                                                        Name(id='tz', ctx=Load()),
                                                                        Name(id='day', ctx=Load()),
                                                                        Name(id='hour_from', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='dt0', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tz', ctx=Load()),
                                                                    attr='localize',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='combine', ctx=Load()),
                                                                        args=[
                                                                            Name(id='day', ctx=Load()),
                                                                            Call(
                                                                                func=Name(id='float_to_time', ctx=Load()),
                                                                                args=[Name(id='hour_from', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='cache_deltas', ctx=Load()),
                                                                    slice=Tuple(
                                                                        elts=[
                                                                            Name(id='tz', ctx=Load()),
                                                                            Name(id='day', ctx=Load()),
                                                                            Name(id='hour_from', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='dt0', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                Assign(
                                                    targets=[Name(id='hour_to', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='attendance', ctx=Load()),
                                                        attr='hour_to',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Tuple(
                                                            elts=[
                                                                Name(id='tz', ctx=Load()),
                                                                Name(id='day', ctx=Load()),
                                                                Name(id='hour_to', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='cache_deltas', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='dt1', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='cache_deltas', ctx=Load()),
                                                                slice=Tuple(
                                                                    elts=[
                                                                        Name(id='tz', ctx=Load()),
                                                                        Name(id='day', ctx=Load()),
                                                                        Name(id='hour_to', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='dt1', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tz', ctx=Load()),
                                                                    attr='localize',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='combine', ctx=Load()),
                                                                        args=[
                                                                            Name(id='day', ctx=Load()),
                                                                            Call(
                                                                                func=Name(id='float_to_time', ctx=Load()),
                                                                                args=[Name(id='hour_to', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='cache_deltas', ctx=Load()),
                                                                    slice=Tuple(
                                                                        elts=[
                                                                            Name(id='tz', ctx=Load()),
                                                                            Name(id='day', ctx=Load()),
                                                                            Name(id='hour_to', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='dt1', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='resource', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Call(
                                                                        func=Name(id='max', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='cache_dates', ctx=Load()),
                                                                                slice=Tuple(
                                                                                    elts=[
                                                                                        Name(id='tz', ctx=Load()),
                                                                                        Name(id='start_dt', ctx=Load()),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='dt0', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='min', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='cache_dates', ctx=Load()),
                                                                                slice=Tuple(
                                                                                    elts=[
                                                                                        Name(id='tz', ctx=Load()),
                                                                                        Name(id='end_dt', ctx=Load()),
                                                                                    ],
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='dt1', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='attendance', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Name(id='Intervals', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources_list', ctx=Load()),
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
                    name='_leave_intervals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='resource', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='resource', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resource', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.resource', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_leave_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='start_dt', ctx=Load()),
                                        Name(id='end_dt', ctx=Load()),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='resources',
                                            value=Name(id='resource', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='domain',
                                            value=Name(id='domain', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='tz',
                                            value=Name(id='tz', ctx=Load()),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_leave_intervals_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='resources', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Return the leave intervals in the given datetime range.\n            The returned intervals are expressed in specified tz or in the calendar's timezone.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='resources', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Name(id='resources', ctx=Load()),
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='resource.resource', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Name(id='resources', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='start_dt', ctx=Load()),
                                        attr='tzinfo',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='end_dt', ctx=Load()),
                                        attr='tzinfo',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='resources_list', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='resources', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='resource.resource', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resource_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources_list', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='domain', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='time_type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='leave', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=BinOp(
                                left=Name(id='domain', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='calendar_id', kind=None),
                                                Constant(value='in', kind=None),
                                                List(
                                                    elts=[
                                                        Constant(value=False, kind=None),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='resource_id', kind=None),
                                                Constant(value='in', kind=None),
                                                Name(id='resource_ids', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='date_from', kind=None),
                                                Constant(value='<=', kind=None),
                                                Call(
                                                    func=Name(id='datetime_to_string', ctx=Load()),
                                                    args=[Name(id='end_dt', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='date_to', kind=None),
                                                Constant(value='>=', kind=None),
                                                Call(
                                                    func=Name(id='datetime_to_string', ctx=Load()),
                                                    args=[Name(id='start_dt', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=List(elts=[], ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tz_dates', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='leave', ctx=Store()),
                            iter=Call(
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='resource', ctx=Store()),
                                    iter=Name(id='resources_list', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='leave', ctx=Load()),
                                                        attr='resource_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Name(id='resource', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='tz', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='tz', ctx=Load()),
                                                body=Name(id='tz', ctx=Load()),
                                                orelse=Call(
                                                    func=Name(id='timezone', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='resource', ctx=Load()),
                                                                    Name(id='self', ctx=Load()),
                                                                ],
                                                            ),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Tuple(
                                                    elts=[
                                                        Name(id='tz', ctx=Load()),
                                                        Name(id='start_dt', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='tz_dates', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='tz_dates', ctx=Load()),
                                                        slice=Tuple(
                                                            elts=[
                                                                Name(id='tz', ctx=Load()),
                                                                Name(id='start_dt', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='start_dt', ctx=Load()),
                                                            attr='astimezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tz', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='tz_dates', ctx=Load()),
                                                            slice=Tuple(
                                                                elts=[
                                                                    Name(id='tz', ctx=Load()),
                                                                    Name(id='start_dt', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='start', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Tuple(
                                                    elts=[
                                                        Name(id='tz', ctx=Load()),
                                                        Name(id='end_dt', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='tz_dates', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='end', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='tz_dates', ctx=Load()),
                                                        slice=Tuple(
                                                            elts=[
                                                                Name(id='tz', ctx=Load()),
                                                                Name(id='end_dt', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='end', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='end_dt', ctx=Load()),
                                                            attr='astimezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tz', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='tz_dates', ctx=Load()),
                                                            slice=Tuple(
                                                                elts=[
                                                                    Name(id='tz', ctx=Load()),
                                                                    Name(id='end_dt', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='end', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='dt0', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='string_to_datetime', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='leave', ctx=Load()),
                                                                attr='date_from',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='astimezone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tz', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='dt1', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='string_to_datetime', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='leave', ctx=Load()),
                                                                attr='date_to',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='astimezone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tz', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='result', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='resource', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Call(
                                                                func=Name(id='max', ctx=Load()),
                                                                args=[
                                                                    Name(id='start', ctx=Load()),
                                                                    Name(id='dt0', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='min', ctx=Load()),
                                                                args=[
                                                                    Name(id='end', ctx=Load()),
                                                                    Name(id='dt1', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Name(id='leave', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Name(id='Intervals', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources_list', ctx=Load()),
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
                    name='_work_intervals_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='resources', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the effective work intervals between the given datetimes. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='resources', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resources', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.resource', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='resources_list', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='resources', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='resources_list', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='resources', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='attendance_intervals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_attendance_intervals_batch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start_dt', ctx=Load()),
                                    Name(id='end_dt', ctx=Load()),
                                    Name(id='resources', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Name(id='tz', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave_intervals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_leave_intervals_batch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start_dt', ctx=Load()),
                                    Name(id='end_dt', ctx=Load()),
                                    Name(id='resources', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Name(id='tz', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=BinOp(
                                    left=Subscript(
                                        value=Name(id='attendance_intervals', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    op=Sub(),
                                    right=Subscript(
                                        value=Name(id='leave_intervals', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='r', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources_list', ctx=Load()),
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
                    name='_unavailable_intervals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='resource', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='resource', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resource', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.resource', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_unavailable_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='start_dt', ctx=Load()),
                                        Name(id='end_dt', ctx=Load()),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='resources',
                                            value=Name(id='resource', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='domain',
                                            value=Name(id='domain', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='tz',
                                            value=Name(id='tz', ctx=Load()),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_unavailable_intervals_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='resources', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the unavailable intervals between the given datetimes. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='resources', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resources', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.resource', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='resources_list', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='resources', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='resources_list', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[Name(id='resources', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='resources_work_intervals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_work_intervals_batch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start_dt', ctx=Load()),
                                    Name(id='end_dt', ctx=Load()),
                                    Name(id='resources', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                    Name(id='tz', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='resource', ctx=Store()),
                            iter=Name(id='resources_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='work_intervals', ctx=Store())],
                                    value=ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='start', ctx=Load()),
                                                Name(id='stop', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='start', ctx=Store()),
                                                        Name(id='stop', ctx=Store()),
                                                        Name(id='meta', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Subscript(
                                                    value=Name(id='resources_work_intervals', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='resource', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='work_intervals', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=List(
                                                elts=[Name(id='start_dt', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='chain', ctx=Load()),
                                                            attr='from_iterable',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='work_intervals', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[Name(id='end_dt', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='work_intervals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='map', ctx=Load()),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='dt', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Name(id='dt', ctx=Load()),
                                                                attr='astimezone',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='utc', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Name(id='work_intervals', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='work_intervals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='zip', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='work_intervals', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=0, kind=None),
                                                            upper=None,
                                                            step=Constant(value=2, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='work_intervals', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Constant(value=1, kind=None),
                                                            upper=None,
                                                            step=Constant(value=2, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='resource', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='work_intervals', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_days_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='intervals', annotation=None, type_comment=None),
                            arg(arg='day_total', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        helper function to compute duration of `intervals`\n        expressed in days and hours.\n        `day_total` is a dict {date: n_hours} with the number of hours for each day.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='day_hours', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='float', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='start', ctx=Store()),
                                    Name(id='stop', ctx=Store()),
                                    Name(id='meta', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='intervals', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='day_hours', ctx=Load()),
                                        slice=Call(
                                            func=Attribute(
                                                value=Name(id='start', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=BinOp(
                                                    left=Name(id='stop', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='start', ctx=Load()),
                                                ),
                                                attr='total_seconds',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Constant(value=3600, kind=None),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='days', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=IfExp(
                                            test=Subscript(
                                                value=Name(id='day_total', ctx=Load()),
                                                slice=Name(id='day', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            body=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='float_utils', ctx=Load()),
                                                        attr='round',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=BinOp(
                                                                left=Name(id='ROUNDING_FACTOR', ctx=Load()),
                                                                op=Mult(),
                                                                right=Subscript(
                                                                    value=Name(id='day_hours', ctx=Load()),
                                                                    slice=Name(id='day', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            op=Div(),
                                                            right=Subscript(
                                                                value=Name(id='day_total', ctx=Load()),
                                                                slice=Name(id='day', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Div(),
                                                right=Name(id='ROUNDING_FACTOR', ctx=Load()),
                                            ),
                                            orelse=Constant(value=0, kind=None),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='day', ctx=Store()),
                                                iter=Name(id='day_hours', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='days', kind=None),
                                    Constant(value='hours', kind=None),
                                ],
                                values=[
                                    Name(id='days', ctx=Load()),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='day_hours', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
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
                    name='_get_resources_day_total',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_datetime', annotation=None, type_comment=None),
                            arg(arg='to_datetime', annotation=None, type_comment=None),
                            arg(arg='resources', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        @return dict with hours of attendance in each day between `from_datetime` and `to_datetime`\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='resources', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Name(id='resources', ctx=Load()),
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='resource.resource', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Name(id='resources', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resources_list', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='resources', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='resource.resource', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='from_full', ctx=Store())],
                            value=BinOp(
                                left=Name(id='from_datetime', ctx=Load()),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_full', ctx=Store())],
                            value=BinOp(
                                left=Name(id='to_datetime', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='days',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='intervals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_attendance_intervals_batch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='from_full', ctx=Load()),
                                    Name(id='to_full', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='resources',
                                        value=Name(id='resources', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Call(
                                            func=Name(id='defaultdict', ctx=Load()),
                                            args=[Name(id='float', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='resource', ctx=Store()),
                            iter=Name(id='resources_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='day_total', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='resource', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='start', ctx=Store()),
                                            Name(id='stop', ctx=Store()),
                                            Name(id='meta', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Subscript(
                                        value=Name(id='intervals', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='resource', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='day_total', ctx=Load()),
                                                slice=Call(
                                                    func=Attribute(
                                                        value=Name(id='start', ctx=Load()),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=BinOp(
                                                            left=Name(id='stop', ctx=Load()),
                                                            op=Sub(),
                                                            right=Name(id='start', ctx=Load()),
                                                        ),
                                                        attr='total_seconds',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Div(),
                                                right=Constant(value=3600, kind=None),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_closest_work_time',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dt', annotation=None, type_comment=None),
                            arg(arg='match_end', annotation=None, type_comment=None),
                            arg(arg='resource', annotation=None, type_comment=None),
                            arg(arg='search_range', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the closest work interval boundary within the search range.\n        Consider only starts of intervals unless `match_end` is True. It will then only consider\n        ends of intervals.\n        :param dt: reference datetime\n        :param match_end: wether to search for the begining of an interval or the end.\n        :param search_range: time interval considered. Defaults to the entire day of `dt`\n        :rtype: datetime | None\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='interval_dt',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='interval', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Name(id='interval', ctx=Load()),
                                        slice=IfExp(
                                            test=Name(id='match_end', ctx=Load()),
                                            body=Constant(value=1, kind=None),
                                            orelse=Constant(value=0, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='resource', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resource', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.resource', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='dt', ctx=Load()),
                                            attr='tzinfo',
                                            ctx=Load(),
                                        ),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='search_range', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='search_range', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='tzinfo',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='search_range', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='tzinfo',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='Provided datetimes needs to be timezoned', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dt', ctx=Load()),
                                    attr='astimezone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='timezone', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tz',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='search_range', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='range_start', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='dt', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='hour',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='minute',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='second',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='range_end', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='dt', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                keyword(
                                                    arg='hour',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='minute',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                                keyword(
                                                    arg='second',
                                                    value=Constant(value=0, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='range_start', ctx=Store()),
                                                Name(id='range_end', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='search_range', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Compare(
                                    left=Name(id='range_start', ctx=Load()),
                                    ops=[
                                        LtE(),
                                        LtE(),
                                    ],
                                    comparators=[
                                        Name(id='dt', ctx=Load()),
                                        Name(id='range_end', ctx=Load()),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='work_intervals', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_work_intervals_batch',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='range_start', ctx=Load()),
                                                Name(id='range_end', ctx=Load()),
                                                Name(id='resource', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='resource', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
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
                                            body=Call(
                                                func=Name(id='abs', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='interval_dt', ctx=Load()),
                                                            args=[Name(id='i', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Name(id='dt', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='work_intervals', ctx=Load()),
                                body=Call(
                                    func=Name(id='interval_dt', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Name(id='work_intervals', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value=None, kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_work_hours_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start_dt', annotation=None, type_comment=None),
                            arg(arg='end_dt', annotation=None, type_comment=None),
                            arg(arg='compute_leaves', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            `compute_leaves` controls whether or not this method is taking into\n            account the global leaves.\n\n            `domain` controls the way leaves are recognized.\n            None means default value ('time_type', '=', 'leave')\n\n            Counts the number of work hours between two datetimes.\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='start_dt', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='start_dt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='start_dt', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='end_dt', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='end_dt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='end_dt', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='compute_leaves', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='intervals', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_work_intervals_batch',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='start_dt', ctx=Load()),
                                                Name(id='end_dt', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='domain',
                                                    value=Name(id='domain', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value=False, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='intervals', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_attendance_intervals_batch',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='start_dt', ctx=Load()),
                                                Name(id='end_dt', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=False, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=BinOp(
                                                        left=Name(id='stop', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='start', ctx=Load()),
                                                    ),
                                                    attr='total_seconds',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            op=Div(),
                                            right=Constant(value=3600, kind=None),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='start', ctx=Store()),
                                                        Name(id='stop', ctx=Store()),
                                                        Name(id='meta', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='intervals', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_work_duration_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_datetime', annotation=None, type_comment=None),
                            arg(arg='to_datetime', annotation=None, type_comment=None),
                            arg(arg='compute_leaves', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            Get the working duration (in days and hours) for a given period, only\n            based on the current calendar. This method does not use resource to\n            compute it.\n\n            `domain` is used in order to recognise the leaves to take,\n            None means default value ('time_type', '=', 'leave')\n\n            Returns a dict {'days': n, 'hours': h} containing the\n            quantity of working time expressed as days and as hours.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='from_datetime', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='make_aware', ctx=Load()),
                                args=[Name(id='from_datetime', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='to_datetime', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='make_aware', ctx=Load()),
                                args=[Name(id='to_datetime', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='day_total', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_resources_day_total',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='from_datetime', ctx=Load()),
                                        Name(id='to_datetime', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=False, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='compute_leaves', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='intervals', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_work_intervals_batch',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='from_datetime', ctx=Load()),
                                                Name(id='to_datetime', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='domain',
                                                    value=Name(id='domain', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value=False, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='intervals', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_attendance_intervals_batch',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='from_datetime', ctx=Load()),
                                                Name(id='to_datetime', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='domain',
                                                    value=Name(id='domain', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value=False, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_days_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='intervals', ctx=Load()),
                                    Name(id='day_total', ctx=Load()),
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
                    name='plan_hours',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='hours', annotation=None, type_comment=None),
                            arg(arg='day_dt', annotation=None, type_comment=None),
                            arg(arg='compute_leaves', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='resource', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        `compute_leaves` controls whether or not this method is taking into\n        account the global leaves.\n\n        `domain` controls the way leaves are recognized.\n        None means default value ('time_type', '=', 'leave')\n\n        Return datetime after having planned hours\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='day_dt', ctx=Store()),
                                        Name(id='revert', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='make_aware', ctx=Load()),
                                args=[Name(id='day_dt', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='resource', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resource', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.resource', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='compute_leaves', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='get_intervals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='partial', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_work_intervals_batch',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=Name(id='domain', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='resources',
                                                value=Name(id='resource', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='resource_id', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='resource', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='get_intervals', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_attendance_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='resource_id', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='hours', ctx=Load()),
                                ops=[GtE()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=Call(
                                        func=Name(id='timedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Constant(value=14, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='n', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=100, kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='dt', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='day_dt', ctx=Load()),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Name(id='delta', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='n', ctx=Load()),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='start', ctx=Store()),
                                                    Name(id='stop', ctx=Store()),
                                                    Name(id='meta', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Subscript(
                                                value=Call(
                                                    func=Name(id='get_intervals', ctx=Load()),
                                                    args=[
                                                        Name(id='dt', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='dt', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='delta', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Name(id='resource_id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='interval_hours', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=BinOp(
                                                                    left=Name(id='stop', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Name(id='start', ctx=Load()),
                                                                ),
                                                                attr='total_seconds',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Div(),
                                                        right=Constant(value=3600, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='hours', ctx=Load()),
                                                        ops=[LtE()],
                                                        comparators=[Name(id='interval_hours', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Name(id='revert', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='start', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='timedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='hours',
                                                                                    value=Name(id='hours', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                AugAssign(
                                                    target=Name(id='hours', ctx=Store()),
                                                    op=Sub(),
                                                    value=Name(id='interval_hours', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='hours', ctx=Store())],
                                    value=Call(
                                        func=Name(id='abs', ctx=Load()),
                                        args=[Name(id='hours', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=Call(
                                        func=Name(id='timedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Constant(value=14, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='n', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=100, kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='dt', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='day_dt', ctx=Load()),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Name(id='delta', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='n', ctx=Load()),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='start', ctx=Store()),
                                                    Name(id='stop', ctx=Store()),
                                                    Name(id='meta', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='reversed', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Name(id='get_intervals', ctx=Load()),
                                                            args=[
                                                                BinOp(
                                                                    left=Name(id='dt', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Name(id='delta', ctx=Load()),
                                                                ),
                                                                Name(id='dt', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Name(id='resource_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='interval_hours', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=BinOp(
                                                                    left=Name(id='stop', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Name(id='start', ctx=Load()),
                                                                ),
                                                                attr='total_seconds',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Div(),
                                                        right=Constant(value=3600, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='hours', ctx=Load()),
                                                        ops=[LtE()],
                                                        comparators=[Name(id='interval_hours', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Name(id='revert', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Name(id='stop', ctx=Load()),
                                                                        op=Sub(),
                                                                        right=Call(
                                                                            func=Name(id='timedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='hours',
                                                                                    value=Name(id='hours', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                AugAssign(
                                                    target=Name(id='hours', ctx=Store()),
                                                    op=Sub(),
                                                    value=Name(id='interval_hours', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='plan_days',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='days', annotation=None, type_comment=None),
                            arg(arg='day_dt', annotation=None, type_comment=None),
                            arg(arg='compute_leaves', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        `compute_leaves` controls whether or not this method is taking into\n        account the global leaves.\n\n        `domain` controls the way leaves are recognized.\n        None means default value ('time_type', '=', 'leave')\n\n        Returns the datetime of a days scheduling.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='day_dt', ctx=Store()),
                                        Name(id='revert', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='make_aware', ctx=Load()),
                                args=[Name(id='day_dt', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='compute_leaves', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='get_intervals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='partial', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_work_intervals_batch',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=Name(id='domain', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='get_intervals', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_attendance_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='days', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='found', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=Call(
                                        func=Name(id='timedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Constant(value=14, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='n', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=100, kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='dt', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='day_dt', ctx=Load()),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Name(id='delta', ctx=Load()),
                                                    op=Mult(),
                                                    right=Name(id='n', ctx=Load()),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='start', ctx=Store()),
                                                    Name(id='stop', ctx=Store()),
                                                    Name(id='meta', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Subscript(
                                                value=Call(
                                                    func=Name(id='get_intervals', ctx=Load()),
                                                    args=[
                                                        Name(id='dt', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='dt', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='delta', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=False, kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='found', ctx=Load()),
                                                            attr='add',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='start', ctx=Load()),
                                                                    attr='date',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='found', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='days', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Name(id='revert', ctx=Load()),
                                                                args=[Name(id='stop', ctx=Load())],
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
                                    type_comment=None,
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='days', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='days', ctx=Store())],
                                            value=Call(
                                                func=Name(id='abs', ctx=Load()),
                                                args=[Name(id='days', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='found', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='delta', ctx=Store())],
                                            value=Call(
                                                func=Name(id='timedelta', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='days',
                                                        value=Constant(value=14, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='n', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[Constant(value=100, kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='dt', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='day_dt', ctx=Load()),
                                                        op=Sub(),
                                                        right=BinOp(
                                                            left=Name(id='delta', ctx=Load()),
                                                            op=Mult(),
                                                            right=Name(id='n', ctx=Load()),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='start', ctx=Store()),
                                                            Name(id='stop', ctx=Store()),
                                                            Name(id='meta', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Name(id='reversed', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Call(
                                                                    func=Name(id='get_intervals', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='dt', ctx=Load()),
                                                                            op=Sub(),
                                                                            right=Name(id='delta', ctx=Load()),
                                                                        ),
                                                                        Name(id='dt', ctx=Load()),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=False, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='found', ctx=Load()),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='start', ctx=Load()),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='found', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='days', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Call(
                                                                        func=Name(id='revert', ctx=Load()),
                                                                        args=[Name(id='start', ctx=Load())],
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
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Name(id='revert', ctx=Load()),
                                                args=[Name(id='day_dt', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_max_number_of_hours',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                            arg(arg='end', annotation=None, type_comment=None),
                        ],
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='attendance_ids',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=0, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mapped_data', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Constant(value=0, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attendance', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='attendance_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='a', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='a', ctx=Load()),
                                                                attr='date_from',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=Attribute(
                                                                value=Name(id='a', ctx=Load()),
                                                                attr='date_to',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='a', ctx=Load()),
                                                                attr='date_from',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[LtE()],
                                                            comparators=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='end', ctx=Load()),
                                                                        attr='date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='a', ctx=Load()),
                                                                attr='date_to',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[GtE()],
                                                            comparators=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='start', ctx=Load()),
                                                                        attr='date',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='mapped_data', ctx=Load()),
                                        slice=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='attendance', ctx=Load()),
                                                    attr='week_type',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='attendance', ctx=Load()),
                                                    attr='dayofweek',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='attendance', ctx=Load()),
                                            attr='hour_to',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='attendance', ctx=Load()),
                                            attr='hour_from',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mapped_data', ctx=Load()),
                                            attr='values',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ResourceCalendarAttendance',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='resource.calendar.attendance', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Work Detail', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='week_type, dayofweek, hour_from', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dayofweek', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value='Monday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='1', kind=None),
                                            Constant(value='Tuesday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='2', kind=None),
                                            Constant(value='Wednesday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='3', kind=None),
                                            Constant(value='Thursday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='4', kind=None),
                                            Constant(value='Friday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='5', kind=None),
                                            Constant(value='Saturday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='6', kind=None),
                                            Constant(value='Sunday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Day of Week', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='0', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Starting Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='End Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='hour_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Work from', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Start and End time of working.\nA specific value of 24:00 is interpreted as 23:59:59.999999.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='hour_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Work to', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='calendar_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='resource.calendar', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value="Resource's Calendar", kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='day_period', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='morning', kind=None),
                                            Constant(value='Morning', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='afternoon', kind=None),
                                            Constant(value='Afternoon', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='morning', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='resource_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.resource', kind=None),
                            Constant(value='Resource', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='week_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1', kind=None),
                                            Constant(value='Second', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='0', kind=None),
                                            Constant(value='First', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Week Number', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='two_weeks_calendar', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Calendar in 2 weeks mode', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='calendar_id.two_weeks_calendar', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='line_section', kind=None),
                                            Constant(value='Section', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field for UX purpose.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Gives the sequence of this line when displaying the resource calendar.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_hours',
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
                                    attr='hour_from',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_from',
                                        ctx=Load(),
                                    ),
                                    Constant(value=23.99, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='hour_from',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_from',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='hour_to',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_to',
                                        ctx=Load(),
                                    ),
                                    Constant(value=24, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='hour_to',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_to',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='hour_to',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_to',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_from',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='hour_from', kind=None),
                                Constant(value='hour_to', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_week_type',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='math', ctx=Load()),
                                                attr='floor',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='date', ctx=Load()),
                                                                attr='toordinal',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    op=Div(),
                                                    right=Constant(value=7, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Constant(value=2, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_display_name',
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_display_name',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='this_week_type', ctx=Store())],
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_week_type',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_today',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='section_names', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='0', kind=None),
                                    Constant(value='1', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='First week', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Second week', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='section_info', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value=True, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='this week', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='other week', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='display_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='line_section', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='section_name', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s (%s)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='section_names', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='week_type',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='section_info', ctx=Load()),
                                                    slice=Compare(
                                                        left=Name(id='this_week_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='week_type',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='display_name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='section_name', ctx=Load()),
                                    type_comment=None,
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
                FunctionDef(
                    name='_copy_attendance_vals',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='dayofweek', kind=None),
                                    Constant(value='date_from', kind=None),
                                    Constant(value='date_to', kind=None),
                                    Constant(value='hour_from', kind=None),
                                    Constant(value='hour_to', kind=None),
                                    Constant(value='day_period', kind=None),
                                    Constant(value='week_type', kind=None),
                                    Constant(value='display_type', kind=None),
                                    Constant(value='sequence', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dayofweek',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_from',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hour_to',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='day_period',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='week_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='display_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sequence',
                                        ctx=Load(),
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
        ClassDef(
            name='ResourceResource',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='resource.resource', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Resources', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceResource', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
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
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='calendar_id', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='company_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.company', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='company_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='calendar_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='resource_calendar_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If the active field is set to False, it will allow you to hide the resource record without removing it.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='resource_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='user', kind=None),
                                            Constant(value='Human', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='material', kind=None),
                                            Constant(value='Material', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='user', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='User', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Related user name for the resource to manage its access.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='time_efficiency', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Efficiency Factor', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=100, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is used to calculate the expected duration of a work order at this work center. For example, if a work order takes one hour and the efficiency factor is 100%, then the expected duration will be one hour. If the efficiency factor is 200%, however the expected duration will be 30 minutes.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='calendar_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='resource.calendar', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Working Time', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Define the schedule of resource', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tz', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_tz_get', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Timezone', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='tz', kind=None)],
                                                keywords=[],
                                            ),
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
                                                ctx=Load(),
                                            ),
                                            Constant(value='UTC', kind=None),
                                        ],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is used in order to define in which timezone the resources will work.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='check_time_efficiency', kind=None),
                                    Constant(value='CHECK(time_efficiency>0)', kind=None),
                                    Constant(value='Time efficiency must be strictly positive', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='company_id', kind=None)],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='calendar_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='calendar_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.company', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='company_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='tz', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tz', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='res.users', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='user_id', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='resource.calendar', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='calendar_id', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='tz', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='tz', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='tz', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceResource', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='copy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='default', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='default', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='name', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='default', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='%s (copy)', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceResource', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='returns',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='self', kind=None),
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_company_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='calendar_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='resource_calendar_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='company_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_user_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tz',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='user_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_work_interval',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                            arg(arg='end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
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
                    name='_adjust_to_calendar',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                            arg(arg='end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Adjust the given start and end datetimes to the closest effective hours encoded\n        in the resource calendar. Only attendances in the same day as `start` and `end` are\n        considered (respectively). If no attendance is found during that day, the closest hour\n        is None.\n        e.g. simplified example:\n             given two attendances: 8am-1pm and 2pm-5pm, given start=9am and end=6pm\n             resource._adjust_to_calendar(start, end)\n             >>> {resource: (8am, 5pm)}\n        :return: Closest matching start and end of working periods for each resource\n        :rtype: dict(resource, tuple(datetime | None, datetime | None))\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='start', ctx=Store()),
                                        Name(id='revert_start_tz', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='make_aware', ctx=Load()),
                                args=[Name(id='start', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='end', ctx=Store()),
                                        Name(id='revert_end_tz', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='make_aware', ctx=Load()),
                                args=[Name(id='end', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='resource', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='calendar_start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='resource', ctx=Load()),
                                                attr='calendar_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_closest_work_time',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='start', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='resource',
                                                value=Name(id='resource', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='search_range', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tz', ctx=Store())],
                                    value=Call(
                                        func=Name(id='timezone', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='resource', ctx=Load()),
                                                attr='tz',
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
                                            Name(id='calendar_start', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='start', ctx=Load()),
                                                                attr='astimezone',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='tz', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='date',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='end', ctx=Load()),
                                                                    attr='astimezone',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='tz', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='end', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='end', ctx=Load()),
                                                    attr='astimezone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tz', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='search_range', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Name(id='start', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='end', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Constant(value=1, kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='hour',
                                                                    value=Constant(value=0, kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='minute',
                                                                    value=Constant(value=0, kind=None),
                                                                ),
                                                                keyword(
                                                                    arg='second',
                                                                    value=Constant(value=0, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='calendar_end', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='resource', ctx=Load()),
                                                attr='calendar_id',
                                                ctx=Load(),
                                            ),
                                            attr='_get_closest_work_time',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='end', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='match_end',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='resource',
                                                value=Name(id='resource', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='search_range',
                                                value=Name(id='search_range', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Name(id='resource', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='calendar_start', ctx=Load()),
                                                    Call(
                                                        func=Name(id='revert_start_tz', ctx=Load()),
                                                        args=[Name(id='calendar_start', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='calendar_end', ctx=Load()),
                                                    Call(
                                                        func=Name(id='revert_end_tz', ctx=Load()),
                                                        args=[Name(id='calendar_end', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_unavailable_intervals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                            arg(arg='end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compute the intervals during which employee is unavailable with hour granularity between start and end\n            Note: this method is used in enterprise (forecast and planning)\n\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='start_datetime', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone_datetime', ctx=Load()),
                                args=[Name(id='start', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_datetime', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone_datetime', ctx=Load()),
                                args=[Name(id='end', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resource_mapping', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar_mapping', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='resource.resource', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='resource', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='calendar_mapping', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='resource', ctx=Load()),
                                            attr='calendar_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Name(id='resource', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='calendar', ctx=Store()),
                                    Name(id='resources', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='calendar_mapping', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resources_unavailable_intervals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='_unavailable_intervals_batch',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='start_datetime', ctx=Load()),
                                            Name(id='end_datetime', ctx=Load()),
                                            Name(id='resources', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='resource_mapping', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='resources_unavailable_intervals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='resource_mapping', ctx=Load()),
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
            name='ResourceCalendarLeaves',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='resource.calendar.leaves', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Resource Time Off Detail', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='date_from', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='date_from', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields_list', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='date_to', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields_list', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='date_from', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='date_to', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='today', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='now',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='user_tz', ctx=Store())],
                                    value=Call(
                                        func=Name(id='timezone', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
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
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_context',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='tz', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='resource_calendar_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tz',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='date_from', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='user_tz', ctx=Load()),
                                            attr='localize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='combine',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='today', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='time', ctx=Load()),
                                                        attr='min',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='date_to', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='user_tz', ctx=Load()),
                                            attr='localize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='combine',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='today', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='time', ctx=Load()),
                                                        attr='max',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='intervals', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_work_intervals_batch',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='date_from', ctx=Load()),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='tzinfo',
                                                            value=Name(id='utc', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='date_to', ctx=Load()),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='tzinfo',
                                                            value=Name(id='utc', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=False, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='intervals', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='list_intervals', ctx=Store())],
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='start', ctx=Load()),
                                                        Name(id='stop', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='start', ctx=Store()),
                                                                Name(id='stop', ctx=Store()),
                                                                Name(id='records', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Name(id='intervals', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='date_from', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='list_intervals', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='date_to', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='list_intervals', ctx=Load()),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='date_from',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='date_from', ctx=Load()),
                                                                attr='astimezone',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='utc', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='tzinfo',
                                                            value=Constant(value=None, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='date_to',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='date_to', ctx=Load()),
                                                                attr='astimezone',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='utc', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='tzinfo',
                                                            value=Constant(value=None, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reason', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_company_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='calendar_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.calendar', kind=None),
                            Constant(value='Working Hours', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Start Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='End Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='resource_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.resource', kind=None),
                            Constant(value='Resource', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If empty, this is a generic time off for the company. If a resource is set, the time off is only for this resource', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='time_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='leave', kind=None),
                                            Constant(value='Time Off', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='other', kind=None),
                                            Constant(value='Other', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='leave', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Whether this should be computed as a time off or as work time (eg: formation)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_company_id',
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
                        For(
                            target=Name(id='leave', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='leave', ctx=Load()),
                                            attr='company_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='leave', ctx=Load()),
                                                    attr='calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='calendar_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_dates',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='leave', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='leave', ctx=Load()),
                                                attr='date_from',
                                                ctx=Load(),
                                            ),
                                            ops=[Gt()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='leave', ctx=Load()),
                                                    attr='date_to',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The start date of the time off must be earlier than the end date.', kind=None)],
                                                keywords=[],
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='date_from', kind=None),
                                Constant(value='date_to', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_resource',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='resource_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='calendar_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='resource_id',
                                            ctx=Load(),
                                        ),
                                        attr='calendar_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='resource_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_copy_leave_vals',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='date_from', kind=None),
                                    Constant(value='date_to', kind=None),
                                    Constant(value='time_type', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='time_type',
                                        ctx=Load(),
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
