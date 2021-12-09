Module(
    body=[
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
            module='unittest.mock',
            names=[
                alias(name='MagicMock', asname=None),
                alias(name='patch', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.microsoft_calendar.utils.microsoft_calendar',
            names=[alias(name='MicrosoftCalendarService', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.microsoft_calendar.models.res_users',
            names=[alias(name='User', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.microsoft_calendar.models.microsoft_sync',
            names=[alias(name='MicrosoftSync', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.registry',
            names=[alias(name='Registry', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.microsoft_account.models.microsoft_service',
            names=[alias(name='TIMEOUT', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='patch_api',
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
                    name='patched',
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='object',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='MicrosoftSync', ctx=Load()),
                                Constant(value='_microsoft_insert', kind=None),
                                Call(
                                    func=Name(id='MagicMock', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='object',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='MicrosoftSync', ctx=Load()),
                                Constant(value='_microsoft_delete', kind=None),
                                Call(
                                    func=Name(id='MagicMock', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='object',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='MicrosoftSync', ctx=Load()),
                                Constant(value='_microsoft_patch', kind=None),
                                Call(
                                    func=Name(id='MagicMock', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='patched', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='TestSyncOdoo2Microsoft',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                                    attr='microsoft_service',
                                    ctx=Store(),
                                ),
                            ],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertMicrosoftEventInserted',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Name(id='MicrosoftSync', ctx=Load()),
                                        attr='_microsoft_insert',
                                        ctx=Load(),
                                    ),
                                    attr='assert_called_once_with',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='microsoft_service',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                    name='assertMicrosoftEventNotInserted',
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
                                        value=Name(id='MicrosoftSync', ctx=Load()),
                                        attr='_microsoft_insert',
                                        ctx=Load(),
                                    ),
                                    attr='assert_not_called',
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
                    name='assertMicrosoftEventPatched',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='microsoft_id', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expected_args', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Name(id='microsoft_id', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_kwargs', ctx=Store())],
                            value=IfExp(
                                test=Name(id='timeout', ctx=Load()),
                                body=Dict(
                                    keys=[Constant(value='timeout', kind=None)],
                                    values=[Name(id='timeout', ctx=Load())],
                                ),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='MicrosoftSync', ctx=Load()),
                                        attr='_microsoft_patch',
                                        ctx=Load(),
                                    ),
                                    attr='assert_called_once',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='args', ctx=Store()),
                                        Name(id='kwargs', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='MicrosoftSync', ctx=Load()),
                                    attr='_microsoft_patch',
                                    ctx=Load(),
                                ),
                                attr='call_args',
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
                                    Subscript(
                                        value=Name(id='args', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='expected_args', ctx=Load()),
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
                                    Name(id='kwargs', ctx=Load()),
                                    Name(id='expected_kwargs', ctx=Load()),
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
                                    attr='stop_microsoft_synchronization',
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
                                        attr='microsoft_synchronization_stopped',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The microsoft synchronization flag should be switched on', kind=None),
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
                                            attr='_sync_microsoft_calendar',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='microsoft_service',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='The microsoft synchronization should be stopped', kind=None),
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
                                    attr='assertMicrosoftEventNotInserted',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='maxDiff',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='microsoft_id', ctx=Store())],
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
                                    attr='stop_microsoft_synchronization',
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
                                            Constant(value='microsoft_id', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='stop', kind=None),
                                            Constant(value='partner_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='microsoft_id', ctx=Load()),
                                            Constant(value='Event', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2021, kind=None),
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
                                                    Constant(value=2021, kind=None),
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
                                    attr='restart_microsoft_synchronization',
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
                                            value=Name(id='event', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='user', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_sync_odoo2microsoft',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='microsoft_service',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='microsoft_guid', ctx=Store())],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='microsoft_calendar.microsoft_guid', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertMicrosoftEventPatched',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='microsoft_id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='organizer', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='singleValueExtendedProperties', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='microsoft_id',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-01-15T08:00:00+00:00', kind=None),
                                                    Constant(value='Europe/London', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-01-15T18:00:00+00:00', kind=None),
                                                    Constant(value='Europe/London', kind=None),
                                                ],
                                            ),
                                            Constant(value='Event', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='content', kind=None),
                                                    Constant(value='contentType', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='text', kind=None),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='busy', kind=None),
                                            Dict(
                                                keys=[Constant(value='displayName', kind=None)],
                                                values=[Constant(value='', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='address', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='jean-luc@opoo.com', kind=None),
                                                            Constant(value='Test user Calendar', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value=0, kind=None),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='value', kind=None),
                                                        ],
                                                        values=[
                                                            BinOp(
                                                                left=Constant(value='String {%s} Name odoo_id', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='microsoft_guid', ctx=Load()),
                                                            ),
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='event', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='value', kind=None),
                                                        ],
                                                        values=[
                                                            BinOp(
                                                                left=Constant(value='String {%s} Name owner_odoo_id', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='microsoft_guid', ctx=Load()),
                                                            ),
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
                                                ctx=Load(),
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
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Name(id='patch', ctx=Load()),
                        attr='object',
                        ctx=Load(),
                    ),
                    args=[
                        Name(id='User', ctx=Load()),
                        Constant(value='_get_microsoft_calendar_token', kind=None),
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
