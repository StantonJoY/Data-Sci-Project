Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='modules', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='pytz',
            names=[
                alias(name='timezone', asname=None),
                alias(name='UTC', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Users',
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
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_systray_get_calendar_event_domain',
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
                            value=Attribute(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='datetime',
                                        ctx=Load(),
                                    ),
                                    attr='utcnow',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='tz', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='start_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='timezone', ctx=Load()),
                                                                args=[Name(id='tz', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='localize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='start_dt', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='astimezone',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='UTC', ctx=Load())],
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
                            orelse=[
                                Assign(
                                    targets=[Name(id='start_date', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='date',
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
                            ],
                        ),
                        Assign(
                            targets=[Name(id='end_dt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='datetime',
                                        ctx=Load(),
                                    ),
                                    attr='combine',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start_date', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        attr='max',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='tz', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='end_dt', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='timezone', ctx=Load()),
                                                        args=[Name(id='tz', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='localize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='end_dt', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='astimezone',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UTC', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Constant(value='|', kind=None),
                                    Constant(value='&', kind=None),
                                    Constant(value='|', kind=None),
                                    List(
                                        elts=[
                                            Constant(value='start', kind=None),
                                            Constant(value='>=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='start_dt', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='stop', kind=None),
                                            Constant(value='>=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='start_dt', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='start', kind=None),
                                            Constant(value='<=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='end_dt', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='&', kind=None),
                                    List(
                                        elts=[
                                            Constant(value='allday', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='start_date', kind=None),
                                            Constant(value='=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='start_date', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='attendee_ids.partner_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='systray_get_activities',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='systray_get_activities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='meetings_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='calendar.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_systray_get_calendar_event_domain',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='attendee_status', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='meetings_lines', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='line', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='line', ctx=Store()),
                                        iter=Name(id='meetings_lines', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='line', ctx=Load()),
                                                    slice=Constant(value='attendee_status', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='declined', kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='meetings_lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='meeting_label', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value="Today's Meetings", kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='meetings_systray', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='icon', kind=None),
                                            Constant(value='meetings', kind=None),
                                        ],
                                        values=[
                                            Constant(value='meeting', kind=None),
                                            Name(id='meeting_label', ctx=Load()),
                                            Constant(value='calendar.event', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='modules', ctx=Load()),
                                                        attr='module',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_module_icon',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='calendar.event', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='_original_module',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='meetings_lines', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Name(id='meetings_systray', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
