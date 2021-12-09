Module(
    body=[
        ImportFrom(
            module='odoo.fields',
            names=[
                alias(name='Datetime', asname=None),
                alias(name='Date', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.hr_contract.tests.common',
            names=[alias(name='TestContractCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestContractCalendars',
            bases=[Name(id='TestContractCommon', ctx=Load())],
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
                                            Name(id='TestContractCalendars', ctx=Load()),
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
                                    attr='calendar_richard',
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
                                        values=[Constant(value='Calendar of Richard', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='employee',
                                        ctx=Load(),
                                    ),
                                    attr='resource_calendar_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='calendar_richard',
                                ctx=Load(),
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='35h calendar', kind=None)],
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
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Date', ctx=Load()),
                                                    attr='to_date',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2015-11-15', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='Date', ctx=Load()),
                                                    attr='to_date',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='2015-01-01', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='First CDD Contract for Richard', kind=None),
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
                                                    attr='employee',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='close', kind=None),
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
                    name='test_contract_state_incoming_to_open',
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='employee',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_richard',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='contract_cdd',
                                        ctx=Load(),
                                    ),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='open', kind=None),
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
                                            attr='employee',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='contract_cdd',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The employee should have the calendar of its contract.', kind=None),
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
                    name='test_contract_transfer_leaves',
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
                            name='create_calendar_leave',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='start', annotation=None, type_comment=None),
                                    arg(arg='end', annotation=None, type_comment=None),
                                    arg(arg='resource', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[Constant(value=None, kind=None)],
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
                                                    Constant(value='date_from', kind=None),
                                                    Constant(value='date_to', kind=None),
                                                    Constant(value='resource_id', kind=None),
                                                    Constant(value='calendar_id', kind=None),
                                                    Constant(value='time_type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='leave name', kind=None),
                                                    Name(id='start', ctx=Load()),
                                                    Name(id='end', ctx=Load()),
                                                    IfExp(
                                                        test=Name(id='resource', ctx=Load()),
                                                        body=Attribute(
                                                            value=Name(id='resource', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=None, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='employee',
                                                                ctx=Load(),
                                                            ),
                                                            attr='resource_calendar_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='leave', kind=None),
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
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_datetime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2015-11-17 07:00:00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_datetime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2015-11-20 18:00:00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave1', ctx=Store())],
                            value=Call(
                                func=Name(id='create_calendar_leave', ctx=Load()),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='resource',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='employee',
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
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_datetime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2015-11-25 07:00:00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_datetime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2015-11-28 18:00:00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave2', ctx=Store())],
                            value=Call(
                                func=Name(id='create_calendar_leave', ctx=Load()),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='resource',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='employee',
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
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_datetime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2015-11-25 07:00:00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Datetime', ctx=Load()),
                                    attr='to_datetime',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='2015-11-28 18:00:00', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leave3', ctx=Store())],
                            value=Call(
                                func=Name(id='create_calendar_leave', ctx=Load()),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_richard',
                                        ctx=Load(),
                                    ),
                                    attr='transfer_leaves_to',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_35h',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='resources',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='employee',
                                                ctx=Load(),
                                            ),
                                            attr='resource_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='from_date',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Date', ctx=Load()),
                                                attr='to_date',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='2015-11-21', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
                                        value=Name(id='leave1', ctx=Load()),
                                        attr='calendar_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_richard',
                                        ctx=Load(),
                                    ),
                                    Constant(value="It should stay in Richard's calendar", kind=None),
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
                                        value=Name(id='leave3', ctx=Load()),
                                        attr='calendar_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_richard',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Global leave should stay in original calendar', kind=None),
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
                                        value=Name(id='leave2', ctx=Load()),
                                        attr='calendar_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_35h',
                                        ctx=Load(),
                                    ),
                                    Constant(value='It should be transfered to the other calendar', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_richard',
                                        ctx=Load(),
                                    ),
                                    attr='transfer_leaves_to',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_35h',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='resources',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='from_date',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='Date', ctx=Load()),
                                                attr='to_date',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='2015-11-21', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
                                        value=Name(id='leave3', ctx=Load()),
                                        attr='calendar_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_35h',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Global leave should be transfered', kind=None),
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
