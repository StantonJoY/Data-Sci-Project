Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='plaintext2html', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='calendar.alarm_manager', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Event Alarm Manager', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_next_potential_limit_alarm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='alarm_type', annotation=None, type_comment=None),
                            arg(arg='seconds', annotation=None, type_comment=None),
                            arg(arg='partners', annotation=None, type_comment=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='delta_request', ctx=Store())],
                            value=Constant(value='\n            SELECT\n                rel.calendar_event_id, max(alarm.duration_minutes) AS max_delta,min(alarm.duration_minutes) AS min_delta\n            FROM\n                calendar_alarm_calendar_event_rel AS rel\n            LEFT JOIN calendar_alarm AS alarm ON alarm.id = rel.calendar_alarm_id\n            WHERE alarm.alarm_type = %s\n            GROUP BY rel.calendar_event_id\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_request', ctx=Store())],
                            value=Constant(value="\n                    SELECT\n                        cal.id,\n                        cal.start - interval '1' minute  * calcul_delta.max_delta AS first_alarm,\n                        CASE\n                            WHEN cal.recurrency THEN rrule.until - interval '1' minute  * calcul_delta.min_delta\n                            ELSE cal.stop - interval '1' minute  * calcul_delta.min_delta\n                        END as last_alarm,\n                        cal.start as first_event_date,\n                        CASE\n                            WHEN cal.recurrency THEN rrule.until\n                            ELSE cal.stop\n                        END as last_event_date,\n                        calcul_delta.min_delta,\n                        calcul_delta.max_delta,\n                        rrule.rrule AS rule\n                    FROM\n                        calendar_event AS cal\n                    RIGHT JOIN calcul_delta ON calcul_delta.calendar_event_id = cal.id\n                    LEFT JOIN calendar_recurrence as rrule ON rrule.id = cal.recurrence_id\n             ", kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filter_user', ctx=Store())],
                            value=Constant(value='\n                RIGHT JOIN calendar_event_res_partner_rel AS part_rel ON part_rel.calendar_event_id = cal.id\n                    AND part_rel.res_partner_id IN %s\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tuple_params', ctx=Store())],
                            value=Tuple(
                                elts=[Name(id='alarm_type', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partners', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='base_request', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='filter_user', ctx=Load()),
                                ),
                                AugAssign(
                                    target=Name(id='tuple_params', ctx=Store()),
                                    op=Add(),
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='partners', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='first_alarm_max_value', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='seconds', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='first_alarm_max_value', ctx=Store())],
                                    value=Constant(value="\n                COALESCE((SELECT MIN(cal.start - interval '1' minute  * calcul_delta.max_delta)\n                FROM calendar_event cal\n                RIGHT JOIN calcul_delta ON calcul_delta.calendar_event_id = cal.id\n                WHERE cal.start - interval '1' minute  * calcul_delta.max_delta > now() at time zone 'utc'\n            ) + interval '3' minute, now() at time zone 'utc')", kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='first_alarm_max_value', ctx=Store())],
                                    value=Constant(value="(now() at time zone 'utc' + interval '%s' second )", kind=None),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='tuple_params', ctx=Store()),
                                    op=Add(),
                                    value=Tuple(
                                        elts=[Name(id='seconds', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value="\n            WITH calcul_delta AS (%s)\n            SELECT *\n                FROM ( %s WHERE cal.active = True ) AS ALL_EVENTS\n               WHERE ALL_EVENTS.first_alarm < %s\n                 AND ALL_EVENTS.last_event_date > (now() at time zone 'utc')\n        ", kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='delta_request', ctx=Load()),
                                                Name(id='base_request', ctx=Load()),
                                                Name(id='first_alarm_max_value', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    Name(id='tuple_params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='event_id', ctx=Store()),
                                    Name(id='first_alarm', ctx=Store()),
                                    Name(id='last_alarm', ctx=Store()),
                                    Name(id='first_meeting', ctx=Store()),
                                    Name(id='last_meeting', ctx=Store()),
                                    Name(id='min_duration', ctx=Store()),
                                    Name(id='max_duration', ctx=Store()),
                                    Name(id='rule', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Name(id='event_id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='event_id', kind=None),
                                            Constant(value='first_alarm', kind=None),
                                            Constant(value='last_alarm', kind=None),
                                            Constant(value='first_meeting', kind=None),
                                            Constant(value='last_meeting', kind=None),
                                            Constant(value='min_duration', kind=None),
                                            Constant(value='max_duration', kind=None),
                                            Constant(value='rrule', kind=None),
                                        ],
                                        values=[
                                            Name(id='event_id', ctx=Load()),
                                            Name(id='first_alarm', ctx=Load()),
                                            Name(id='last_alarm', ctx=Load()),
                                            Name(id='first_meeting', ctx=Load()),
                                            Name(id='last_meeting', ctx=Load()),
                                            Name(id='min_duration', ctx=Load()),
                                            Name(id='max_duration', ctx=Load()),
                                            Name(id='rule', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                                args=[Name(id='result', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=DictComp(
                                key=Name(id='key', ctx=Load()),
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='key', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='events', ctx=Load()),
                                                            attr='_filter_access_rules',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='read', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='ids',
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
                    name='do_check_alarm_for_one_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='one_date', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='event_maxdelta', annotation=None, type_comment=None),
                            arg(arg='in_the_next_X_seconds', annotation=None, type_comment=None),
                            arg(arg='alarm_type', annotation=None, type_comment=None),
                            arg(arg='after', annotation=None, type_comment=None),
                            arg(arg='missing', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value=' Search for some alarms in the interval of time determined by some parameters (after, in_the_next_X_seconds, ...)\n            :param one_date: date of the event to check (not the same that in the event browse if recurrent)\n            :param event: Event browse record\n            :param event_maxdelta: biggest duration from alarms for this event\n            :param in_the_next_X_seconds: looking in the future (in seconds)\n            :param after: if not False: will return alert if after this date (date as string - todo: change in master)\n            :param missing: if not False: will return alert even if we are too late\n            :param notif: Looking for type notification\n            :param mail: looking for type email\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='past', ctx=Store())],
                            value=BinOp(
                                left=Name(id='one_date', ctx=Load()),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='minutes',
                                            value=BinOp(
                                                left=Name(id='missing', ctx=Load()),
                                                op=Mult(),
                                                right=Name(id='event_maxdelta', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='future', ctx=Store())],
                            value=BinOp(
                                left=Call(
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
                                op=Add(),
                                right=Call(
                                    func=Name(id='timedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='seconds',
                                            value=Name(id='in_the_next_X_seconds', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='future', ctx=Load()),
                                ops=[LtE()],
                                comparators=[Name(id='past', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Name(id='result', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='alarm', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='event', ctx=Load()),
                                attr='alarm_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='alarm', ctx=Load()),
                                            attr='alarm_type',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='alarm_type', ctx=Load())],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='past', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='one_date', ctx=Load()),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='minutes',
                                                    value=BinOp(
                                                        left=Name(id='missing', ctx=Load()),
                                                        op=Mult(),
                                                        right=Attribute(
                                                            value=Name(id='alarm', ctx=Load()),
                                                            attr='duration_minutes',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='future', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Name(id='past', ctx=Load())],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='after', ctx=Load()),
                                            Compare(
                                                left=Name(id='past', ctx=Load()),
                                                ops=[LtE()],
                                                comparators=[
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
                                                        args=[Name(id='after', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='alarm_id', kind=None),
                                                    Constant(value='event_id', kind=None),
                                                    Constant(value='notify_at', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='alarm', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Name(id='one_date', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='timedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='minutes',
                                                                    value=Attribute(
                                                                        value=Name(id='alarm', ctx=Load()),
                                                                        attr='duration_minutes',
                                                                        ctx=Load(),
                                                                    ),
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_events_by_alarm_to_notify',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='alarm_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Get the events with an alarm of the given type between the cron\n        last call and now.\n\n        Please note that all new reminders created since the cron last\n        call with an alarm prior to the cron last call are skipped by\n        design. The attendees receive an invitation for any new event\n        already.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n            SELECT "alarm"."id", "event"."id"\n              FROM "calendar_event" AS "event"\n              JOIN "calendar_alarm_calendar_event_rel" AS "event_alarm_rel"\n                ON "event"."id" = "event_alarm_rel"."calendar_event_id"\n              JOIN "calendar_alarm" AS "alarm"\n                ON "event_alarm_rel"."calendar_alarm_id" = "alarm"."id"\n             WHERE (\n                   "alarm"."alarm_type" = %s\n               AND "event"."active"\n               AND "event"."start" - CAST("alarm"."duration" || \' \' || "alarm"."interval" AS Interval) >= %s\n               AND "event"."start" - CAST("alarm"."duration" || \' \' || "alarm"."interval" AS Interval) < now() at time zone \'utc\'\n             )', kind=None),
                                    List(
                                        elts=[
                                            Name(id='alarm_type', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='lastcall', kind=None),
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
                            targets=[Name(id='events_by_alarm', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='alarm_id', ctx=Store()),
                                    Name(id='event_id', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='fetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='events_by_alarm', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='alarm_id', ctx=Load()),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='event_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='events_by_alarm', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
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
                        Assign(
                            targets=[Name(id='events_by_alarm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_events_by_alarm_to_notify',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='email', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='events_by_alarm', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='event_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='event_id', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='event_ids', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='events_by_alarm', ctx=Load()),
                                                                attr='values',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                    comprehension(
                                                        target=Name(id='event_id', ctx=Store()),
                                                        iter=Name(id='event_ids', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                args=[Name(id='event_ids', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='alarms', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='calendar.alarm', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='events_by_alarm', ctx=Load()),
                                            attr='keys',
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
                        For(
                            target=Name(id='alarm', ctx=Store()),
                            iter=Name(id='alarms', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='alarm_attendees', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attendees', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='attendee', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='attendee', ctx=Load()),
                                                            attr='event_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='events_by_alarm', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='alarm', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='alarm_attendees', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_notify_force_send',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='calendar_template_ignore_recurrence',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='_send_mail_to_attendees',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='alarm', ctx=Load()),
                                                attr='mail_template_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='force_send',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
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
                FunctionDef(
                    name='get_next_notif',
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
                            targets=[Name(id='partner', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_notif', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='partner', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='all_meetings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_next_potential_limit_alarm',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='notification', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='partners',
                                        value=Name(id='partner', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='time_limit', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=3600, kind=None),
                                op=Mult(),
                                right=Constant(value=24, kind=None),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='event_id', ctx=Store()),
                            iter=Name(id='all_meetings', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='max_delta', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='all_meetings', ctx=Load()),
                                            slice=Name(id='event_id', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='max_duration', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='meeting', ctx=Store())],
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
                                        args=[Name(id='event_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='in_date_format', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='meeting', ctx=Load()),
                                                attr='start',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='last_found', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='do_check_alarm_for_one_date',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='in_date_format', ctx=Load()),
                                            Name(id='meeting', ctx=Load()),
                                            Name(id='max_delta', ctx=Load()),
                                            Name(id='time_limit', ctx=Load()),
                                            Constant(value='notification', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='after',
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='calendar_last_notif_ack',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='last_found', ctx=Load()),
                                    body=[
                                        For(
                                            target=Name(id='alert', ctx=Store()),
                                            iter=Name(id='last_found', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='all_notif', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='do_notif_reminder',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='alert', ctx=Load())],
                                                                keywords=[],
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='all_notif', ctx=Load()),
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
                    name='do_notif_reminder',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='alert', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='alarm', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='calendar.alarm', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='alert', ctx=Load()),
                                        slice=Constant(value='alarm_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='meeting', ctx=Store())],
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
                                    Subscript(
                                        value=Name(id='alert', ctx=Load()),
                                        slice=Constant(value='event_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='alarm', ctx=Load()),
                                    attr='alarm_type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='notification', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='meeting', ctx=Load()),
                                        attr='display_time',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='alarm', ctx=Load()),
                                        attr='body',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='message', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='<p>%s</p>', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='plaintext2html', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='alarm', ctx=Load()),
                                                            attr='body',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='alert', ctx=Load()),
                                            slice=Constant(value='notify_at', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Call(
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
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='delta', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='delta', ctx=Load()),
                                            attr='seconds',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='delta', ctx=Load()),
                                                    attr='days',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=3600, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=24, kind=None),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='alarm_id', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='message', kind=None),
                                            Constant(value='timer', kind=None),
                                            Constant(value='notify_at', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='alarm', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='meeting', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='meeting', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='message', ctx=Load()),
                                            Name(id='delta', ctx=Load()),
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
                                                args=[
                                                    Subscript(
                                                        value=Name(id='alert', ctx=Load()),
                                                        slice=Constant(value='notify_at', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
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
                    name='_notify_next_alarm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Sends through the bus the next alarm of given partners ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='notifications', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='users', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[Name(id='partner_ids', ctx=Load())],
                                                        keywords=[],
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
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Name(id='users', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='notif', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_user',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='user', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='allowed_company_ids',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='company_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            attr='get_next_notif',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='notifications', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='calendar.alarm', kind=None),
                                                    Name(id='notif', ctx=Load()),
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
                                    args=[Name(id='notifications', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
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
                                                slice=Constant(value='bus.bus', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_sendmany',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='notifications', ctx=Load())],
                                        keywords=[],
                                    ),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
