Module(
    body=[
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
            module='odoo.addons.microsoft_calendar.utils.microsoft_calendar',
            names=[alias(name='MicrosoftCalendarService', asname=None)],
            level=0,
        ),
        ClassDef(
            name='RecurrenceRule',
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
                    value=Constant(value='calendar.recurrence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='calendar.recurrence', kind=None),
                            Constant(value='microsoft.calendar.sync', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='need_sync_m', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
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
                    targets=[Name(id='microsoft_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Microsoft Calendar Recurrence Id', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_rrule',
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
                            target=Name(id='recurrence', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='rrule',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='_rrule_serialize',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='rrule', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='recurrence', ctx=Load()),
                                                                    attr='_rrule_serialize',
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
                FunctionDef(
                    name='_inverse_rrule',
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
                            target=Name(id='recurrence', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='rrule', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_rrule_parse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='recurrence', ctx=Load()),
                                                attr='rrule',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='recurrence', ctx=Load()),
                                                attr='dtstart',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='need_sync_m', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
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
                    name='_apply_recurrence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='specific_values_creation', annotation=None, type_comment=None),
                            arg(arg='no_send_edit', annotation=None, type_comment=None),
                            arg(arg='generic_values_creation', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='filtered',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='need_sync_m', kind=None)],
                                    keywords=[],
                                ),
                                attr='calendar_event_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='detached_events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='specific_values_creation', ctx=Load()),
                                    Name(id='no_send_edit', ctx=Load()),
                                    Name(id='generic_values_creation', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='microsoft_service', ctx=Store())],
                            value=Call(
                                func=Name(id='MicrosoftCalendarService', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='microsoft.service', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='events', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='microsoft_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='active',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='microsoft_id',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='microsoft_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='vals', ctx=Store()),
                                            op=Add(),
                                            value=List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='microsoft_id', kind=None),
                                                            Constant(value='start', kind=None),
                                                            Constant(value='stop', kind=None),
                                                            Constant(value='active', kind=None),
                                                            Constant(value='need_sync_m', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='microsoft_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='start',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='stop',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='_microsoft_delete',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='microsoft_service', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='microsoft_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='microsoft_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_event_ids',
                                        ctx=Load(),
                                    ),
                                    attr='need_sync_m',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='detached_events', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_write_events',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='dtstart', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='need_sync_m', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[Name(id='dtstart', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_write_events',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='dtstart',
                                        value=Name(id='dtstart', ctx=Load()),
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
                    name='_get_rrule',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dtstart', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='dtstart', ctx=Load()),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dtstart',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dtstart', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dtstart',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_rrule',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dtstart', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_microsoft_synced_fields',
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
                            value=BinOp(
                                left=Set(
                                    elts=[Constant(value='rrule', kind=None)],
                                ),
                                op=BitOr(),
                                right=Call(
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
                                        attr='_get_microsoft_synced_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_restart_microsoft_sync',
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
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='calendar.recurrence', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_microsoft_sync_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='need_sync_m', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                    name='_write_from_microsoft',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='microsoft_event', annotation=None, type_comment=None),
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
                            targets=[Name(id='current_rrule', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='rrule',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='event_tz', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='microsoft_event', ctx=Load()),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='timeZone', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_write_from_microsoft',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='microsoft_event', ctx=Load()),
                                    Name(id='vals', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='base_event_time_fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='start', kind=None),
                                    Constant(value='stop', kind=None),
                                    Constant(value='allday', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_event_values', ctx=Store())],
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
                                    attr='_microsoft_to_odoo_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='microsoft_event', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='old_event_values', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='base_event_id',
                                                    ctx=Load(),
                                                ),
                                                attr='read',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='base_event_time_fields', ctx=Load())],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='old_event_values', ctx=Load()),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Subscript(
                                                        value=Name(id='new_event_values', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='old_event_values', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='key', ctx=Store()),
                                                        iter=Name(id='base_event_time_fields', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='base_event_id', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_event_ids',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='base_event_id', ctx=Load()),
                                            ),
                                            attr='microsoft_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_event_ids',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='base_event_id', ctx=Load()),
                                            ),
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='base_event_id', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='dont_notify',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='new_event_values', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='microsoft_id',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='need_sync_m',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='rrule',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='current_rrule', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='dont_notify',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='_apply_recurrence',
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
                            orelse=[
                                Assign(
                                    targets=[Name(id='time_fields', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
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
                                                attr='_get_time_fields',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=BitOr(),
                                        right=Call(
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
                                                attr='_get_recurrent_fields',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_write_events',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    DictComp(
                                                        key=Name(id='field', ctx=Load()),
                                                        value=Name(id='value', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='field', ctx=Store()),
                                                                        Name(id='value', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='new_event_values', ctx=Load()),
                                                                        attr='items',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Name(id='field', ctx=Load()),
                                                                        ops=[NotIn()],
                                                                        comparators=[Name(id='time_fields', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='need_sync_m',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='rrule',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='current_rrule', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='detached_events', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_apply_recurrence',
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
                                            value=Name(id='detached_events', ctx=Load()),
                                            attr='microsoft_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='detached_events', ctx=Load()),
                                            attr='unlink',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_microsoft_sync_domain',
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='calendar_event_ids.user_id', kind=None),
                                            Constant(value='=', kind=None),
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
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='rrule', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=False, kind=None),
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
                    name='_cancel_microsoft',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_event_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_cancel_microsoft',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_cancel_microsoft',
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
                    name='_microsoft_to_odoo_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='microsoft_recurrence', annotation=None, type_comment=None),
                            arg(arg='default_reminders', annotation=None, type_comment=None),
                            arg(arg='default_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Tuple(elts=[], ctx=Load()),
                            Dict(keys=[], values=[]),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='microsoft_recurrence', ctx=Load()),
                                    attr='get_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    None,
                                    Constant(value='microsoft_id', kind=None),
                                ],
                                values=[
                                    Name(id='recurrence', ctx=Load()),
                                    Attribute(
                                        value=Name(id='microsoft_recurrence', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='_microsoft_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields_to_sync', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='events_outliers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_event_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='follow_recurrence',
                                                ctx=Load(),
                                            ),
                                        ),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='calendar_event_ids',
                                        ctx=Load(),
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='start', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='normal_event', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=BinOp(
                                            left=Name(id='events', ctx=Load()),
                                            op=Sub(),
                                            right=Name(id='events_outliers', ctx=Load()),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=1, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=1, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='normal_event', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='normal_event', ctx=Load()),
                                    attr='_microsoft_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields_to_sync', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='initial_values',
                                        value=Dict(
                                            keys=[Constant(value='type', kind=None)],
                                            values=[Constant(value='seriesMaster', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='microsoft_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='microsoft_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='events_outliers', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='event', ctx=Store()),
                                            iter=Name(id='events_outliers', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='event_value', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='_microsoft_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='fields_to_sync', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='values', ctx=Store()),
                                                    op=Add(),
                                                    value=List(
                                                        elts=[Name(id='event_value', ctx=Load())],
                                                        ctx=Load(),
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
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_ensure_attendees_have_email',
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='e', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='active',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_ensure_attendees_have_email',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
