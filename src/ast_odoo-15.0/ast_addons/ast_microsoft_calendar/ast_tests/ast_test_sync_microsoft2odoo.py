Module(
    body=[
        ImportFrom(
            module='odoo.addons.microsoft_calendar.utils.microsoft_calendar',
            names=[
                alias(name='MicrosoftCalendarService', asname=None),
                alias(name='MicrosoftEvent', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
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
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestSyncMicrosoft2Odoo',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                                    attr='recurrence_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAACyq4xQ=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Constant(value='2020-05-06T07:00:00Z', kind=None),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAACyq4xQ==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000D848B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAALKrjF"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAALKrjF"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAALKrjF"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='datetime_future',
                                    ctx=Store(),
                                ),
                            ],
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
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='now',
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
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='calendar.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[Name(id='events', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_new_microsoft_recurrence',
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Attribute(
                                value=Name(id='recurrence', ctx=Load()),
                                attr='calendar_event_ids',
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
                                args=[
                                    Name(id='recurrence', ctx=Load()),
                                    Constant(value='It should have created an recurrence', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='It should have created 3 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='events', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=16, kind=None),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=16, kind=None),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                    name='test_microsoft_recurrence_delete_one_event',
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
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Constant(value='It should keep the recurrence', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='It should keep 2 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                        ],
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
                    name='test_microsoft_recurrence_change_name_one_event',
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
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='originalStart', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ=="', kind=None),
                                            Constant(value='2020-05-06T08:01:32.4884797Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00807E40504874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='2020-05-04T14:30:00Z', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='exception', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA%3D&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Constant(value='It should have created an recurrence', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='It should have created 3 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                        ],
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
                    name='test_microsoft_recurrence_change_name_all_event',
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
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADIaZKQ==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpkp"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Constant(value='It should keep the recurrence', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='It should keep the 3 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                        ],
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
                    name='test_microsoft_recurrence_change_date_one_event',
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
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADIaZPA=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADIaZPA==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpk8"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='originalStart', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADIaZPA=="', kind=None),
                                            Constant(value='2020-05-06T08:41:52.1067613Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADIaZPA==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00807E40504874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='2020-05-04T14:30:00Z', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='exception', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA%3D&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T17:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMhpk8"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='special_event', ctx=Store())],
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
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
                                    Constant(value='It should have created an recurrence', kind=None),
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
                                    Name(id='special_event', ctx=Load()),
                                    Constant(value='It should have created an special event', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='It should have created 3 events', kind=None),
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
                                    Compare(
                                        left=Name(id='special_event', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='events', ctx=Load())],
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
                                        value=Name(id='recurrence', ctx=Load()),
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event_not_special', ctx=Store())],
                            value=BinOp(
                                left=Name(id='events', ctx=Load()),
                                op=Sub(),
                                right=Name(id='special_event', ctx=Load()),
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
                                            value=Name(id='event_not_special', ctx=Load()),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='event_not_special', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=16, kind=None),
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
                                            value=Name(id='event_not_special', ctx=Load()),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='event_not_special', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=16, kind=None),
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
                                        value=Name(id='special_event', ctx=Load()),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        value=Name(id='special_event', ctx=Load()),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
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
                    name='test_microsoft_recurrence_delete_first_event',
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
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADI/Bnw=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADI/Bnw==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8Gf"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8Gf"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Constant(value='It should have created an recurrence', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='It should left 2 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=16, kind=None),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADI/Bpg=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADI/Bpg==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8Gm"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T16:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
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
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Constant(value=1, kind=None),
                                    Constant(value='It should have created 1 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADI/Bqg=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADI/Bqg==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-05', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8Gq"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8Gq"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAACyy0xAAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T16:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8Gq"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T16:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
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
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Constant(value='It should have created 3 events', kind=None),
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
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event', kind=None),
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
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=30, kind=None),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=30, kind=None),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                        keywords=[],
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
                    name='test_microsoft_recurrence_split_recurrence',
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
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADI/Dig=="', kind=None),
                                            Constant(value='2020-05-06T07:03:49.1444085Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADI/Dig==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000874F057E7423D601000000000000000010000000C6918C4B44D2D84586351FEC8B1B7F8C', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='2020-05-03', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADI/Dkw=="', kind=None),
                                            Constant(value='2020-05-06T13:24:10.0507138Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADI/Dkw==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E008000000001A4457A0A923D601000000000000000010000000476AE6084FD718418262DA1AE3E41411', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAA&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAA', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T17:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2020-05-04', kind=None),
                                                            Constant(value='2020-05-06', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8OK"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX7vTsS0AARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-03T16:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8OT"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX774WtQAAAEYAAAJAcu19N72jSr9Rp1mE2xWABwBlLa4RUBXJToExnebpwea2AAACAQ0AAABlLa4RUBXJToExnebpwea2AAAADJIEKwAAABA=', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-04T17:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='originalStart', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='AllowNewTimeProposals', kind=None),
                                            Constant(value='IsDraft', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"ZS2uEVAVyU6BMZ3m6cHmtgAADI/Dkw=="', kind=None),
                                            Constant(value='2020-05-06T13:25:05.9240043Z', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='datetime_future',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ZS2uEVAVyU6BMZ3m6cHmtgAADI/Dkw==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00807E405051A4457A0A923D601000000000000000010000000476AE6084FD718418262DA1AE3E41411', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='2020-05-05T14:30:00Z', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAA', kind=None),
                                            Constant(value='busy', kind=None),
                                            Constant(value='exception', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAAEA%3D%3D&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8IdBHsAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='organizer', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-05T17:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                            Constant(value='outlook_7BA43549E5FD4413@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAABlLa4RUBXJToExnebpwea2AAAMj8OT"', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAA', kind=None),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoBUQAICADX8VBriIAARgAAAkBy7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAAEA==', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-06T14:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2020-05-06T17:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrence_1', ctx=Store())],
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                        Assign(
                            targets=[Name(id='recurrence_2', ctx=Store())],
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAAMkgQrAAAA', kind=None),
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
                            targets=[Name(id='events_1', ctx=Store())],
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
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence_1', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events_2', ctx=Store())],
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
                                                    Constant(value='recurrence_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='recurrence_2', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='start asc', kind=None),
                                    ),
                                ],
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
                                    Name(id='recurrence_1', ctx=Load()),
                                    Constant(value='It should have created an recurrence', kind=None),
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
                                    Name(id='recurrence_2', ctx=Load()),
                                    Constant(value='It should have created an recurrence', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events_1', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='It should left 1 event', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='events_2', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='It should have created 3 events', kind=None),
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
                                        value=Name(id='recurrence_1', ctx=Load()),
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events_1', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                        value=Name(id='recurrence_2', ctx=Load()),
                                        attr='base_event_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='events_2', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
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
                                        func=Attribute(
                                            value=Name(id='events_1', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[Constant(value='My recurrent event', kind=None)],
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
                                        func=Attribute(
                                            value=Name(id='events_2', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='My recurrent event', kind=None),
                                            Constant(value='My recurrent event 2', kind=None),
                                            Constant(value='My recurrent event', kind=None),
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
                                            value=Name(id='events_1', ctx=Load()),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='events_1', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=16, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='events_2', ctx=Load()),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='events_2', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=4, kind=None),
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
                                            value=Name(id='events_2', ctx=Load()),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='events_2', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=5, kind=None),
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
                                            value=Name(id='events_2', ctx=Load()),
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
                                            Constant(value=5, kind=None),
                                            Constant(value=6, kind=None),
                                            Constant(value=14, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Name(id='events_2', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2020, kind=None),
                                            Constant(value=5, kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_microsoft_recurrence_delete',
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                        Assign(
                            targets=[Name(id='event_ids', ctx=Store())],
                            value=Attribute(
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
                                                        Constant(value='recurrence_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Name(id='recurrence_id', ctx=Load()),
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
                                    keywords=[
                                        keyword(
                                            arg='order',
                                            value=Constant(value='start asc', kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='@removed', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='AQ8PojGtrADQATM3ZmYAZS0yY2MAMC00MDg1LTAwAi0wMAoARgAAA0By7X03vaNKv1GnWYTbFYAHAGUtrhFQFclOgTGd5unB5rYAAAIBDQAAAGUtrhFQFclOgTGd5unB5rYAAAALLLTEAAAA', kind=None),
                                            Dict(
                                                keys=[Constant(value='reason', kind=None)],
                                                values=[Constant(value='deleted', kind=None)],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
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
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='event_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
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
                                    Name(id='recurrence', ctx=Load()),
                                    Constant(value='It should remove recurrence', kind=None),
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
                                    Name(id='events', ctx=Load()),
                                    Constant(value='It should remove all events', kind=None),
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
                    name='test_attendees_must_have_email',
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
                            value=Constant(value="\n        Synching with a partner without mail raises a ValidationError because Microsoft don't accept attendees without one.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='MicrosoftCal', ctx=Store())],
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='SuperPartner', kind=None)],
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
                                        ],
                                        values=[
                                            Constant(value='SuperEvent', kind=None),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=11, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='datetime', ctx=Load()),
                                                args=[
                                                    Constant(value=2020, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=13, kind=None),
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='_sync_odoo2microsoft',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='MicrosoftCal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cancel_occurence_of_recurrent_event',
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
                            value=Constant(value=' The user is invited to a recurrent event. When synced, all events are present, there are three occurrences:\n            - 07/15/2021, 15:00-15:30\n            - 07/16/2021, 15:00-15:30\n            - 07/17/2021, 15:00-15:30\n        Then, the organizer cancels the second occurrence -> The latter should not be displayed anymore\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='microsoft_id', ctx=Store())],
                            value=Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgBGAAADZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAA=', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_sync_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='transactionId', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='allowNewTimeProposals', kind=None),
                                            Constant(value='OccurrenceId', kind=None),
                                            Constant(value='isDraft', kind=None),
                                            Constant(value='hideAttendees', kind=None),
                                            Constant(value='CalendarEventClassifications', kind=None),
                                            Constant(value='AutoRoomBookingOptions', kind=None),
                                            Constant(value='onlineMeeting', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"pynKRnkCyUmnqILQHcLZEQAABElcNQ=="', kind=None),
                                            Constant(value='2021-07-15T14:47:40.2996962Z', kind=None),
                                            Constant(value='2021-07-15T14:47:40.3783507Z', kind=None),
                                            Constant(value='pynKRnkCyUmnqILQHcLZEQAABElcNQ==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=None, kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000B35B3B5A8879D70100000000000000001000000008A0949F4EC0A1479E4ED178D87EF679', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='Recurrent Event 1646', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='tentative', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgBGAAADZ59RIxdyh0Kt%2FMXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAA%3D&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='notResponded', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2021-07-15', kind=None),
                                                            Constant(value='2021-07-17', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='status', kind=None),
                                                            Constant(value='emailAddress', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='response', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='none', kind=None),
                                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='address', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Odoo02 Outlook02', kind=None),
                                                                    Constant(value='odoo_bf_user02@outlook.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='status', kind=None),
                                                            Constant(value='emailAddress', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='response', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='none', kind=None),
                                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='address', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Odoo01 Outlook01', kind=None),
                                                                    Constant(value='odoo_bf_user01@outlook.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Odoo02 Outlook02', kind=None),
                                                            Constant(value='odoo_bf_user02@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAACnKcpGeQLJSaeogtAdwtkRAAAESVw1"', kind=None),
                                            BinOp(
                                                left=Constant(value='%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='microsoft_id', ctx=Load()),
                                            ),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlHI305wABGAAACZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAACnKcpGeQLJSaeogtAdwtkRAAAESVw1"', kind=None),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlH7KejgABGAAACZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-16T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-16T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAACnKcpGeQLJSaeogtAdwtkRAAAESVw1"', kind=None),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlItdINQABGAAACZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-17T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-17T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='second_sync_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='transactionId', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='allowNewTimeProposals', kind=None),
                                            Constant(value='OccurrenceId', kind=None),
                                            Constant(value='isDraft', kind=None),
                                            Constant(value='hideAttendees', kind=None),
                                            Constant(value='CalendarEventClassifications', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='recurrence', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"pynKRnkCyUmnqILQHcLZEQAABElcUw=="', kind=None),
                                            Constant(value='2021-07-15T14:47:40.2996962Z', kind=None),
                                            Constant(value='2021-07-15T14:51:25.2560888Z', kind=None),
                                            Constant(value='pynKRnkCyUmnqILQHcLZEQAABElcUw==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=None, kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00800000000B35B3B5A8879D70100000000000000001000000008A0949F4EC0A1479E4ED178D87EF679', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='Recurrent Event 1646', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value='tentative', kind=None),
                                            Constant(value='seriesMaster', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgBGAAADZ59RIxdyh0Kt%2FMXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAA%3D&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(elts=[], ctx=Load()),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='notResponded', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            Dict(
                                                keys=[
                                                    Constant(value='pattern', kind=None),
                                                    Constant(value='range', kind=None),
                                                ],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='interval', kind=None),
                                                            Constant(value='month', kind=None),
                                                            Constant(value='dayOfMonth', kind=None),
                                                            Constant(value='firstDayOfWeek', kind=None),
                                                            Constant(value='index', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='daily', kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Constant(value='sunday', kind=None),
                                                            Constant(value='first', kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='startDate', kind=None),
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='recurrenceTimeZone', kind=None),
                                                            Constant(value='numberOfOccurrences', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='endDate', kind=None),
                                                            Constant(value='2021-07-15', kind=None),
                                                            Constant(value='2021-07-17', kind=None),
                                                            Constant(value='Romance Standard Time', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='status', kind=None),
                                                            Constant(value='emailAddress', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='response', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='none', kind=None),
                                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='address', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Odoo02 Outlook02', kind=None),
                                                                    Constant(value='odoo_bf_user02@outlook.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='status', kind=None),
                                                            Constant(value='emailAddress', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='response', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='none', kind=None),
                                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='address', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Odoo01 Outlook01', kind=None),
                                                                    Constant(value='odoo_bf_user01@outlook.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Odoo02 Outlook02', kind=None),
                                                            Constant(value='odoo_bf_user02@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAACnKcpGeQLJSaeogtAdwtkRAAAESVxT"', kind=None),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlHI305wABGAAACZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-15T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='createdDateTime', kind=None),
                                            Constant(value='lastModifiedDateTime', kind=None),
                                            Constant(value='changeKey', kind=None),
                                            Constant(value='categories', kind=None),
                                            Constant(value='transactionId', kind=None),
                                            Constant(value='originalStartTimeZone', kind=None),
                                            Constant(value='originalEndTimeZone', kind=None),
                                            Constant(value='iCalUId', kind=None),
                                            Constant(value='reminderMinutesBeforeStart', kind=None),
                                            Constant(value='isReminderOn', kind=None),
                                            Constant(value='hasAttachments', kind=None),
                                            Constant(value='subject', kind=None),
                                            Constant(value='bodyPreview', kind=None),
                                            Constant(value='importance', kind=None),
                                            Constant(value='sensitivity', kind=None),
                                            Constant(value='originalStart', kind=None),
                                            Constant(value='isAllDay', kind=None),
                                            Constant(value='isCancelled', kind=None),
                                            Constant(value='isOrganizer', kind=None),
                                            Constant(value='IsRoomRequested', kind=None),
                                            Constant(value='AutoRoomBookingStatus', kind=None),
                                            Constant(value='responseRequested', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='showAs', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='webLink', kind=None),
                                            Constant(value='onlineMeetingUrl', kind=None),
                                            Constant(value='isOnlineMeeting', kind=None),
                                            Constant(value='onlineMeetingProvider', kind=None),
                                            Constant(value='allowNewTimeProposals', kind=None),
                                            Constant(value='OccurrenceId', kind=None),
                                            Constant(value='isDraft', kind=None),
                                            Constant(value='hideAttendees', kind=None),
                                            Constant(value='CalendarEventClassifications', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='responseStatus', kind=None),
                                            Constant(value='body', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='locations', kind=None),
                                            Constant(value='attendees', kind=None),
                                            Constant(value='organizer', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"pynKRnkCyUmnqILQHcLZEQAABElcUw=="', kind=None),
                                            Constant(value='2021-07-15T14:51:25.1366139Z', kind=None),
                                            Constant(value='2021-07-15T14:51:25.136614Z', kind=None),
                                            Constant(value='pynKRnkCyUmnqILQHcLZEQAABElcUw==', kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value=None, kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='Romance Standard Time', kind=None),
                                            Constant(value='040000008200E00074C5B7101A82E00807E50710B35B3B5A8879D70100000000000000001000000008A0949F4EC0A1479E4ED178D87EF679', kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='Canceled: Recurrent Event 1646', kind=None),
                                            Constant(value='', kind=None),
                                            Constant(value='high', kind=None),
                                            Constant(value='normal', kind=None),
                                            Constant(value='2021-07-16T15:00:00Z', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='None', kind=None),
                                            Constant(value=True, kind=None),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Constant(value='free', kind=None),
                                            Constant(value='exception', kind=None),
                                            Constant(value='https://outlook.live.com/owa/?itemid=AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlH7KejgABGAAACZ59RIxdyh0Kt%2FMXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ&exvsurl=1&path=/calendar/item', kind=None),
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='unknown', kind=None),
                                            Constant(value=True, kind=None),
                                            BinOp(
                                                left=Constant(value='OID.%s.2021-07-16', kind=None),
                                                op=Mod(),
                                                right=Name(id='microsoft_id', ctx=Load()),
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            List(elts=[], ctx=Load()),
                                            Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlH7KejgABGAAACZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='response', kind=None),
                                                    Constant(value='time', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='notResponded', kind=None),
                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='contentType', kind=None),
                                                    Constant(value='content', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='html', kind=None),
                                                    Constant(value='<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n<meta name="Generator" content="Microsoft Exchange Server">\r\n<!-- converted from text -->\r\n<style><!-- .EmailQuote { margin-left: 1pt; padding-left: 4pt; border-left: #800000 2px solid; } --></style></head>\r\n<body>\r\n<font size="2"><span style="font-size:11pt;"><div class="PlainText">&nbsp;</div></span></font>\r\n</body>\r\n</html>\r\n', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-16T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-16T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='displayName', kind=None),
                                                    Constant(value='locationType', kind=None),
                                                    Constant(value='uniqueIdType', kind=None),
                                                    Constant(value='address', kind=None),
                                                    Constant(value='coordinates', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='default', kind=None),
                                                    Constant(value='unknown', kind=None),
                                                    Dict(keys=[], values=[]),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='status', kind=None),
                                                            Constant(value='emailAddress', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='response', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='none', kind=None),
                                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='address', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Odoo02 Outlook02', kind=None),
                                                                    Constant(value='odoo_bf_user02@outlook.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='status', kind=None),
                                                            Constant(value='emailAddress', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='required', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='response', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='none', kind=None),
                                                                    Constant(value='0001-01-01T00:00:00Z', kind=None),
                                                                ],
                                                            ),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='address', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Odoo01 Outlook01', kind=None),
                                                                    Constant(value='odoo_bf_user01@outlook.com', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='emailAddress', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='address', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='Odoo02 Outlook02', kind=None),
                                                            Constant(value='odoo_bf_user02@outlook.com', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='@odata.type', kind=None),
                                            Constant(value='@odata.etag', kind=None),
                                            Constant(value='seriesMasterId', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='end', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#microsoft.graph.event', kind=None),
                                            Constant(value='W/"DwAAABYAAACnKcpGeQLJSaeogtAdwtkRAAAESVxT"', kind=None),
                                            Name(id='microsoft_id', ctx=Load()),
                                            Constant(value='occurrence', kind=None),
                                            Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgFRAAgIANlItdINQABGAAACZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAAQ', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-17T15:00:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='dateTime', kind=None),
                                                    Constant(value='timeZone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='2021-07-17T15:30:00.0000000', kind=None),
                                                    Constant(value='UTC', kind=None),
                                                ],
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
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
                                        args=[Name(id='first_sync_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recurrent_event', ctx=Store())],
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
                                                    Constant(value='microsoft_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='AQMkADAwATM3ZmYAZS0zZmMyLWYxYjQtMDACLTAwCgBGAAADZ59RIxdyh0Kt-MXfyCpfwAcApynKRnkCyUmnqILQHcLZEQAAAgENAAAApynKRnkCyUmnqILQHcLZEQAAAARKsSQAAAA=', kind=None),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='recurrent_event', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='recurrent_event', ctx=Load()),
                                    attr='write_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2021, kind=None),
                                    Constant(value=7, kind=None),
                                    Constant(value=15, kind=None),
                                    Constant(value=14, kind=None),
                                    Constant(value=0, kind=None),
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
                                        slice=Constant(value='calendar.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sync_microsoft2odoo',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='MicrosoftEvent', ctx=Load()),
                                        args=[Name(id='second_sync_values', ctx=Load())],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='recurrent_event', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='recurrent_event', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
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
                                            Constant(value=7, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=15, kind=None),
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
                                            value=Attribute(
                                                value=Name(id='recurrent_event', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=30, kind=None),
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
                                            value=Attribute(
                                                value=Name(id='recurrent_event', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
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
                                            Constant(value=7, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=15, kind=None),
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
                                            value=Attribute(
                                                value=Name(id='recurrent_event', ctx=Load()),
                                                attr='calendar_event_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='stop',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='datetime', ctx=Load()),
                                        args=[
                                            Constant(value=2021, kind=None),
                                            Constant(value=7, kind=None),
                                            Constant(value=17, kind=None),
                                            Constant(value=15, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                        keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
