Module(
    body=[
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
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.microsoft_calendar.utils.microsoft_event',
            names=[alias(name='MicrosoftEvent', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.microsoft_account.models.microsoft_service',
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
            name='MicrosoftCalendarService',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='microsoft_service', annotation=None, type_comment=None),
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
                                    attr='microsoft_service',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='microsoft_service', ctx=Load()),
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
                            value=Constant(value='/v1.0/me/calendarView/delta', kind=None),
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
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='sync_token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='$deltatoken', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='sync_token', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='startDateTime', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='2016-12-01T00:00:00Z', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='endDateTime', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='2030-1-01T00:00:00Z', kind=None),
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
                                                attr='microsoft_service',
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
                                    Constant(value='value', kind=None),
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
                                args=[Constant(value='@odata.nextLink', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='next_page_token', ctx=Load()),
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
                                                attr='microsoft_service',
                                                ctx=Load(),
                                            ),
                                            attr='_do_request',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='next_page_token', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                            Name(id='headers', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='preuri',
                                                value=Constant(value='', kind=None),
                                            ),
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
                                        args=[Constant(value='@odata.nextLink', kind=None)],
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
                                            Constant(value='value', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='next_sync_token_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='@odata.deltaLink', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='next_sync_token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='urls', ctx=Load()),
                                                    attr='url_parse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='next_sync_token_url', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='decode_query',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='$deltatoken', kind=None),
                                    Constant(value=False, kind=None),
                                ],
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
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                            value=Constant(value='/v1.0/me/calendar/events', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='id', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='dummy', ctx=Store()),
                                        Name(id='data', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='microsoft_service',
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
                                        keywords=[
                                            keyword(
                                                arg='separators',
                                                value=Tuple(
                                                    elts=[
                                                        Constant(value=',', kind=None),
                                                        Constant(value=':', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
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
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Name(id='data', ctx=Load()),
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
                                left=Constant(value='/v1.0/me/calendar/events/%s', kind=None),
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
                                        attr='microsoft_service',
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
                                        keywords=[
                                            keyword(
                                                arg='separators',
                                                value=Tuple(
                                                    elts=[
                                                        Constant(value=',', kind=None),
                                                        Constant(value=':', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Name(id='headers', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='method',
                                        value=Constant(value='PATCH', kind=None),
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
                                left=Constant(value='/v1.0/me/calendar/events/%s', kind=None),
                                op=Mod(),
                                right=Name(id='event_id', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='Authorization', kind=None)],
                                values=[
                                    BinOp(
                                        left=Constant(value='Bearer %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='token', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='microsoft_service',
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
                                                        left=Constant(value='Microsoft event %s was already deleted', kind=None),
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
                    name='answer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event_id', annotation=None, type_comment=None),
                            arg(arg='answer', annotation=None, type_comment=None),
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
                                left=Constant(value='/v1.0/me/calendar/events/%s/%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='event_id', ctx=Load()),
                                        Name(id='answer', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        attr='microsoft_service',
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
                                        attr='microsoft_calendar_rtoken',
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
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='offline_access openid Calendars.ReadWrite', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_microsoft_authentication_url',
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
                                        attr='microsoft_service',
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
                    name='_can_authorize_microsoft',
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
