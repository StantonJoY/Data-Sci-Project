Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr_work_entry_holidays.tests.common',
            names=[alias(name='TestWorkEntryHolidaysBase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestWorkEntryHolidaysMultiContract',
            bases=[Name(id='TestWorkEntryHolidaysBase', ctx=Load())],
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
                                        args=[],
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
                                    attr='leave_type',
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
                                        slice=Constant(value='hr.leave.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='time_type', kind=None),
                                            Constant(value='requires_allocation', kind=None),
                                            Constant(value='work_entry_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Legal Leaves', kind=None),
                                            Constant(value='leave', kind=None),
                                            Constant(value='no', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='work_entry_type_leave',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_leave',
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
                        Assign(
                            targets=[Name(id='work_days_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='jules_emp',
                                        ctx=Load(),
                                    ),
                                    attr='_get_work_days_data_batch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='holiday_status_id', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='date_to', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Doctor Appointment', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='jules_emp',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='leave_type',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='start', ctx=Load()),
                                            Name(id='end', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='work_days_data', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules_emp',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='days', kind=None),
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
                    name='test_multi_contract_holiday',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2015, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2015, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=18, kind=None),
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
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_approve',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-01', kind=None),
                                    Constant(value='%Y-%m-%d', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_generate', ctx=Store())],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2015, kind=None),
                                    Constant(value=11, kind=None),
                                    Constant(value=30, kind=None),
                                    Constant(value=23, kind=None),
                                    Constant(value=59, kind=None),
                                    Constant(value=59, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='work_entries', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='jules_emp',
                                            ctx=Load(),
                                        ),
                                        attr='contract_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_generate_work_entries',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end_generate', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='work_entries', ctx=Load()),
                                    attr='action_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='work_entries', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='work_entries', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='we', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='we', ctx=Load()),
                                                attr='contract_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='contract_cdi',
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
                        Assign(
                            targets=[Name(id='work', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='work_entries', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='work_entry_type_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
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
                                                    args=[Constant(value='hr_work_entry.work_entry_type_attendance', kind=None)],
                                                    keywords=[],
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
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='work_entries', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='work_entry_type_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='work_entry_type_leave',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='work', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='duration', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=49, kind=None),
                                    Constant(value='It should be 49 hours of work this month for this contract', kind=None),
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
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='leave', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='duration', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=28, kind=None),
                                    Constant(value='It should be 28 hours of leave this month for this contract', kind=None),
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
                    name='test_move_contract_in_leave',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-05 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-12-15 18:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='contract_cdi',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='date_start', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='2015-12-30', kind=None),
                                                            Constant(value='%Y-%m-%d', kind=None),
                                                        ],
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_approve',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='contract_cdi',
                                                ctx=Load(),
                                            ),
                                            attr='date_start',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-17', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='test_create_contract_in_leave',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-05 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-12-15 18:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='contract_cdi',
                                        ctx=Load(),
                                    ),
                                    attr='date_start',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-12-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='action_approve',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
                                                slice=Constant(value='hr.contract', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date_start', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='resource_calendar_id', kind=None),
                                                    Constant(value='wage', kind=None),
                                                    Constant(value='employee_id', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='date_generated_from', kind=None),
                                                    Constant(value='date_generated_to', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='datetime', ctx=Load()),
                                                                    attr='strptime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='2015-11-30', kind=None),
                                                                    Constant(value='%Y-%m-%d', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='Contract for Richard', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='calendar_40h',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=5000.0, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='jules_emp',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='open', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='2015-11-30', kind=None),
                                                            Constant(value='%Y-%m-%d', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='strptime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='2015-11-30', kind=None),
                                                            Constant(value='%Y-%m-%d', kind=None),
                                                        ],
                                                        keywords=[],
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
                FunctionDef(
                    name='test_leave_outside_contract',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2014-10-18 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2014-10-20 09:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2014-10-25 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-01-15 18:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='contract_cdi',
                                        ctx=Load(),
                                    ),
                                    attr='date_end',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-30', kind=None),
                                            Constant(value='%Y-%m-%d', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-25 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-12-5 18:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
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
                    name='test_no_leave_overlapping_contracts',
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
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-12 07:00:00', kind=None),
                                            Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                            attr='strptime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='2015-11-17 18:00:00', kind=None),
                                            Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='create_leave',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-04 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-07 09:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-18 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-20 09:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
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
                    name='test_leave_request_next_contracts',
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
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-23 07:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
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
                                    attr='strptime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='2015-11-24 18:00:00', kind=None),
                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_leave',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leave', ctx=Load()),
                                    attr='_compute_number_of_hours_display',
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
                                    Attribute(
                                        value=Name(id='leave', ctx=Load()),
                                        attr='number_of_hours_display',
                                        ctx=Load(),
                                    ),
                                    Constant(value=14, kind=None),
                                    Constant(value='It should count hours according to the future contract.', kind=None),
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
