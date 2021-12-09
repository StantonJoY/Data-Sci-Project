Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
                alias(name='time', asname=None),
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
            module='odoo.addons.mrp.tests.common',
            names=[alias(name='TestMrpCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestOee',
            bases=[Name(id='TestMrpCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='create_productivity_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='loss_reason', annotation=None, type_comment=None),
                            arg(arg='date_start', annotation=None, type_comment=None),
                            arg(arg='date_end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.workcenter.productivity', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='workcenter_id', kind=None),
                                            Constant(value='date_start', kind=None),
                                            Constant(value='date_end', kind=None),
                                            Constant(value='loss_id', kind=None),
                                            Constant(value='description', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='workcenter_1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_start', ctx=Load()),
                                            Name(id='date_end', ctx=Load()),
                                            Attribute(
                                                value=Name(id='loss_reason', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='loss_reason', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
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
                    name='test_wrokcenter_oee',
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
                            value=Constant(value='  Test case workcenter oee. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='day', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='today',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='day', ctx=Load()),
                                        attr='weekday',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=5, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='day', ctx=Store()),
                                    op=Sub(),
                                    value=Call(
                                        func=Name(id='timedelta', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='tz', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='workcenter_1',
                                                ctx=Load(),
                                            ),
                                            attr='resource_calendar_id',
                                            ctx=Load(),
                                        ),
                                        attr='tz',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='time_to_string_utc_datetime',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='time', annotation=None, type_comment=None)],
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
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tz', ctx=Load()),
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
                                                                    Name(id='day', ctx=Load()),
                                                                    Name(id='time', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
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
                        Assign(
                            targets=[Name(id='start_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=43, kind=None),
                                            Constant(value=22, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=56, kind=None),
                                            Constant(value=22, kind=None),
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
                                    attr='create_productivity_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mrp.block_reason7', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='start_time', ctx=Load()),
                                    Name(id='end_time', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=47, kind=None),
                                            Constant(value=8, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='workcenter_productivity_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_productivity_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mrp.block_reason0', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='start_time', ctx=Load()),
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='workcenter_1',
                                            ctx=Load(),
                                        ),
                                        attr='working_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='blocked', kind=None),
                                    Constant(value='Wrong working state of workcenter.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='end_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=48, kind=None),
                                            Constant(value=39, kind=None),
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
                                    value=Name(id='workcenter_productivity_1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='date_end', kind=None)],
                                        values=[Name(id='end_time', ctx=Load())],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='workcenter_1',
                                            ctx=Load(),
                                        ),
                                        attr='working_state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='normal', kind=None),
                                    Constant(value='Wrong working state of workcenter.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=48, kind=None),
                                            Constant(value=38, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=49, kind=None),
                                            Constant(value=58, kind=None),
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
                                    attr='create_productivity_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mrp.block_reason5', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='start_time', ctx=Load()),
                                    Name(id='end_time', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=50, kind=None),
                                            Constant(value=22, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_time', ctx=Store())],
                            value=Call(
                                func=Name(id='time_to_string_utc_datetime', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='time', ctx=Load()),
                                        args=[
                                            Constant(value=10, kind=None),
                                            Constant(value=53, kind=None),
                                            Constant(value=22, kind=None),
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
                                    attr='create_productivity_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mrp.block_reason4', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='start_time', ctx=Load()),
                                    Name(id='end_time', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='blocked_time_in_hour', ctx=Store())],
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Constant(value=1.33, kind=None),
                                                op=Add(),
                                                right=Constant(value=3.0, kind=None),
                                            ),
                                            op=Add(),
                                            right=Constant(value=1.52, kind=None),
                                        ),
                                        op=Div(),
                                        right=Constant(value=60.0, kind=None),
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='productive_time_in_hour', ctx=Store())],
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=13.0, kind=None),
                                        op=Div(),
                                        right=Constant(value=60.0, kind=None),
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='workcenter_1',
                                            ctx=Load(),
                                        ),
                                        attr='blocked_time',
                                        ctx=Load(),
                                    ),
                                    Name(id='blocked_time_in_hour', ctx=Load()),
                                    Constant(value='Wrong block time on workcenter.', kind=None),
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
                                            attr='workcenter_1',
                                            ctx=Load(),
                                        ),
                                        attr='productive_time',
                                        ctx=Load(),
                                    ),
                                    Name(id='productive_time_in_hour', ctx=Load()),
                                    Constant(value='Wrong productive time on workcenter.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='computed_oee', ctx=Store())],
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='productive_time_in_hour', ctx=Load()),
                                            op=Mult(),
                                            right=Constant(value=100.0, kind=None),
                                        ),
                                        op=Div(),
                                        right=BinOp(
                                            left=Name(id='productive_time_in_hour', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='blocked_time_in_hour', ctx=Load()),
                                        ),
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='workcenter_1',
                                            ctx=Load(),
                                        ),
                                        attr='oee',
                                        ctx=Load(),
                                    ),
                                    Name(id='computed_oee', ctx=Load()),
                                    Constant(value='Wrong oee on workcenter.', kind=None),
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
