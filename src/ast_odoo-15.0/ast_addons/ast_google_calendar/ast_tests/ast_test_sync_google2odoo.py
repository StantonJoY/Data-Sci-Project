Module(
    body=[
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='date', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='new_test_user', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.tests.test_sync_common',
            names=[
                alias(name='TestSyncGoogle', asname=None),
                alias(name='patch_api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.utils.google_calendar',
            names=[alias(name='GoogleEvent', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='html2plaintext', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSyncGoogle2Odoo',
            bases=[Name(id='TestSyncGoogle', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='now',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='utc',
                                                ctx=Load(),
                                            ),
                                            attr='localize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='isoformat',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='sync',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='events', annotation=None, type_comment=None),
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
                                    value=Name(id='events', ctx=Load()),
                                    attr='clear_type_ambiguity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='google_recurrence', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='events', ctx=Load()),
                                    attr='filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='GoogleEvent', ctx=Load()),
                                        attr='is_recurrence',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[Name(id='google_recurrence', ctx=Load())],
                                keywords=[],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='events', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='google_recurrence', ctx=Load()),
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
                    name='test_new_google_event',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mitchell Admin', kind=None),
                                                    Constant(value='admin@yourcompany.example.com', kind=None),
                                                    Constant(value='needsAction', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T16:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T19:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Constant(value='It should have created an event', kind=None),
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
                                        value=Name(id='event', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='summary', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='allday',
                                        ctx=Load(),
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
                                    Call(
                                        func=Name(id='html2plaintext', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='description',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='description', kind=None)],
                                        keywords=[],
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
                                        value=Name(id='event', ctx=Load()),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=55, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Name(id='event', ctx=Load()),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=18, kind=None),
                                            Constant(value=55, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='admin_attendee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='event', ctx=Load()),
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
                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='admin@yourcompany.example.com', kind=None)],
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
                                    Constant(value='admin@yourcompany.example.com', kind=None),
                                    Attribute(
                                        value=Name(id='admin_attendee', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
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
                                    Constant(value='Mitchell Admin', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='admin_attendee', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
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
                                        value=Name(id='event', ctx=Load()),
                                        attr='partner_ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='attendee_ids',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
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
                                    Constant(value='needsAction', kind=None),
                                    Attribute(
                                        value=Name(id='admin_attendee', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_invalid_owner_property',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='extendedProperties', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T16:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='shared', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    BinOp(
                                                        left=Constant(value='%s_owner_id', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='dbname',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                values=[Constant(value='invalid owner id', kind=None)],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T19:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_valid_owner_property',
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
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='calendar-user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='extendedProperties', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(elts=[], ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T16:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[Constant(value='shared', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    BinOp(
                                                        left=Constant(value='%s_owner_id', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='dbname',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T19:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='user', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cancelled',
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
                            value=Constant(value=' Cancel event when the current user is the organizer ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='google_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='google_id', ctx=Load()),
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
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
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
                                                                attr='ids',
                                                                ctx=Load(),
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
                        Assign(
                            targets=[Name(id='gevent', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Name(id='google_id', ctx=Load()),
                                                    Constant(value='cancelled', kind=None),
                                                ],
                                            ),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[Name(id='gevent', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attendee_cancelled',
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
                            value=Constant(value=' Cancel event when the current user is not the organizer ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='calendar-user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='google_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=5, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='set',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                        Assign(
                            targets=[Name(id='gevent', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Name(id='google_id', ctx=Load()),
                                                    Constant(value='cancelled', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_attendee', ctx=Store())],
                            value=Attribute(
                                value=Name(id='event', ctx=Load()),
                                attr='attendee_ids',
                                ctx=Load(),
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
                                        value=Name(id='user_attendee', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='needsAction', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='gevent', ctx=Load()),
                                    attr='clear_type_ambiguity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                                slice=Constant(value='calendar.event', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[Name(id='gevent', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='user_attendee', ctx=Store())],
                            value=Attribute(
                                value=Name(id='event', ctx=Load()),
                                attr='attendee_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_attendee', ctx=Load())],
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
                                        value=Name(id='user_attendee', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='declined', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_private_extended_properties',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='google_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
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
                                                                attr='ids',
                                                                ctx=Load(),
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
                        Assign(
                            targets=[Name(id='user_attendee', ctx=Store())],
                            value=Attribute(
                                value=Name(id='event', ctx=Load()),
                                attr='attendee_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_attendee', ctx=Load())],
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
                                        value=Name(id='user_attendee', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='accepted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_attendee', ctx=Load()),
                                    attr='do_decline',
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
                                    attr='assertGoogleEventPatched',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                            Constant(value='reminders', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='google_id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='coucou', kind=None),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='start_date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='stop_date',
                                                                    ctx=Load(),
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
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='responseStatus', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='odoobot@example.com', kind=None),
                                                            Constant(value='declined', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='private', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            BinOp(
                                                                left=Constant(value='%s_odoo_id', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='dbname',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='overrides', kind=None),
                                                    Constant(value='useDefault', kind=None),
                                                ],
                                                values=[
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attendee_removed',
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
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='calendar-user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                                slice=Constant(value='calendar.event', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='google_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='partner_id',
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='gevent', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='description', kind=None),
                                                    Constant(value='updated', kind=None),
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='visibility', kind=None),
                                                    Constant(value='attendees', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='end', kind=None),
                                                ],
                                                values=[
                                                    Name(id='google_id', ctx=Load()),
                                                    Constant(value='Small mini desc', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='self', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                    ),
                                                    Constant(value='Pricing new update', kind=None),
                                                    Constant(value='public', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='dateTime', kind=None),
                                                            Constant(value='timeZone', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2020-01-13T16:55:00+01:00', kind=None),
                                                            Constant(value='Europe/Brussels', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='dateTime', kind=None),
                                                            Constant(value='timeZone', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2020-01-13T19:55:00+01:00', kind=None),
                                                            Constant(value='Europe/Brussels', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='partner_ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
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
                                            value=Name(id='event', ctx=Load()),
                                            attr='attendee_ids',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[Name(id='gevent', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='attendee_ids',
                                            ctx=Load(),
                                        ),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='partner_ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='recurrence_id', ctx=Load()),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2020-01-6', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2020-01-7', kind=None)],
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='recurrence', ctx=Load()),
                                    Constant(value='it should have created a recurrence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='it should have created a recurrence with 3 events', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='events', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='recurrency', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200106', kind=None),
                                        op=Mod(),
                                        right=Name(id='recurrence_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200113', kind=None),
                                        op=Mod(),
                                        right=Name(id='recurrence_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200120', kind=None),
                                        op=Mod(),
                                        right=Name(id='recurrence_id', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_datetime',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='recurrence_id', ctx=Load()),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='dateTime', kind=None)],
                                        values=[Constant(value='2020-01-06T18:00:00+01:00', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='dateTime', kind=None)],
                                        values=[Constant(value='2020-01-06T19:00:00+01:00', kind=None)],
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='recurrence', ctx=Load()),
                                    Constant(value='it should have created a recurrence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='it should have created a recurrence with 3 events', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='events', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='recurrency', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200106T170000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='recurrence_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200113T170000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='recurrence_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200120T170000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='recurrence_id', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_exdate',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='recurrence', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='end', kind=None),
                                                ],
                                                values=[
                                                    Name(id='recurrence_id', ctx=Load()),
                                                    Constant(value='Pricing new update', kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='self', kind=None),
                                                        ],
                                                        values=[
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
                                                                attr='email',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-6', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-7', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='originalStartTime', kind=None),
                                                    Constant(value='recurringEventId', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='%s_20200113', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='recurrence_id', ctx=Load()),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='dateTime', kind=None)],
                                                        values=[Constant(value='2020-01-13', kind=None)],
                                                    ),
                                                    Constant(value='oj44nep1ldf8a3ll02uip0c9pk', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Constant(value='cancelled', kind=None),
                                                ],
                                            ),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[Name(id='events', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='recurrence_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='recurrence', ctx=Load()),
                                    Constant(value='it should have created a recurrence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='it should have created a recurrence with 2 events', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_first_exdate',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='4c0de517evkk3ra294lmut57vm', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='updated', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='end', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='recurrence', kind=None),
                                                ],
                                                values=[
                                                    Name(id='recurrence_id', ctx=Load()),
                                                    Constant(value='2020-01-13T16:17:03.806Z', kind=None),
                                                    Constant(value='r rul', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-6', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='self', kind=None),
                                                        ],
                                                        values=[
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
                                                                attr='email',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-7', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    List(
                                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='status', kind=None),
                                                    Constant(value='recurringEventId', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='originalStartTime', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='%s_20200106', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='recurrence_id', ctx=Load()),
                                                    ),
                                                    Constant(value='cancelled', kind=None),
                                                    Constant(value='4c0de517evkk3ra294lmut57vm', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-06', kind=None)],
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[Name(id='events', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='recurrence_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='it should have created a recurrence with 2 events', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrencde_first_updated',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='4c0de517evkk3ra294lmut57vm', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='recurrence', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='end', kind=None),
                                                    Constant(value='status', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='updated', kind=None),
                                                ],
                                                values=[
                                                    Name(id='recurrence_id', ctx=Load()),
                                                    List(
                                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=WE', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-01', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-02', kind=None)],
                                                    ),
                                                    Constant(value='confirmed', kind=None),
                                                    Constant(value='rrule', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='originalStartTime', kind=None),
                                                    Constant(value='recurringEventId', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='end', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='updated', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='edited', kind=None),
                                                    BinOp(
                                                        left=Constant(value='%s_20200101', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='recurrence_id', ctx=Load()),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-01', kind=None)],
                                                    ),
                                                    Name(id='recurrence_id', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-01', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-02', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[Name(id='events', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='recurrence_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='it should have created a recurrence with 3 events', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='edited', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='rrule', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='rrule', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_existing_recurrence_first_updated',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='4c0de517evkk3ra294lmut57vm', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                        ],
                                        values=[
                                            Name(id='recurrence_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='summary', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='originalStartTime', kind=None),
                                            Constant(value='recurringEventId', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='updated', kind=None),
                                        ],
                                        values=[
                                            Constant(value='edited', kind=None),
                                            BinOp(
                                                left=Constant(value='%s_20200106', kind=None),
                                                op=Mod(),
                                                right=Name(id='recurrence_id', ctx=Load()),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-06', kind=None)],
                                            ),
                                            Name(id='recurrence_id', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-06', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-07', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='useDefault', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='now',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='recurrence_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='it should have created a recurrence with 3 events', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='edited', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='coucou', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='coucou', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_outlier',
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
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Name(id='GoogleEvent', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='recurrence', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='end', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='updated', kind=None),
                                                ],
                                                values=[
                                                    Name(id='recurrence_id', ctx=Load()),
                                                    Constant(value='Pricing new update', kind=None),
                                                    List(
                                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-6', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-7', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='summary', kind=None),
                                                    Constant(value='start', kind=None),
                                                    Constant(value='end', kind=None),
                                                    Constant(value='originalStartTime', kind=None),
                                                    Constant(value='reminders', kind=None),
                                                    Constant(value='updated', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='%s_20200113', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='recurrence_id', ctx=Load()),
                                                    ),
                                                    Constant(value='Pricing new update', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-18', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-19', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='date', kind=None)],
                                                        values=[Constant(value='2020-01-13', kind=None)],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='useDefault', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[Name(id='events', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='recurrence_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='recurrence', ctx=Load()),
                                    Constant(value='it should have created a recurrence', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='it should have created a recurrence with 3 events', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=18, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='It should not be in sync with the recurrence', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_moved',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='base_event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='updated', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='coucou', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2020-01-08', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2020-01-09', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value='accepted', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Name(id='recurrence', ctx=Load()),
                                        attr='rrule',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=15, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200108', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200115', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_name_updated',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='base_event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='updated', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='coucou again', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=2;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2020-01-06', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='date', kind=None)],
                                        values=[Constant(value='2020-01-07', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value='accepted', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        value=Name(id='recurrence', ctx=Load()),
                                        attr='rrule',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=MO', kind=None),
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
                                        func=Attribute(
                                            value=Name(id='events', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='coucou again', kind=None),
                                            Constant(value='coucou again', kind=None),
                                        ],
                                        ctx=Load(),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='date', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=13, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200106', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20200113', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_write_with_outliers',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='base_event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20210215T080000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20210222T080000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20210301T080000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='middle_event', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='start',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Call(
                                                    func=Name(id='datetime', ctx=Load()),
                                                    args=[
                                                        Constant(value=2021, kind=None),
                                                        Constant(value=2, kind=None),
                                                        Constant(value=22, kind=None),
                                                        Constant(value=8, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='middle_event', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='start', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=22, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='updated', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='coucou again', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='dateTime', kind=None)],
                                        values=[Constant(value='2021-02-15T09:00:00+01:00', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='dateTime', kind=None)],
                                        values=[Constant(value='2021-02-15-T11:00:00+01:00', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value='accepted', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
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
                                        value=Name(id='recurrence', ctx=Load()),
                                        attr='rrule',
                                        ctx=Load(),
                                    ),
                                    Constant(value='FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None),
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
                                        func=Attribute(
                                            value=Name(id='events', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='coucou again', kind=None),
                                            Constant(value='coucou again', kind=None),
                                            Constant(value='coucou again', kind=None),
                                        ],
                                        ctx=Load(),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=22, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20210215T080000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20210222T080000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s_20210301T080000Z', kind=None),
                                        op=Mod(),
                                        right=Name(id='google_id', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_write_time_fields',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='base_event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='updated', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value="It's me again", kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=4;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='dateTime', kind=None)],
                                        values=[Constant(value='2021-02-15T12:00:00+01:00', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='dateTime', kind=None)],
                                        values=[Constant(value='2021-02-15-T15:00:00+01:00', kind=None)],
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value='accepted', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=22, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=8, kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_deleted',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=10, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='base_event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Attribute(
                                value=Name(id='recurrence', ctx=Load()),
                                attr='calendar_event_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='status', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='cancelled', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sync',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='The recurrence should be deleted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='events', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='All events should be deleted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_timezone',
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
                            value=Constant(value=' Ensure that the timezone of the base_event is saved on the recurrency\n        Google save the TZ on the event and we save it on the recurrency.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='recurrence_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='recurrence_id', ctx=Load()),
                                    Constant(value='', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Event with ', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-06T18:00:00+01:00', kind=None),
                                            Constant(value='Pacific/Auckland', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-06T19:00:00+01:00', kind=None),
                                            Constant(value='Pacific/Auckland', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
                                        attr='event_tz',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Pacific/Auckland', kind=None),
                                    Constant(value='The Google event Timezone should be saved on the recurrency', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_simple_event_into_recurrency',
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
                            value=Constant(value=' Synched single events should be converted in recurrency without problems', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='aaaaaaaaaaaa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mitchell Admin', kind=None),
                                                    Constant(value='admin@yourcompany.example.com', kind=None),
                                                    Constant(value='needsAction', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-06T18:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T19:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Event with ', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;WKST=SU;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-06T18:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-06T19:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
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
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='it should have created a recurrence with 3 events', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='id', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='The old event should not exits anymore', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_new_google_notifications',
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
                            value=Constant(value=' Event from Google should not create notifications and trigger. It ruins the perfs on large databases ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='cron_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='ref',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='calendar.ir_cron_scheduler_alarm', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='triggers_before', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.cron.trigger', kind=None),
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
                                                    Constant(value='cron_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='cron_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
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
                                            arg='months',
                                            value=Constant(value=1, kind=None),
                                        ),
                                        keyword(
                                            arg='day',
                                            value=Constant(value=1, kind=None),
                                        ),
                                        keyword(
                                            arg='hours',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
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
                                            arg='months',
                                            value=Constant(value=1, kind=None),
                                        ),
                                        keyword(
                                            arg='day',
                                            value=Constant(value=1, kind=None),
                                        ),
                                        keyword(
                                            arg='hours',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='updated', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
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
                                            arg='minutes',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='Small mini desc', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing new update', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mitchell Admin', kind=None),
                                                    Constant(value='admin@yourcompany.example.com', kind=None),
                                                    Constant(value='needsAction', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='overrides', kind=None),
                                            Constant(value='useDefault', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='method', kind=None),
                                                            Constant(value='minutes', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='utc',
                                                                ctx=Load(),
                                                            ),
                                                            attr='localize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='start', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='isoformat',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='utc',
                                                                ctx=Load(),
                                                            ),
                                                            attr='localize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='end', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='isoformat',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='triggers_after', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.cron.trigger', kind=None),
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
                                                    Constant(value='cron_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='cron_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='new_triggers', ctx=Store())],
                            value=BinOp(
                                left=Name(id='triggers_after', ctx=Load()),
                                op=Sub(),
                                right=Name(id='triggers_before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='new_triggers', ctx=Load()),
                                    Constant(value='The event should not be created with triggers.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='updated', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='pytz', ctx=Load()),
                                                        attr='utc',
                                                        ctx=Load(),
                                                    ),
                                                    attr='localize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='updated', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='isoformat',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='New Super description', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value='Pricing was not good, now it is correct', kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mitchell Admin', kind=None),
                                                    Constant(value='admin@yourcompany.example.com', kind=None),
                                                    Constant(value='needsAction', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='overrides', kind=None),
                                            Constant(value='useDefault', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='method', kind=None),
                                                            Constant(value='minutes', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value=10, kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='utc',
                                                                ctx=Load(),
                                                            ),
                                                            attr='localize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='start', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='isoformat',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='utc',
                                                                ctx=Load(),
                                                            ),
                                                            attr='localize',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='end', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='isoformat',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='triggers_after', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.cron.trigger', kind=None),
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
                                                    Constant(value='cron_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='cron_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='new_triggers', ctx=Store())],
                            value=BinOp(
                                left=Name(id='triggers_after', ctx=Load()),
                                op=Sub(),
                                right=Name(id='triggers_before', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='new_triggers', ctx=Load()),
                                    Constant(value='The event should not be created with triggers.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attendee_state',
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
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='calendar-user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                                slice=Constant(value='calendar.event', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='google_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event with me', kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='partner_id',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='attendee_ids',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='accepted', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='updated', kind=None),
                                    Constant(value='organizer', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='visibility', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Constant(value='Changed my mind', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='self', kind=None),
                                        ],
                                        values=[
                                            Constant(value='odoocalendarref@gmail.com', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                    Constant(value="I don't want to be with me anymore", kind=None),
                                    Constant(value='public', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='calendar-user (base.group_user)', kind=None),
                                                    Constant(value='c.c@example.com', kind=None),
                                                    Constant(value='declined', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T16:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2020-01-13T19:55:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
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
                                            value=Name(id='event', ctx=Load()),
                                            attr='attendee_ids',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='declined', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attendees_same_event_both_share',
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='oj44nep1ldf8a3ll02uip0c9aa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='other_user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='calendar-user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='google_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=6, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='other_user', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
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
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='other_user', ctx=Load()),
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
                                    value=Name(id='event', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=7, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='date', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=8, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleEventPatched',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='guestsCanModify', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='visibility', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='google_id',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='start_date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='stop_date',
                                                                    ctx=Load(),
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
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='coucou', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='c.c@example.com', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='responseStatus', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='c.c@example.com', kind=None),
                                                            Constant(value='needsAction', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='responseStatus', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='odoobot@example.com', kind=None),
                                                            Constant(value='accepted', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='shared', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            BinOp(
                                                                left=Constant(value='%s_odoo_id', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='dbname',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value='%s_owner_id', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='cr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='dbname',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='other_user', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='overrides', kind=None),
                                                    Constant(value='useDefault', kind=None),
                                                ],
                                                values=[
                                                    List(elts=[], ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Constant(value='public', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=3, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attendee_recurrence_answer',
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
                            value=Constant(value=' Write on a recurrence to update all attendee answers ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='other_user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='calendar-user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='aaaaaaaaaaa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_event', ctx=Store())],
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
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='event_tz', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='coucou', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=7, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=9, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='Europe/Brussels', kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='other_user', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Name(id='base_event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='base_event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    value=Name(id='recurrence', ctx=Load()),
                                    attr='_apply_recurrence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='calendar_event_ids',
                                            ctx=Load(),
                                        ),
                                        attr='attendee_ids',
                                        ctx=Load(),
                                    ),
                                    attr='state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='accepted', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='updated', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='c.c@example.com', kind=None),
                                                    Constant(value='declined', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='coucou', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2021-02-15T8:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2021-02-15T10:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attendee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='calendar_event_ids',
                                            ctx=Load(),
                                        ),
                                        attr='attendee_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
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
                                    Name(id='attendee', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='declined', kind=None),
                                            Constant(value='declined', kind=None),
                                            Constant(value='declined', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='All events should be declined', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurrence_creation_with_attendee_answer',
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
                            value=Constant(value=' Create a recurrence with predefined attendee answers ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='aaaaaaaaaaa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='updated', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='attendees', kind=None),
                                    Constant(value='summary', kind=None),
                                    Constant(value='recurrence', kind=None),
                                    Constant(value='reminders', kind=None),
                                    Constant(value='start', kind=None),
                                    Constant(value='end', kind=None),
                                ],
                                values=[
                                    Name(id='google_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='responseStatus', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='c.c@example.com', kind=None),
                                                    Constant(value='declined', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='coucou', kind=None),
                                    List(
                                        elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=3;BYDAY=MO', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='useDefault', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2021-02-15T8:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='dateTime', kind=None),
                                            Constant(value='timeZone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2021-02-15T10:00:00+01:00', kind=None),
                                            Constant(value='Europe/Brussels', kind=None),
                                        ],
                                    ),
                                ],
                            ),
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
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_google2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[Name(id='values', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence', ctx=Store())],
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='google_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='google_id', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='attendee', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='calendar_event_ids',
                                            ctx=Load(),
                                        ),
                                        attr='attendee_ids',
                                        ctx=Load(),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
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
                                    Name(id='attendee', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='declined', kind=None),
                                            Constant(value='declined', kind=None),
                                            Constant(value='declined', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='All events should be declined', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleAPINotCalled',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
