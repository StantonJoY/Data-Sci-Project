Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='AlarmManager',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='calendar.alarm_manager', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_reminder',
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
                            value=Constant(value=' Cron method, overridden here to send SMS reminders as well\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_send_reminder',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='alarms_by_event', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_events_by_alarm_to_notify',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='sms', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='alarms_by_event', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='alarms_by_event', ctx=Load()),
                                                    attr='keys',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                            targets=[Name(id='attendees', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='events', ctx=Load()),
                                        attr='attendee_ids',
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
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='declined', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='event_id', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='alarms_by_event', ctx=Load()),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='event_alarms', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='attendees', ctx=Load()),
                                                    attr='event_id',
                                                    ctx=Load(),
                                                ),
                                                attr='alarm_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='alarm', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='alarm', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='alarms_by_event', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='event_id', ctx=Load()),
                                                                List(elts=[], ctx=Load()),
                                                            ],
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
                                For(
                                    target=Name(id='alarm', ctx=Store()),
                                    iter=Name(id='event_alarms', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='events', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='event_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='_do_sms_reminder',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='alarm', ctx=Load())],
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
