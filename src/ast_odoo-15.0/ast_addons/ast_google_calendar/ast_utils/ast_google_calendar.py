Module(
    body=[
        ImportFrom(
            module='uuid',
            names=[alias(name='uuid4', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='exception_to_unicode', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_calendar.utils.google_event',
            names=[alias(name='GoogleEvent', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.google_account.models.google_service',
            names=[alias(name='TIMEOUT', asname=None)],
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
        FunctionDef(
            name='requires_auth_token',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='func', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='wrapped',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='kwargs', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='token', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AttributeError', ctx=Load()),
                                        args=[Constant(value='An authentication token is required', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='func', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrapped', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='InvalidSyncToken',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='GoogleCalendarService',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='google_service', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='google_service',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='google_service', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_events',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sync_token', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Name(id='TIMEOUT', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Constant(value='/calendar/v3/calendars/primary/events', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='Content-type', kind=None)],
                                values=[Constant(value='application/json', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='access_token', kind=None)],
                                values=[Name(id='token', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='sync_token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='syncToken', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='sync_token', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='ICP', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='google_service',
                                                        ctx=Load(),
                                                    ),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='day_range', ctx=Store())],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ICP', ctx=Load()),
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='google_calendar.sync.range_days', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='default',
                                                        value=Constant(value=365, kind=None),
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Full cal sync, restricting to %s days range', kind=None),
                                            Name(id='day_range', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='lower_bound', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='subtract',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
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
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Name(id='day_range', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='upper_bound', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
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
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='days',
                                                value=Name(id='day_range', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='timeMin', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='lower_bound', ctx=Load()),
                                                attr='isoformat',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value='Z', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='timeMax', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='upper_bound', ctx=Load()),
                                                attr='isoformat',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value='Z', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='status', ctx=Store()),
                                                Name(id='data', ctx=Store()),
                                                Name(id='time', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='google_service',
                                                ctx=Load(),
                                            ),
                                            attr='_do_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='url', ctx=Load()),
                                            Name(id='params', ctx=Load()),
                                            Name(id='headers', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='method',
                                                value=Constant(value='GET', kind=None),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='timeout', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='requests', ctx=Load()),
                                        attr='HTTPError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='response',
                                                                ctx=Load(),
                                                            ),
                                                            attr='status_code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=410, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='fullSyncRequired', kind=None),
                                                        ops=[In()],
                                                        comparators=[
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='e', ctx=Load()),
                                                                            attr='response',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='content',
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
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='InvalidSyncToken', ctx=Load()),
                                                        args=[Constant(value='Invalid sync token. Full sync required', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Raise(
                                            exc=Name(id='e', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='items', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='next_page_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='nextPageToken', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='next_page_token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='access_token', kind=None),
                                            Constant(value='pageToken', kind=None),
                                        ],
                                        values=[
                                            Name(id='token', ctx=Load()),
                                            Name(id='next_page_token', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='status', ctx=Store()),
                                                Name(id='data', ctx=Store()),
                                                Name(id='time', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='google_service',
                                                ctx=Load(),
                                            ),
                                            attr='_do_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='url', ctx=Load()),
                                            Name(id='params', ctx=Load()),
                                            Name(id='headers', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='method',
                                                value=Constant(value='GET', kind=None),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='timeout', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='next_page_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='nextPageToken', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='events', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='items', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='next_sync_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='nextSyncToken', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_reminders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='defaultReminders', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='GoogleEvent', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='next_sync_token', ctx=Load()),
                                    Name(id='default_reminders', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='requires_auth_token', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='insert',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Name(id='TIMEOUT', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Constant(value='/calendar/v3/calendars/primary/events?sendUpdates=all', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='Content-type', kind=None),
                                    Constant(value='Authorization', kind=None),
                                ],
                                values=[
                                    Constant(value='application/json', kind=None),
                                    BinOp(
                                        left=Constant(value='Bearer %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='values', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='id', kind=None)],
                                    keywords=[],
                                ),
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
                                        value=Call(
                                            func=Name(id='uuid4', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='hex',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
                                        ctx=Load(),
                                    ),
                                    attr='_do_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='headers', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='POST', kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='timeout', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=Name(id='values', ctx=Load()),
                                slice=Constant(value='id', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='requires_auth_token', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='patch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event_id', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Name(id='TIMEOUT', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/calendar/v3/calendars/primary/events/%s?sendUpdates=all', kind=None),
                                op=Mod(),
                                right=Name(id='event_id', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='Content-type', kind=None),
                                    Constant(value='Authorization', kind=None),
                                ],
                                values=[
                                    Constant(value='application/json', kind=None),
                                    BinOp(
                                        left=Constant(value='Bearer %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
                                        ctx=Load(),
                                    ),
                                    attr='_do_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='json', ctx=Load()),
                                            attr='dumps',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='headers', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='PUT', kind=None),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='timeout', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='requires_auth_token', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='delete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event_id', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Name(id='TIMEOUT', ctx=Load()),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/calendar/v3/calendars/primary/events/%s?sendUpdates=all', kind=None),
                                op=Mod(),
                                right=Name(id='event_id', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='Content-type', kind=None)],
                                values=[Constant(value='application/json', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='access_token', kind=None)],
                                values=[Name(id='token', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='google_service',
                                                ctx=Load(),
                                            ),
                                            attr='_do_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='url', ctx=Load()),
                                            Name(id='params', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='headers',
                                                value=Name(id='headers', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='method',
                                                value=Constant(value='DELETE', kind=None),
                                            ),
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='timeout', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='requests', ctx=Load()),
                                        attr='HTTPError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='response',
                                                        ctx=Load(),
                                                    ),
                                                    attr='status_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=410, kind=None),
                                                            Constant(value=403, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Name(id='e', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Google event %s was already deleted', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='event_id', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='requires_auth_token', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_authorized',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='user', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='google_calendar_rtoken',
                                        ctx=Load(),
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
                    name='_get_calendar_scope',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='RO', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='readonly', ctx=Store())],
                            value=IfExp(
                                test=Name(id='RO', ctx=Load()),
                                body=Constant(value='.readonly', kind=None),
                                orelse=Constant(value='', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='https://www.googleapis.com/auth/calendar%s', kind=None),
                                op=Mod(),
                                right=Name(id='readonly', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_google_authentication_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='http://www.odoo.com', kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='google_service',
                                        ctx=Load(),
                                    ),
                                    attr='_get_authorize_uri',
                                    ctx=Load(),
                                ),
                                args=[Name(id='from_url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='service',
                                        value=Constant(value='calendar', kind=None),
                                    ),
                                    keyword(
                                        arg='scope',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_calendar_scope',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                    name='_can_authorize_google',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='user', ctx=Load()),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.group_erp_manager', kind=None)],
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
