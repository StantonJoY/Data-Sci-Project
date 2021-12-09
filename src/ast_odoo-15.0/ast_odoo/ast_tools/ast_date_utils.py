Module(
    body=[
        Import(
            names=[alias(name='math', asname=None)],
        ),
        Import(
            names=[alias(name='calendar', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='ustr', asname=None)],
            level=1,
        ),
        ImportFrom(
            module='func',
            names=[alias(name='lazy', asname=None)],
            level=1,
        ),
        FunctionDef(
            name='get_month',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='date', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Compute the month dates range on which the 'date' parameter belongs to.\n\n    :param date: A datetime.datetime or datetime.date object.\n    :return: A tuple (date_from, date_to) having the same object type as the 'date' parameter.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
                    value=Call(
                        func=Call(
                            func=Name(id='type', ctx=Load()),
                            args=[Name(id='date', ctx=Load())],
                            keywords=[],
                        ),
                        args=[
                            Attribute(
                                value=Name(id='date', ctx=Load()),
                                attr='year',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='date', ctx=Load()),
                                attr='month',
                                ctx=Load(),
                            ),
                            Constant(value=1, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Call(
                            func=Name(id='type', ctx=Load()),
                            args=[Name(id='date', ctx=Load())],
                            keywords=[],
                        ),
                        args=[
                            Attribute(
                                value=Name(id='date', ctx=Load()),
                                attr='year',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='date', ctx=Load()),
                                attr='month',
                                ctx=Load(),
                            ),
                            Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='monthrange',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='date', ctx=Load()),
                                            attr='year',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='date', ctx=Load()),
                                            attr='month',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='date_from', ctx=Load()),
                            Name(id='date_to', ctx=Load()),
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
            name='get_quarter_number',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='date', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Get the number of the quarter on which the 'date' parameter belongs to.\n\n    :param date: A datetime.datetime or datetime.date object.\n    :return: A [1-4] integer.\n    ", kind=None),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Name(id='math', ctx=Load()),
                            attr='ceil',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Attribute(
                                    value=Name(id='date', ctx=Load()),
                                    attr='month',
                                    ctx=Load(),
                                ),
                                op=Div(),
                                right=Constant(value=3, kind=None),
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
            name='get_quarter',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='date', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=" Compute the quarter dates range on which the 'date' parameter belongs to.\n\n    :param date: A datetime.datetime or datetime.date object.\n    :return: A tuple (date_from, date_to) having the same object type as the 'date' parameter.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='quarter_number', ctx=Store())],
                    value=Call(
                        func=Name(id='get_quarter_number', ctx=Load()),
                        args=[Name(id='date', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='month_from', ctx=Store())],
                    value=BinOp(
                        left=BinOp(
                            left=BinOp(
                                left=Name(id='quarter_number', ctx=Load()),
                                op=Sub(),
                                right=Constant(value=1, kind=None),
                            ),
                            op=Mult(),
                            right=Constant(value=3, kind=None),
                        ),
                        op=Add(),
                        right=Constant(value=1, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_from', ctx=Store())],
                    value=Call(
                        func=Call(
                            func=Name(id='type', ctx=Load()),
                            args=[Name(id='date', ctx=Load())],
                            keywords=[],
                        ),
                        args=[
                            Attribute(
                                value=Name(id='date', ctx=Load()),
                                attr='year',
                                ctx=Load(),
                            ),
                            Name(id='month_from', ctx=Load()),
                            Constant(value=1, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=BinOp(
                        left=Name(id='date_from', ctx=Load()),
                        op=Add(),
                        right=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='months',
                                    value=Constant(value=2, kind=None),
                                ),
                            ],
                        ),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='date_to', ctx=Load()),
                            attr='replace',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='day',
                                value=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='monthrange',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='date_to', ctx=Load()),
                                                attr='year',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='date_to', ctx=Load()),
                                                attr='month',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    slice=Constant(value=1, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='date_from', ctx=Load()),
                            Name(id='date_to', ctx=Load()),
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
            name='get_fiscal_year',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='date', annotation=None, type_comment=None),
                    arg(arg='day', annotation=None, type_comment=None),
                    arg(arg='month', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=31, kind=None),
                    Constant(value=12, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Compute the fiscal year dates range on which the 'date' parameter belongs to.\n    A fiscal year is the period used by governments for accounting purposes and vary between countries.\n\n    By default, calling this method with only one parameter gives the calendar year because the ending date of the\n    fiscal year is set to the YYYY-12-31.\n\n    :param date:    A datetime.datetime or datetime.date object.\n    :param day:     The day of month the fiscal year ends.\n    :param month:   The month of year the fiscal year ends.\n    :return: A tuple (date_from, date_to) having the same object type as the 'date' parameter.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='max_day', ctx=Store())],
                    value=Subscript(
                        value=Call(
                            func=Attribute(
                                value=Name(id='calendar', ctx=Load()),
                                attr='monthrange',
                                ctx=Load(),
                            ),
                            args=[
                                Attribute(
                                    value=Name(id='date', ctx=Load()),
                                    attr='year',
                                    ctx=Load(),
                                ),
                                Name(id='month', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        slice=Constant(value=1, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_to', ctx=Store())],
                    value=Call(
                        func=Call(
                            func=Name(id='type', ctx=Load()),
                            args=[Name(id='date', ctx=Load())],
                            keywords=[],
                        ),
                        args=[
                            Attribute(
                                value=Name(id='date', ctx=Load()),
                                attr='year',
                                ctx=Load(),
                            ),
                            Name(id='month', ctx=Load()),
                            Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Name(id='day', ctx=Load()),
                                    Name(id='max_day', ctx=Load()),
                                ],
                                keywords=[],
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
                            Compare(
                                left=Attribute(
                                    value=Name(id='date_to', ctx=Load()),
                                    attr='month',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=2, kind=None)],
                            ),
                            Compare(
                                left=Attribute(
                                    value=Name(id='date_to', ctx=Load()),
                                    attr='day',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=28, kind=None)],
                            ),
                            Compare(
                                left=Name(id='max_day', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=29, kind=None)],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_to', ctx=Store())],
                            value=Call(
                                func=Call(
                                    func=Name(id='type', ctx=Load()),
                                    args=[Name(id='date', ctx=Load())],
                                    keywords=[],
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='date', ctx=Load()),
                                        attr='year',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value=29, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='date', ctx=Load()),
                        ops=[LtE()],
                        comparators=[Name(id='date_to', ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=BinOp(
                                left=Name(id='date_to', ctx=Load()),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='years',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='max_day', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='monthrange',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='date_from', ctx=Load()),
                                            attr='year',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='date_from', ctx=Load()),
                                            attr='month',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='date_from', ctx=Load()),
                                            attr='month',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='date_from', ctx=Load()),
                                            attr='day',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=28, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='max_day', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=29, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='date_from', ctx=Store())],
                                    value=Call(
                                        func=Call(
                                            func=Name(id='type', ctx=Load()),
                                            args=[Name(id='date', ctx=Load())],
                                            keywords=[],
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='date_from', ctx=Load()),
                                                attr='year',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            Constant(value=29, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='date_from', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='days',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=BinOp(
                                left=Name(id='date_to', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
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
                            targets=[Name(id='max_day', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='monthrange',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='date_to', ctx=Load()),
                                                attr='year',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        Attribute(
                                            value=Name(id='date_to', ctx=Load()),
                                            attr='month',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_to', ctx=Store())],
                            value=Call(
                                func=Call(
                                    func=Name(id='type', ctx=Load()),
                                    args=[Name(id='date', ctx=Load())],
                                    keywords=[],
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='date', ctx=Load()),
                                            attr='year',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    Name(id='month', ctx=Load()),
                                    Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Name(id='day', ctx=Load()),
                                            Name(id='max_day', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='date_to', ctx=Load()),
                                            attr='month',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='date_to', ctx=Load()),
                                            attr='day',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=28, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='max_day', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=29, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='date_to', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='relativedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Name(id='date_from', ctx=Load()),
                            Name(id='date_to', ctx=Load()),
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
            name='get_timedelta',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='qty', annotation=None, type_comment=None),
                    arg(arg='granularity', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n        Helper to get a `relativedelta` object for the given quantity and interval unit.\n        :param qty: the number of unit to apply on the timedelta to return\n        :param granularity: Type of period in string, can be year, quarter, month, week, day or hour.\n\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='switch', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='hour', kind=None),
                            Constant(value='day', kind=None),
                            Constant(value='week', kind=None),
                            Constant(value='month', kind=None),
                            Constant(value='year', kind=None),
                        ],
                        values=[
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='hours',
                                        value=Name(id='qty', ctx=Load()),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='days',
                                        value=Name(id='qty', ctx=Load()),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='weeks',
                                        value=Name(id='qty', ctx=Load()),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='months',
                                        value=Name(id='qty', ctx=Load()),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='years',
                                        value=Name(id='qty', ctx=Load()),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Subscript(
                        value=Name(id='switch', ctx=Load()),
                        slice=Name(id='granularity', ctx=Load()),
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='start_of',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='granularity', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Get start of a time period from a date or a datetime.\n\n    :param value: initial date or datetime.\n    :param granularity: type of period in string, can be year, quarter, month, week, day or hour.\n    :return: a date/datetime object corresponding to the start of the specified period.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='is_datetime', ctx=Store())],
                    value=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='datetime', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='granularity', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='year', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='value', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='month',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='day',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='granularity', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='quarter', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='get_quarter', ctx=Load()),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='granularity', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='month', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='day',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='granularity', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='week', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='result', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='value', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='calendar', ctx=Load()),
                                                                            attr='weekday',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='value', ctx=Load()),
                                                                                attr='year',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='value', ctx=Load()),
                                                                                attr='month',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='value', ctx=Load()),
                                                                                attr='day',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='granularity', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='day', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='result', ctx=Store())],
                                                            value=Name(id='value', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='granularity', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='hour', kind=None)],
                                                                    ),
                                                                    Name(id='is_datetime', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='datetime', ctx=Load()),
                                                                                    attr='combine',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='value', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='time', ctx=Load()),
                                                                                        attr='min',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='replace',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='hour',
                                                                                value=Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='hour',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Name(id='is_datetime', ctx=Load()),
                                                                    body=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='Granularity must be year, quarter, month, week, day or hour for value %s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Name(id='value', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='Granularity must be year, quarter, month, week or day for value %s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Name(id='value', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=IfExp(
                        test=Name(id='is_datetime', ctx=Load()),
                        body=Call(
                            func=Attribute(
                                value=Name(id='datetime', ctx=Load()),
                                attr='combine',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='result', ctx=Load()),
                                Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='min',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        orelse=Name(id='result', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='end_of',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='value', annotation=None, type_comment=None),
                    arg(arg='granularity', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Get end of a time period from a date or a datetime.\n\n    :param value: initial date or datetime.\n    :param granularity: Type of period in string, can be year, quarter, month, week, day or hour.\n    :return: A date/datetime object corresponding to the start of the specified period.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='is_datetime', ctx=Store())],
                    value=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Name(id='datetime', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='granularity', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='year', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='value', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='month',
                                        value=Constant(value=12, kind=None),
                                    ),
                                    keyword(
                                        arg='day',
                                        value=Constant(value=31, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='granularity', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='quarter', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Name(id='get_quarter', ctx=Load()),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='granularity', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='month', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='value', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='day',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        keyword(
                                                            arg='months',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        keyword(
                                                            arg='days',
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
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='granularity', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='week', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='result', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='value', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='days',
                                                                    value=BinOp(
                                                                        left=Constant(value=6, kind=None),
                                                                        op=Sub(),
                                                                        right=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='calendar', ctx=Load()),
                                                                                attr='weekday',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='year',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='month',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='day',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='granularity', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='day', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='result', ctx=Store())],
                                                            value=Name(id='value', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='granularity', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='hour', kind=None)],
                                                                    ),
                                                                    Name(id='is_datetime', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='datetime', ctx=Load()),
                                                                                    attr='combine',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Name(id='value', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='time', ctx=Load()),
                                                                                        attr='max',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='replace',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='hour',
                                                                                value=Attribute(
                                                                                    value=Name(id='value', ctx=Load()),
                                                                                    attr='hour',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Name(id='is_datetime', ctx=Load()),
                                                                    body=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='Granularity must be year, quarter, month, week, day or hour for value %s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Name(id='value', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='Granularity must be year, quarter, month, week or day for value %s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Name(id='value', ctx=Load()),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=IfExp(
                        test=Name(id='is_datetime', ctx=Load()),
                        body=Call(
                            func=Attribute(
                                value=Name(id='datetime', ctx=Load()),
                                attr='combine',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='result', ctx=Load()),
                                Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='max',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        orelse=Name(id='result', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='add',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='value', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Return the sum of ``value`` and a :class:`relativedelta`.\n\n    :param value: initial date or datetime.\n    :param args: positional args to pass directly to :class:`relativedelta`.\n    :param kwargs: keyword args to pass directly to :class:`relativedelta`.\n    :return: the resulting date/datetime.\n    ', kind=None),
                ),
                Return(
                    value=BinOp(
                        left=Name(id='value', ctx=Load()),
                        op=Add(),
                        right=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[
                                Starred(
                                    value=Name(id='args', ctx=Load()),
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg=None,
                                    value=Name(id='kwargs', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='subtract',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='value', annotation=None, type_comment=None)],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Return the difference between ``value`` and a :class:`relativedelta`.\n\n    :param value: initial date or datetime.\n    :param args: positional args to pass directly to :class:`relativedelta`.\n    :param kwargs: keyword args to pass directly to :class:`relativedelta`.\n    :return: the resulting date/datetime.\n    ', kind=None),
                ),
                Return(
                    value=BinOp(
                        left=Name(id='value', ctx=Load()),
                        op=Sub(),
                        right=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[
                                Starred(
                                    value=Name(id='args', ctx=Load()),
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg=None,
                                    value=Name(id='kwargs', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='json_default',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='obj', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Properly serializes date and datetime objects.\n    ', kind=None),
                ),
                ImportFrom(
                    module='odoo',
                    names=[alias(name='fields', asname=None)],
                    level=0,
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='obj', ctx=Load()),
                            Name(id='datetime', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
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
                                args=[Name(id='obj', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='obj', ctx=Load()),
                            Name(id='date', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[Name(id='obj', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='obj', ctx=Load()),
                            Name(id='lazy', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Name(id='obj', ctx=Load()),
                                attr='_value',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[Name(id='obj', ctx=Load())],
                        keywords=[],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='date_range',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='start', annotation=None, type_comment=None),
                    arg(arg='end', annotation=None, type_comment=None),
                    arg(arg='step', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Call(
                        func=Name(id='relativedelta', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='months',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Date range generator with a step interval.\n\n    :param start datetime: beginning date of the range.\n    :param end datetime: ending date of the range.\n    :param step relativedelta: interval of the range.\n    :return: a range of datetime from start to end.\n    :rtype: Iterator[datetime]\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='are_naive', ctx=Store())],
                    value=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Attribute(
                                    value=Name(id='start', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            Compare(
                                left=Attribute(
                                    value=Name(id='end', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='are_utc', ctx=Store())],
                    value=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Attribute(
                                    value=Name(id='start', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='pytz', ctx=Load()),
                                        attr='utc',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            Compare(
                                left=Attribute(
                                    value=Name(id='end', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='pytz', ctx=Load()),
                                        attr='utc',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='are_others', ctx=Store())],
                    value=BoolOp(
                        op=And(),
                        values=[
                            Attribute(
                                value=Name(id='start', ctx=Load()),
                                attr='tzinfo',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='end', ctx=Load()),
                                attr='tzinfo',
                                ctx=Load(),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='are_utc', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='are_others', ctx=Load()),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='start', ctx=Load()),
                                        attr='tzinfo',
                                        ctx=Load(),
                                    ),
                                    attr='zone',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='end', ctx=Load()),
                                            attr='tzinfo',
                                            ctx=Load(),
                                        ),
                                        attr='zone',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='Timezones of start argument and end argument seem inconsistent', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='are_naive', ctx=Load()),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='are_utc', ctx=Load()),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Name(id='are_others', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[Constant(value='Timezones of start argument and end argument mismatch', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='start', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Name(id='end', ctx=Load())],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[Constant(value='start > end, start date must be before end', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Compare(
                        left=Name(id='start', ctx=Load()),
                        ops=[Eq()],
                        comparators=[
                            BinOp(
                                left=Name(id='start', ctx=Load()),
                                op=Add(),
                                right=Name(id='step', ctx=Load()),
                            ),
                        ],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='ValueError', ctx=Load()),
                                args=[Constant(value='Looks like step is null', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Attribute(
                        value=Name(id='start', ctx=Load()),
                        attr='tzinfo',
                        ctx=Load(),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='localize', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='start', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                                attr='localize',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='localize', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='dt', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Name(id='dt', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='dt', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='start', ctx=Load()),
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
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='end', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='end', ctx=Load()),
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
                    type_comment=None,
                ),
                While(
                    test=Compare(
                        left=Name(id='dt', ctx=Load()),
                        ops=[LtE()],
                        comparators=[Name(id='end', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Call(
                                    func=Name(id='localize', ctx=Load()),
                                    args=[Name(id='dt', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dt', ctx=Store())],
                            value=BinOp(
                                left=Name(id='dt', ctx=Load()),
                                op=Add(),
                                right=Name(id='step', ctx=Load()),
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
    type_ignores=[],
)
