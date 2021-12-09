Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='resource.calendar.leaves', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='timesheet_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='account.analytic.line', kind=None),
                            Constant(value='global_leave_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic Lines', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_work_time_per_day',
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
                            value=Constant(value=' Get work time per day based on the calendar and its attendances\n\n            1) Gets all calendars with their characteristics (i.e.\n                (a) the leaves in it,\n                (b) the resources which have a leave,\n                (c) the oldest and\n                (d) the latest leave dates\n               ) for leaves in self.\n            2) Search the attendances based on the characteristics retrieved for each calendar.\n                The attendances found are the ones between the date_from of the oldest leave\n                and the date_to of the most recent leave.\n            3) Create a dict as result of this method containing:\n                {\n                    leave: {\n                            max(date_start of work hours, date_start of the leave):\n                                the duration in days of the work including the leave\n                    }\n                }\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='leaves_read_group', ctx=Store())],
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
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='calendar_id', kind=None),
                                            Constant(value='ids:array_agg(id)', kind=None),
                                            Constant(value='resource_ids:array_agg(resource_id)', kind=None),
                                            Constant(value='min_date_from:min(date_from)', kind=None),
                                            Constant(value='max_date_to:max(date_to)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='calendar_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cal_attendance_intervals_dict', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='calendar_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Dict(
                                    keys=[
                                        Constant(value='date_from', kind=None),
                                        Constant(value='date_to', kind=None),
                                        Constant(value='resources', kind=None),
                                        Constant(value='leaves', kind=None),
                                    ],
                                    values=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='utc', ctx=Load()),
                                                attr='localize',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='min_date_from', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='utc', ctx=Load()),
                                                attr='localize',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='max_date_to', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='resource.resource', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                IfExp(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Constant(value='resource_ids', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    slice=Constant(value='resource_ids', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='resource_ids', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    orelse=List(elts=[], ctx=Load()),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        Call(
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
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='ids', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='res', ctx=Store()),
                                        iter=Name(id='leaves_read_group', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendars_dict', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='calendar', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Name(id='calendar', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='calendar', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='calendar_id',
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
                            targets=[Name(id='results', ctx=Store())],
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
                            target=Tuple(
                                elts=[
                                    Name(id='calendar_id', ctx=Store()),
                                    Name(id='cal_attendance_intervals_params_entry', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='cal_attendance_intervals_dict', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='calendar', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='calendars_dict', ctx=Load()),
                                        slice=Name(id='calendar_id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='work_hours_intervals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='_attendance_intervals_batch',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='cal_attendance_intervals_params_entry', ctx=Load()),
                                                slice=Constant(value='date_from', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='cal_attendance_intervals_params_entry', ctx=Load()),
                                                slice=Constant(value='date_to', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='cal_attendance_intervals_params_entry', ctx=Load()),
                                                slice=Constant(value='resources', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Call(
                                                    func=Name(id='timezone', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='calendar', ctx=Load()),
                                                            attr='tz',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='leave', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='cal_attendance_intervals_params_entry', ctx=Load()),
                                        slice=Constant(value='leaves', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='work_hours_data', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='work_hours_intervals', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='leave', ctx=Load()),
                                                        attr='resource_id',
                                                        ctx=Load(),
                                                    ),
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
                                                    Name(id='date_from', ctx=Store()),
                                                    Name(id='date_to', ctx=Store()),
                                                    Name(id='dummy', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Name(id='work_hours_data', ctx=Load()),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='date_to', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='utc', ctx=Load()),
                                                                            attr='localize',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='leave', ctx=Load()),
                                                                                attr='date_from',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Name(id='date_from', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='utc', ctx=Load()),
                                                                            attr='localize',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='leave', ctx=Load()),
                                                                                attr='date_to',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='tmp_start', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='max', ctx=Load()),
                                                                args=[
                                                                    Name(id='date_from', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='utc', ctx=Load()),
                                                                            attr='localize',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='leave', ctx=Load()),
                                                                                attr='date_from',
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
                                                            targets=[Name(id='tmp_end', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='min', ctx=Load()),
                                                                args=[
                                                                    Name(id='date_to', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='utc', ctx=Load()),
                                                                            attr='localize',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='leave', ctx=Load()),
                                                                                attr='date_to',
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
                                                        AugAssign(
                                                            target=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='results', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='leave', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='tmp_start', ctx=Load()),
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
                                                                            left=Name(id='tmp_end', ctx=Load()),
                                                                            op=Sub(),
                                                                            right=Name(id='tmp_start', ctx=Load()),
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
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='results', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='leave', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='results', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='leave', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='items',
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_create_lines',
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
                            value=Constant(value=' Create timesheet leaves for each employee using the same calendar containing in self.calendar_id\n\n            If the employee has already a time off in the same day then no timesheet should be created.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='work_hours_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_work_time_per_day',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employees_groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='resource_calendar_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='calendar_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='resource_calendar_id', kind=None),
                                            Constant(value='ids:array_agg(id)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='resource_calendar_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_employee', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='employee', ctx=Load()),
                                        slice=Constant(value='resource_calendar_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='hr.employee', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Subscript(
                                            value=Name(id='employee', ctx=Load()),
                                            slice=Constant(value='ids', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='employee', ctx=Store()),
                                        iter=Name(id='employees_groups', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='employee_ids_set', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='employee_ids_set', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=ListComp(
                                            elt=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='line', ctx=Store()),
                                                    iter=Name(id='employees_groups', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Name(id='min_date', ctx=Store()),
                                Name(id='max_date', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='work_hours_data', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='d', ctx=Store()),
                                            Name(id='dummy', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='values', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='min_date', ctx=Load()),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='max_date', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='min_date', ctx=Store()),
                                                        Name(id='max_date', ctx=Store()),
                                                    ],
                                                    value=Name(id='d', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='d', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Name(id='min_date', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='min_date', ctx=Store())],
                                                            value=Name(id='d', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='d', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='max_date', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='max_date', ctx=Store())],
                                                                    value=Name(id='d', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='holidays_read_group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.leave', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='employee_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='employee_ids_set', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='max_date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='min_date', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='cancel', kind=None),
                                                            Constant(value='refuse', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='date_from_list:array_agg(date_from)', kind=None),
                                            Constant(value='date_to_list:array_agg(date_to)', kind=None),
                                            Constant(value='employee_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='employee_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='holidays_by_employee', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='line', ctx=Load()),
                                        slice=Constant(value='employee_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=ListComp(
                                    elt=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='date_from', ctx=Load()),
                                                    attr='date',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='date_to', ctx=Load()),
                                                    attr='date',
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
                                            target=Tuple(
                                                elts=[
                                                    Name(id='date_from', ctx=Store()),
                                                    Name(id='date_to', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='zip', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Constant(value='date_from_list', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Constant(value='date_to_list', kind=None),
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
                                generators=[
                                    comprehension(
                                        target=Name(id='line', ctx=Store()),
                                        iter=Name(id='holidays_read_group', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='leave', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='employee', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='mapped_employee', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='leave', ctx=Load()),
                                                    attr='calendar_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='hr.employee', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='holidays', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='holidays_by_employee', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='employee', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='work_hours_list', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='work_hours_data', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='leave', ctx=Load()),
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
                                                    Name(id='index', ctx=Store()),
                                                    Tuple(
                                                        elts=[
                                                            Name(id='day_date', ctx=Store()),
                                                            Name(id='work_hours_count', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='enumerate', ctx=Load()),
                                                args=[Name(id='work_hours_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='holidays', ctx=Load()),
                                                            ),
                                                            Call(
                                                                func=Name(id='all', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=UnaryOp(
                                                                            op=Not(),
                                                                            operand=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Name(id='date_from', ctx=Load()),
                                                                                        ops=[LtE()],
                                                                                        comparators=[Name(id='day_date', ctx=Load())],
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Name(id='date_to', ctx=Load()),
                                                                                        ops=[GtE()],
                                                                                        comparators=[Name(id='day_date', ctx=Load())],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Tuple(
                                                                                    elts=[
                                                                                        Name(id='date_from', ctx=Store()),
                                                                                        Name(id='date_to', ctx=Store()),
                                                                                    ],
                                                                                    ctx=Store(),
                                                                                ),
                                                                                iter=Name(id='holidays', ctx=Load()),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='vals_list', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='leave', ctx=Load()),
                                                                            attr='_timesheet_prepare_line_values',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='index', ctx=Load()),
                                                                            Name(id='employee', ctx=Load()),
                                                                            Name(id='work_hours_list', ctx=Load()),
                                                                            Name(id='day_date', ctx=Load()),
                                                                            Name(id='work_hours_count', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.analytic.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_timesheet_prepare_line_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='index', annotation=None, type_comment=None),
                            arg(arg='employee_id', annotation=None, type_comment=None),
                            arg(arg='work_hours_data', annotation=None, type_comment=None),
                            arg(arg='day_date', annotation=None, type_comment=None),
                            arg(arg='work_hours_count', annotation=None, type_comment=None),
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='project_id', kind=None),
                                    Constant(value='task_id', kind=None),
                                    Constant(value='account_id', kind=None),
                                    Constant(value='unit_amount', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='global_leave_id', kind=None),
                                    Constant(value='employee_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='Time Off (%s/%s)', kind=None),
                                            BinOp(
                                                left=Name(id='index', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='work_hours_data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='employee_id', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='internal_project_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='employee_id', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            attr='leave_timesheet_task_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='employee_id', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='internal_project_id',
                                                ctx=Load(),
                                            ),
                                            attr='analytic_account_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='work_hours_count', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='employee_id', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='day_date', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='employee_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='employee_id', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceCalendarLeaves', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results_with_leave_timesheet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='results', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
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
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='resource_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='calendar_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='internal_project_id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='calendar_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='leave_timesheet_task_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='results_with_leave_timesheet', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='results_with_leave_timesheet', ctx=Load()),
                                            attr='_timesheet_create_lines',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='results', ctx=Load()),
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='start_dates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='date_from', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_dates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='date_to', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceCalendarLeaves', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='date_from', ctx=Store()),
                                        Name(id='date_to', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='date_from', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='date_to', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='date_from', ctx=Load()),
                                    Name(id='date_to', ctx=Load()),
                                ],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='start_date', ctx=Load()),
                                                            ops=[NotEq()],
                                                            comparators=[Name(id='date_from', ctx=Load())],
                                                        ),
                                                        Compare(
                                                            left=Name(id='end_date', ctx=Load()),
                                                            ops=[NotEq()],
                                                            comparators=[Name(id='date_to', ctx=Load())],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='start_date', ctx=Store()),
                                                                Name(id='end_date', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Name(id='zip', ctx=Load()),
                                                            args=[
                                                                Name(id='start_dates', ctx=Load()),
                                                                Name(id='end_dates', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='timesheets', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='timesheet_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='timesheets', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='timesheets', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='global_leave_id', kind=None)],
                                                                values=[Constant(value=False, kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='timesheets', ctx=Load()),
                                                            attr='unlink',
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
                                                            attr='_timesheet_create_lines',
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
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
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
