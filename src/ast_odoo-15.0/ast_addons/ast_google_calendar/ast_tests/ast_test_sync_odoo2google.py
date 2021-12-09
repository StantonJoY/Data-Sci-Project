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
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.utils.google_calendar',
            names=[alias(name='GoogleCalendarService', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.models.res_users',
            names=[alias(name='User', asname=None)],
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
            module='odoo.tests.common',
            names=[
                alias(name='users', asname=None),
                alias(name='warmup', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSyncOdoo2Google',
            bases=[Name(id='TestSyncGoogle', ctx=Load())],
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
                                    attr='google_service',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='GoogleCalendarService', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='google.service', kind=None),
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
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='google_calendar.sync.range_days', kind=None),
                                    Constant(value=10000, kind=None),
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
                    name='test_event_creation',
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
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean-Luc', kind=None),
                                            Constant(value='jean-luc@opoo.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='alarm_type', kind=None),
                                            Constant(value='interval', kind=None),
                                            Constant(value='duration', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Notif', kind=None),
                                            Constant(value='notification', kind=None),
                                            Constant(value='minutes', kind=None),
                                            Constant(value=18, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
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
                                            Constant(value='partner_ids', kind=None),
                                            Constant(value='alarm_ids', kind=None),
                                            Constant(value='privacy', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='id',
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
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='alarm', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='private', kind=None),
                                            Constant(value=False, kind=None),
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
                                    attr='_sync_odoo2google',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
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
                                    attr='assertGoogleEventInserted',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='visibility', kind=None),
                                            Constant(value='guestsCanModify', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='dateTime', kind=None)],
                                                values=[Constant(value='2020-01-15T08:00:00+00:00', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='dateTime', kind=None)],
                                                values=[Constant(value='2020-01-15T18:00:00+00:00', kind=None)],
                                            ),
                                            Constant(value='Event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='private', kind=None),
                                            Constant(value=True, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='useDefault', kind=None),
                                                    Constant(value='overrides', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='method', kind=None),
                                                                    Constant(value='minutes', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='popup', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='alarm', ctx=Load()),
                                                                        attr='duration_minutes',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='jean-luc@opoo.com', kind=None),
                                                            Constant(value='needsAction', kind=None),
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
                    name='test_event_creation_perf',
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
                            targets=[Name(id='EVENT_COUNT', ctx=Store())],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='Jean-Luc %s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                                BinOp(
                                                    left=Constant(value='jean-luc-%s@opoo.com', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='i', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Name(id='EVENT_COUNT', ctx=Load())],
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
                            type_comment=None,
                        ),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='alarm_type', kind=None),
                                            Constant(value='interval', kind=None),
                                            Constant(value='duration', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Notif', kind=None),
                                            Constant(value='notification', kind=None),
                                            Constant(value='minutes', kind=None),
                                            Constant(value=18, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_model', ctx=Store())],
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
                                args=[Constant(value='base.model_res_partner', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=1211, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
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
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            ListComp(
                                                elt=Dict(
                                                    keys=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='start', kind=None),
                                                        Constant(value='stop', kind=None),
                                                        Constant(value='partner_ids', kind=None),
                                                        Constant(value='alarm_ids', kind=None),
                                                        Constant(value='privacy', kind=None),
                                                        Constant(value='need_sync', kind=None),
                                                        Constant(value='res_model_id', kind=None),
                                                        Constant(value='res_id', kind=None),
                                                    ],
                                                    values=[
                                                        BinOp(
                                                            left=Constant(value='Event %s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='i', ctx=Load()),
                                                        ),
                                                        Call(
                                                            func=Name(id='datetime', ctx=Load()),
                                                            args=[
                                                                Constant(value=2020, kind=None),
                                                                Constant(value=1, kind=None),
                                                                Constant(value=15, kind=None),
                                                                Constant(value=8, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='datetime', ctx=Load()),
                                                            args=[
                                                                Constant(value=2020, kind=None),
                                                                Constant(value=1, kind=None),
                                                                Constant(value=15, kind=None),
                                                                Constant(value=18, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value=4, kind=None),
                                                                        Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='partners', ctx=Load()),
                                                                                slice=Name(id='i', ctx=Load()),
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
                                                                        Constant(value=4, kind=None),
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
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value=4, kind=None),
                                                                        Attribute(
                                                                            value=Name(id='alarm', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='private', kind=None),
                                                        Constant(value=False, kind=None),
                                                        Attribute(
                                                            value=Name(id='partner_model', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Name(id='EVENT_COUNT', ctx=Load())],
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
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='events', ctx=Load()),
                                            attr='_sync_odoo2google',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='google_service',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=129, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='events', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Name(id='patch_api', ctx=Load()),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='__system__', kind=None)],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_recurring_event_creation_perf',
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
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean-Luc', kind=None),
                                            Constant(value='jean-luc@opoo.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='alarm_type', kind=None),
                                            Constant(value='interval', kind=None),
                                            Constant(value='duration', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Notif', kind=None),
                                            Constant(value='notification', kind=None),
                                            Constant(value='minutes', kind=None),
                                            Constant(value=18, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_model', ctx=Store())],
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
                                args=[Constant(value='base.model_res_partner', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=3635, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
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
                                                    Constant(value='partner_ids', kind=None),
                                                    Constant(value='alarm_ids', kind=None),
                                                    Constant(value='privacy', kind=None),
                                                    Constant(value='need_sync', kind=None),
                                                    Constant(value='interval', kind=None),
                                                    Constant(value='recurrency', kind=None),
                                                    Constant(value='rrule_type', kind=None),
                                                    Constant(value='end_type', kind=None),
                                                    Constant(value='res_model_id', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Event', kind=None),
                                                    Call(
                                                        func=Name(id='datetime', ctx=Load()),
                                                        args=[
                                                            Constant(value=2020, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=15, kind=None),
                                                            Constant(value=8, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='datetime', ctx=Load()),
                                                        args=[
                                                            Constant(value=2020, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=15, kind=None),
                                                            Constant(value=18, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=4, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='id',
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
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=4, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='alarm', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='private', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value='daily', kind=None),
                                                    Constant(value='forever', kind=None),
                                                    Attribute(
                                                        value=Name(id='partner_model', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
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
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueryCount',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='__system__',
                                                value=Constant(value=2191, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Name(id='patch_api', ctx=Load()),
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='__system__', kind=None)],
                            keywords=[],
                        ),
                        Name(id='warmup', ctx=Load()),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_event_without_user',
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
                                            Constant(value='user_id', kind=None),
                                            Constant(value='privacy', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value='private', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='_google_values',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Compare(
                                        left=BinOp(
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
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='extendedProperties', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='shared', kind=None),
                                                    Dict(keys=[], values=[]),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_event_allday_creation',
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
                                            Constant(value='allday', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Constant(value=True, kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='_sync_odoo2google',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
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
                                    attr='assertGoogleEventInserted',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='visibility', kind=None),
                                            Constant(value='guestsCanModify', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-15', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-16', kind=None)],
                                            ),
                                            Constant(value='Event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                    name='test_inactive_event',
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
                                            Constant(value='active', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
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
                                    attr='_sync_odoo2google',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
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
                                    attr='assertGoogleEventNotInserted',
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
                                    attr='assertGoogleEventNotDeleted',
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
                    name='test_synced_inactive_event',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='google_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='active', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='_sync_odoo2google',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
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
                                    attr='assertGoogleEventDeleted',
                                    ctx=Load(),
                                ),
                                args=[Name(id='google_id', ctx=Load())],
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
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='google_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
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
                                            Constant(value='rrule', kind=None),
                                            Constant(value='calendar_event_ids', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
                                    attr='_sync_odoo2google',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
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
                                    attr='assertGoogleEventInserted',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='visibility', kind=None),
                                            Constant(value='guestsCanModify', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-15', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-16', kind=None)],
                                            ),
                                            Constant(value='Event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='accepted', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None)],
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
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='recurrence', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
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
                    name='test_event_added_to_recurrence',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='google_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='allday', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
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
                                            Constant(value='recurrency', kind=None),
                                            Constant(value='rrule', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='to_delete', ctx=Store())],
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='active_test',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='to_delete', ctx=Load())],
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
                                        value=Name(id='to_delete', ctx=Load()),
                                        attr='active',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='google_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The google id will be set after the API call', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleEventInserted',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='visibility', kind=None),
                                            Constant(value='guestsCanModify', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-15', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value='2020-01-16', kind=None)],
                                            ),
                                            Constant(value='Event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='accepted', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None)],
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
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='recurrence_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleEventDeleted',
                                    ctx=Load(),
                                ),
                                args=[Name(id='google_id', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='patch_api', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_following_event_updated',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event_1', ctx=Store())],
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event_2', ctx=Store())],
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=22, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=22, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
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
                                            Constant(value='calendar_event_ids', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='event_1', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='event_2', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Name(id='event_2', ctx=Load()),
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
                                            Constant(value='name', kind=None),
                                            Constant(value='recurrence_update', kind=None),
                                        ],
                                        values=[
                                            Constant(value='New name', kind=None),
                                            Constant(value='future_events', kind=None),
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
                                            Constant(value='New name', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                    name='test_stop_synchronization',
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='stop_google_synchronization',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
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
                                        attr='google_synchronization_stopped',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The google synchronization flag should be switched on', kind=None),
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
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='_sync_google_calendar',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='google_service',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='The google synchronization should be stopped', kind=None),
                                ],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='privacy', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='private', kind=None),
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
                                    attr='assertGoogleEventNotInserted',
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
                    name='test_restart_synchronization',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean-Luc', kind=None),
                                            Constant(value='jean-luc@opoo.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test user Calendar', kind=None),
                                            Constant(value='jean-luc@opoo.com', kind=None),
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
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
                                    value=Name(id='user', ctx=Load()),
                                    attr='stop_google_synchronization',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                            Constant(value='google_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=18, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='restart_google_synchronization',
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
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='visibility', kind=None),
                                            Constant(value='guestsCanModify', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='google_id',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='dateTime', kind=None)],
                                                values=[Constant(value='2020-01-15T08:00:00+00:00', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='dateTime', kind=None)],
                                                values=[Constant(value='2020-01-15T18:00:00+00:00', kind=None)],
                                            ),
                                            Constant(value='Event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='public', kind=None),
                                            Constant(value=True, kind=None),
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
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='jean-luc@opoo.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='jean-luc@opoo.com', kind=None),
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
                    name='test_all_event_updated',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
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
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
                                            Constant(value='name', kind=None),
                                            Constant(value='recurrence_update', kind=None),
                                        ],
                                        values=[
                                            Constant(value='New name', kind=None),
                                            Constant(value='all_events', kind=None),
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
                                        value=Name(id='recurrence', ctx=Load()),
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
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='visibility', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='recurrence', ctx=Load()),
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
                                            Constant(value='New name', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='accepted', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None)],
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
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='recurrence', ctx=Load()),
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
                    name='test_event_need_sync',
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
                                            Constant(value='recurrence_id', kind=None),
                                            Constant(value='recurrency', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='need_sync',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Event created with True recurrency should not be synched to avoid duplicate event on google', kind=None),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='google_id', kind=None),
                                            Constant(value='rrule', kind=None),
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
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
                            targets=[Name(id='event_2', ctx=Store())],
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
                                            Constant(value='recurrence_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Name(id='recurrence', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event_2', ctx=Load()),
                                        attr='need_sync',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Event created with recurrence_id should not be synched to avoid duplicate event on google', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGoogleEventNotInserted',
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
                                    attr='assertGoogleEventNotDeleted',
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
                    name='test_event_until_utc',
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
                            value=Constant(value=" UNTIl rrule value must be in UTC: ending with a 'Z ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='google_id', ctx=Store())],
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
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
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=DAILY;UNTIL=20200117T235959', kind=None),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='_google_values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            slice=Constant(value='recurrence', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='RRULE:FREQ=DAILY;UNTIL=20200117T235959Z', kind=None),
                                    Constant(value='The rrule sent to google should be in UTC: end with Z', kind=None),
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
                                args=[
                                    Dict(
                                        keys=[Constant(value='rrule', kind=None)],
                                        values=[Constant(value='FREQ=DAILY;UNTIL=20200118T235959;INTERVAL=3', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='_google_values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            slice=Constant(value='recurrence', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='RRULE:FREQ=DAILY;UNTIL=20200118T235959Z;INTERVAL=3', kind=None),
                                    Constant(value='The rrule sent to google should be in UTC: end with Z and preserve the following parameters', kind=None),
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
                                args=[
                                    Dict(
                                        keys=[Constant(value='rrule', kind=None)],
                                        values=[Constant(value='FREQ=DAILY;UNTIL=20200119T235959Z', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='_google_values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            slice=Constant(value='recurrence', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='RRULE:FREQ=DAILY;UNTIL=20200119T235959Z', kind=None),
                                    Constant(value='The rrule sent to google should be in UTC: end with one Z', kind=None),
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
                    name='test_write_unsynced_field',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
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
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=11, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=11, kind=None),
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
                            targets=[Name(id='event_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='calendar.event.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='type', kind=None)],
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
                                            Constant(value='recurrence_update', kind=None),
                                            Constant(value='categ_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='all_events', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='event_type', ctx=Load()),
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
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='categ_ids',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='event_type', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='e', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='recurrence', ctx=Load()),
                                                            attr='calendar_event_ids',
                                                            ctx=Load(),
                                                        ),
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
                        Expr(
                            value=Constant(value=' Sync attendee state immediately ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean-Luc', kind=None),
                                            Constant(value='jean-luc@opoo.com', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
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
                                            Constant(value='need_sync', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                            Constant(value='google_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event with attendees', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='aaaaaaaaa', kind=None),
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
                                    Constant(value='needsAction', kind=None),
                                    Constant(value="The attendee state should be 'needsAction", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='attendee_ids',
                                        ctx=Load(),
                                    ),
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
                                            Constant(value='Event with attendees', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='jean-luc@opoo.com', kind=None),
                                                            Constant(value='declined', kind=None),
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
                                            Constant(value='public', kind=None),
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
                    name='test_all_event_with_tz_updated',
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
                            value=Constant(value='aaaaaaaaa', kind=None),
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
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=8, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=9, kind=None),
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
                                            Constant(value='base_event_id', kind=None),
                                            Constant(value='need_sync', kind=None),
                                        ],
                                        values=[
                                            Name(id='google_id', ctx=Load()),
                                            Constant(value='FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None),
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
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
                                            Constant(value='name', kind=None),
                                            Constant(value='recurrence_update', kind=None),
                                        ],
                                        values=[
                                            Constant(value='New name', kind=None),
                                            Constant(value='all_events', kind=None),
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
                                        value=Name(id='recurrence', ctx=Load()),
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
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='extendedProperties', kind=None),
                                            Constant(value='reminders', kind=None),
                                            Constant(value='visibility', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='recurrence', ctx=Load()),
                                                attr='google_id',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-01-15T08:00:00+00:00', kind=None),
                                                    Constant(value='Europe/Brussels', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-01-15T09:00:00+00:00', kind=None),
                                                    Constant(value='Europe/Brussels', kind=None),
                                                ],
                                            ),
                                            Constant(value='New name', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value=True, kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='self', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='odoobot@example.com', kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            Constant(value='accepted', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='RRULE:FREQ=WEEKLY;COUNT=2;BYDAY=WE', kind=None)],
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
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='recurrence', ctx=Load()),
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='odoo2google', kind=None)],
                    keywords=[],
                ),
                Call(
                    func=Attribute(
                        value=Name(id='patch', ctx=Load()),
                        attr='object',
                        ctx=Load(),
                    ),
                    args=[
                        Name(id='User', ctx=Load()),
                        Constant(value='_get_google_calendar_token', kind=None),
                        Lambda(
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='user', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=Constant(value='dummy-token', kind=None),
                        ),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
