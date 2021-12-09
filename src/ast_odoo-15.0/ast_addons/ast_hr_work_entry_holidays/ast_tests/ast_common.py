Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr_work_entry_contract.tests.common',
            names=[alias(name='TestWorkEntryBase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestWorkEntryHolidaysBase',
            bases=[Name(id='TestWorkEntryBase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='TestWorkEntryHolidaysBase', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='leave_type',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
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
                                                    value=Name(id='cls', ctx=Load()),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='jules_emp',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='hr.employee', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='gender', kind=None),
                                            Constant(value='birthday', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='department_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jules', kind=None),
                                            Constant(value='male', kind=None),
                                            Constant(value='1984-05-01', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.be', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='dep_rd',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='calendar_35h',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attendance_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='35h calendar', kind=None),
                                            List(
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
                                                                    Constant(value='Monday Morning', kind=None),
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
                                                                    Constant(value='Monday Evening', kind=None),
                                                                    Constant(value='0', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=16, kind=None),
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
                                                                    Constant(value='Tuesday Morning', kind=None),
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
                                                                    Constant(value='Tuesday Evening', kind=None),
                                                                    Constant(value='1', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=16, kind=None),
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
                                                                    Constant(value='Wednesday Morning', kind=None),
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
                                                                    Constant(value='Wednesday Evening', kind=None),
                                                                    Constant(value='2', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=16, kind=None),
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
                                                                    Constant(value='Thursday Morning', kind=None),
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
                                                                    Constant(value='Thursday Evening', kind=None),
                                                                    Constant(value='3', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=16, kind=None),
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
                                                                    Constant(value='Friday Morning', kind=None),
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
                                                                    Constant(value='Friday Evening', kind=None),
                                                                    Constant(value='4', kind=None),
                                                                    Constant(value=13, kind=None),
                                                                    Constant(value=16, kind=None),
                                                                    Constant(value='afternoon', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='calendar_35h',
                                        ctx=Load(),
                                    ),
                                    attr='_onchange_hours_per_day',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='calendar_40h',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Default calendar', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='contract_cdd',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
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
                                            Constant(value='date_end', kind=None),
                                            Constant(value='date_start', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_calendar_id', kind=None),
                                            Constant(value='wage', kind=None),
                                            Constant(value='employee_id', kind=None),
                                            Constant(value='state', kind=None),
                                            Constant(value='kanban_state', kind=None),
                                            Constant(value='date_generated_from', kind=None),
                                            Constant(value='date_generated_to', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-15', kind=None),
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
                                                    Constant(value='2015-01-01', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='First CDD Contract for Jules', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='calendar_40h',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5000.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='jules_emp',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='open', kind=None),
                                            Constant(value='blocked', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-16', kind=None),
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
                                                    Constant(value='2015-11-16', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='contract_cdi',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
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
                                            Constant(value='kanban_state', kind=None),
                                            Constant(value='date_generated_from', kind=None),
                                            Constant(value='date_generated_to', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-16', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='Contract for Jules', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='calendar_35h',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5000.0, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='jules_emp',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='open', kind=None),
                                            Constant(value='normal', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2015-11-15', kind=None),
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
                                                    Constant(value='2015-11-15', kind=None),
                                                    Constant(value='%Y-%m-%d', kind=None),
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
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create_leave',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='date_from', annotation=None, type_comment=None),
                            arg(arg='date_to', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_from', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='date_from', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Datetime', ctx=Load()),
                                            attr='today',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_to', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='date_to', ctx=Load()),
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='Datetime', ctx=Load()),
                                                attr='today',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
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
                                            Constant(value='date_to', kind=None),
                                            Constant(value='date_from', kind=None),
                                            Constant(value='number_of_days', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Holiday !!!', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='richard_emp',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='leave_type',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='date_to', ctx=Load()),
                                            Name(id='date_from', ctx=Load()),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
