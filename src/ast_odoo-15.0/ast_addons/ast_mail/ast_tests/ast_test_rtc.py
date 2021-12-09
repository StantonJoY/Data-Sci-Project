Module(
    body=[
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[alias(name='MailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='users', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestChannelInternals',
            bases=[Name(id='MailCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_join_call',
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
                            value=Constant(value='Join call should remove existing sessions, remove invitation, create a new session, and return data.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_create',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Constant(value='Test Channel', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel.rtc.session/ended', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='sessionId', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                            attr='rtc_session_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                                                            attr='rtc_session_ids',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='isCameraOn', kind=None),
                                                                                                    Constant(value='isDeaf', kind=None),
                                                                                                    Constant(value='isMuted', kind=None),
                                                                                                    Constant(value='isScreenSharingOn', kind=None),
                                                                                                    Constant(value='partner', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    BinOp(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='channel_partner', ctx=Load()),
                                                                                                                attr='rtc_session_ids',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='insert', kind=None),
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='id', kind=None),
                                                                                                                            Constant(value='name', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Attribute(
                                                                                                                                value=Attribute(
                                                                                                                                    value=Attribute(
                                                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                                                        attr='user_employee',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    attr='partner_id',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Constant(value='Ernest Employee', kind=None),
                                                                                                                        ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner', ctx=Load()),
                                            attr='_rtc_join_call',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                                    Name(id='res', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='iceServers', kind=None),
                                            Constant(value='rtcSessions', kind=None),
                                            Constant(value='sessionId', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='insert', kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='isCameraOn', kind=None),
                                                                            Constant(value='isDeaf', kind=None),
                                                                            Constant(value='isMuted', kind=None),
                                                                            Constant(value='isScreenSharingOn', kind=None),
                                                                            Constant(value='partner', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='channel_partner', ctx=Load()),
                                                                                    attr='rtc_session_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            Constant(value=False, kind=None),
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='insert', kind=None),
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='name', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='user_employee',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value='Ernest Employee', kind=None),
                                                                                                ],
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
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='insert-and-unlink', kind=None),
                                                            List(
                                                                elts=[
                                                                    Dict(
                                                                        keys=[Constant(value='id', kind=None)],
                                                                        values=[
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='channel_partner', ctx=Load()),
                                                                                        attr='rtc_session_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                        ],
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
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='channel_partner', ctx=Load()),
                                                    attr='rtc_session_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_10_start_call_in_chat_should_invite_all_members_to_call',
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
                            targets=[Name(id='test_user', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test User', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='channel_get',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='user_employee',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='test_user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='last_rtc_session_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='rtc_session_ids',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_leave_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='isCameraOn', kind=None),
                                                                                                    Constant(value='isDeaf', kind=None),
                                                                                                    Constant(value='isMuted', kind=None),
                                                                                                    Constant(value='isScreenSharingOn', kind=None),
                                                                                                    Constant(value='partner', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    BinOp(
                                                                                                        left=Name(id='last_rtc_session_id', ctx=Load()),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='insert', kind=None),
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='id', kind=None),
                                                                                                                            Constant(value='name', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Attribute(
                                                                                                                                value=Attribute(
                                                                                                                                    value=Attribute(
                                                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                                                        attr='user_employee',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    attr='partner_id',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Constant(value='Ernest Employee', kind=None),
                                                                                                                        ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedPartners', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='name', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='test_user', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value='Test User', kind=None),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner', ctx=Load()),
                                            attr='_rtc_join_call',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='invitedGuests', kind=None),
                                    Name(id='res', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='invitedPartners', kind=None),
                                    Name(id='res', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='invitedPartners', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='insert', kind=None),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='test_user', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='Test User', kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_11_start_call_in_group_should_invite_all_members_to_call',
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
                            targets=[Name(id='test_user', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test User', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_guest', ctx=Store())],
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
                                                slice=Constant(value='mail.guest', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Guest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='user_employee',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='test_user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='guest_ids',
                                        value=Attribute(
                                            value=Name(id='test_guest', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='last_rtc_session_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='rtc_session_ids',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_leave_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.guest', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_guest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='isCameraOn', kind=None),
                                                                                                    Constant(value='isDeaf', kind=None),
                                                                                                    Constant(value='isMuted', kind=None),
                                                                                                    Constant(value='isScreenSharingOn', kind=None),
                                                                                                    Constant(value='partner', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    BinOp(
                                                                                                        left=Name(id='last_rtc_session_id', ctx=Load()),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='insert', kind=None),
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='id', kind=None),
                                                                                                                            Constant(value='name', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Attribute(
                                                                                                                                value=Attribute(
                                                                                                                                    value=Attribute(
                                                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                                                        attr='user_employee',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    attr='partner_id',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Constant(value='Ernest Employee', kind=None),
                                                                                                                        ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='isCameraOn', kind=None),
                                                                                                    Constant(value='isDeaf', kind=None),
                                                                                                    Constant(value='isMuted', kind=None),
                                                                                                    Constant(value='isScreenSharingOn', kind=None),
                                                                                                    Constant(value='partner', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    BinOp(
                                                                                                        left=Name(id='last_rtc_session_id', ctx=Load()),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='insert', kind=None),
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='id', kind=None),
                                                                                                                            Constant(value='name', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Attribute(
                                                                                                                                value=Attribute(
                                                                                                                                    value=Attribute(
                                                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                                                        attr='user_employee',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    attr='partner_id',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Constant(value='Ernest Employee', kind=None),
                                                                                                                        ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedGuests', kind=None),
                                                                    Constant(value='invitedPartners', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='name', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='test_guest', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value='Test Guest', kind=None),
                                                                                                ],
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
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='name', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='test_user', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value='Test User', kind=None),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner', ctx=Load()),
                                            attr='_rtc_join_call',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='invitedGuests', kind=None),
                                    Name(id='res', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='invitedGuests', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='insert', kind=None),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='test_guest', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='Test Guest', kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='invitedPartners', kind=None),
                                    Name(id='res', ctx=Load()),
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
                                    Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='invitedPartners', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='insert', kind=None),
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='test_user', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='Test User', kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_20_join_call_should_cancel_pending_invitations',
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
                            targets=[Name(id='test_user', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test User', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_guest', ctx=Store())],
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
                                                slice=Constant(value='mail.guest', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Guest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='user_employee',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='test_user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='guest_ids',
                                        value=Attribute(
                                            value=Name(id='test_guest', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner_test_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='test_user', ctx=Load()),
                                                    attr='partner_id',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[Constant(value='unlink', kind=None)],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedPartners', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='test_user', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='isCameraOn', kind=None),
                                                                                                    Constant(value='isDeaf', kind=None),
                                                                                                    Constant(value='isMuted', kind=None),
                                                                                                    Constant(value='isScreenSharingOn', kind=None),
                                                                                                    Constant(value='partner', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    BinOp(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='channel_partner', ctx=Load()),
                                                                                                                attr='rtc_session_ids',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='insert', kind=None),
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='id', kind=None),
                                                                                                                            Constant(value='name', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Attribute(
                                                                                                                                value=Attribute(
                                                                                                                                    value=Name(id='test_user', ctx=Load()),
                                                                                                                                    attr='partner_id',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Constant(value='Test User', kind=None),
                                                                                                                        ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner_test_user', ctx=Load()),
                                            attr='_rtc_join_call',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner_test_guest', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='guest_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='test_guest', ctx=Load())],
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.guest', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_guest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[Constant(value='unlink', kind=None)],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedGuests', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='test_guest', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='isCameraOn', kind=None),
                                                                                                    Constant(value='isDeaf', kind=None),
                                                                                                    Constant(value='isMuted', kind=None),
                                                                                                    Constant(value='isScreenSharingOn', kind=None),
                                                                                                    Constant(value='guest', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    BinOp(
                                                                                                        left=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='channel_partner', ctx=Load()),
                                                                                                                attr='rtc_session_ids',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        op=Add(),
                                                                                                        right=Constant(value=2, kind=None),
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    Constant(value=False, kind=None),
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Tuple(
                                                                                                                elts=[
                                                                                                                    Constant(value='insert', kind=None),
                                                                                                                    Dict(
                                                                                                                        keys=[
                                                                                                                            Constant(value='id', kind=None),
                                                                                                                            Constant(value='name', kind=None),
                                                                                                                        ],
                                                                                                                        values=[
                                                                                                                            Attribute(
                                                                                                                                value=Name(id='test_guest', ctx=Load()),
                                                                                                                                attr='id',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            Constant(value='Test Guest', kind=None),
                                                                                                                        ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner_test_guest', ctx=Load()),
                                            attr='_rtc_join_call',
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
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_21_leave_call_should_cancel_pending_invitations',
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
                            targets=[Name(id='test_user', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test User', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_guest', ctx=Store())],
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
                                                slice=Constant(value='mail.guest', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Guest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='user_employee',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='test_user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='guest_ids',
                                        value=Attribute(
                                            value=Name(id='test_guest', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner_test_user', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='test_user', ctx=Load()),
                                                    attr='partner_id',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[Constant(value='unlink', kind=None)],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedPartners', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='test_user', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner_test_user', ctx=Load()),
                                            attr='_rtc_leave_call',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner_test_guest', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='guest_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='test_guest', ctx=Load())],
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.guest', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_guest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[Constant(value='unlink', kind=None)],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedGuests', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='test_guest', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner_test_guest', ctx=Load()),
                                            attr='_rtc_leave_call',
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
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_25_lone_call_participant_leaving_call_should_cancel_pending_invitations',
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
                            targets=[Name(id='test_user', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test User', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_guest', ctx=Store())],
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
                                                slice=Constant(value='mail.guest', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Guest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=BinOp(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='user_employee',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='test_user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
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
                                    value=Name(id='channel', ctx=Load()),
                                    attr='add_members',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='guest_ids',
                                        value=Attribute(
                                            value=Name(id='test_guest', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.guest', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_guest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel.rtc.session/ended', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='sessionId', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                            attr='rtc_session_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[Constant(value='unlink', kind=None)],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[Constant(value='unlink', kind=None)],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedGuests', kind=None),
                                                                    Constant(value='invitedPartners', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='test_guest', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='test_user', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                                                            attr='rtc_session_ids',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner', ctx=Load()),
                                            attr='_rtc_leave_call',
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
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_30_add_members_while_in_call_should_invite_new_members_to_call',
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
                            targets=[Name(id='test_user', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='login', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test User', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_guest', ctx=Store())],
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
                                                slice=Constant(value='mail.guest', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Guest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_employee',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.guest', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_guest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='test_user', ctx=Load()),
                                                                    attr='partner_id',
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='id', kind=None),
                                                                                            Constant(value='isCameraOn', kind=None),
                                                                                            Constant(value='isDeaf', kind=None),
                                                                                            Constant(value='isMuted', kind=None),
                                                                                            Constant(value='isScreenSharingOn', kind=None),
                                                                                            Constant(value='partner', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='channel_partner', ctx=Load()),
                                                                                                    attr='rtc_session_ids',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                            List(
                                                                                                elts=[
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='insert', kind=None),
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='id', kind=None),
                                                                                                                    Constant(value='name', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Attribute(
                                                                                                                        value=Attribute(
                                                                                                                            value=Attribute(
                                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                                attr='user_employee',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            attr='partner_id',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='id',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    Constant(value='Ernest Employee', kind=None),
                                                                                                                ],
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
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcInvitingSession', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Constant(value='id', kind=None),
                                                                                            Constant(value='isCameraOn', kind=None),
                                                                                            Constant(value='isDeaf', kind=None),
                                                                                            Constant(value='isMuted', kind=None),
                                                                                            Constant(value='isScreenSharingOn', kind=None),
                                                                                            Constant(value='partner', kind=None),
                                                                                        ],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='channel_partner', ctx=Load()),
                                                                                                    attr='rtc_session_ids',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value=False, kind=None),
                                                                                            List(
                                                                                                elts=[
                                                                                                    Tuple(
                                                                                                        elts=[
                                                                                                            Constant(value='insert', kind=None),
                                                                                                            Dict(
                                                                                                                keys=[
                                                                                                                    Constant(value='id', kind=None),
                                                                                                                    Constant(value='name', kind=None),
                                                                                                                ],
                                                                                                                values=[
                                                                                                                    Attribute(
                                                                                                                        value=Attribute(
                                                                                                                            value=Attribute(
                                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                                attr='user_employee',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            attr='partner_id',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='id',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    Constant(value='Ernest Employee', kind=None),
                                                                                                                ],
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
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/insert', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='invitedGuests', kind=None),
                                                                    Constant(value='invitedPartners', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='name', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='test_guest', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value='Test Guest', kind=None),
                                                                                                ],
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
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[
                                                                                                    Constant(value='id', kind=None),
                                                                                                    Constant(value='name', kind=None),
                                                                                                ],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='test_user', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Constant(value='Test User', kind=None),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel', ctx=Load()),
                                            attr='add_members',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='test_user', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='guest_ids',
                                                value=Attribute(
                                                    value=Name(id='test_guest', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='invite_to_rtc_call',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_40_leave_call_should_remove_existing_sessions_of_user_in_channel_and_return_data',
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
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_employee',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel.rtc.session/ended', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='sessionId', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                            attr='rtc_session_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                                                            attr='rtc_session_ids',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner', ctx=Load()),
                                            attr='_rtc_leave_call',
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
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_50_garbage_collect_should_remove_old_sessions_and_notify_data',
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
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_employee',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
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
                                        value=Name(id='channel_partner', ctx=Load()),
                                        attr='rtc_session_ids',
                                        ctx=Load(),
                                    ),
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
                                        value=Name(id='channel_partner', ctx=Load()),
                                        attr='rtc_session_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='write_date', kind=None)],
                                        values=[
                                            BinOp(
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
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=2, kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='bus.bus', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel.rtc.session/ended', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='sessionId', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                            attr='rtc_session_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                                                            attr='rtc_session_ids',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
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
                                                        slice=Constant(value='mail.channel.rtc.session', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_gc_inactive_sessions',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                                        value=Name(id='channel_partner', ctx=Load()),
                                        attr='rtc_session_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_51_action_disconnect_should_remove_selected_session_and_notify_data',
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
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_employee',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='res.partner', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='user_employee',
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
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel.rtc.session/ended', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='sessionId', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                            attr='rtc_session_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='channel_partner', ctx=Load()),
                                                                                                            attr='rtc_session_ids',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='rtc_session_ids',
                                                ctx=Load(),
                                            ),
                                            attr='action_disconnect',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                                        value=Name(id='channel_partner', ctx=Load()),
                                        attr='rtc_session_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_60_rtc_sync_sessions_should_gc_and_return_outdated_and_active_sessions',
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
                            targets=[Name(id='channel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='mail.channel', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='create_group',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='partners_to',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_employee',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='channel_last_seen_partner_ids',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='channel_partner', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='channel_partner', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='user_employee',
                                                        ctx=Load(),
                                                    ),
                                                    attr='partner_id',
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
                        Assign(
                            targets=[Name(id='join_call_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='channel_partner', ctx=Load()),
                                    attr='_rtc_join_call',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_guest', ctx=Store())],
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
                                                slice=Constant(value='mail.guest', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Test Guest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_channel_partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.channel.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='guest_id', kind=None),
                                            Constant(value='channel_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_guest', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='channel', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='test_session', ctx=Store())],
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
                                                slice=Constant(value='mail.channel.rtc.session', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='channel_partner_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_channel_partner', ctx=Load()),
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
                                    value=Name(id='test_session', ctx=Load()),
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
                                    value=Name(id='test_session', ctx=Load()),
                                    attr='_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='write_date', kind=None)],
                                        values=[
                                            BinOp(
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
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=2, kind=None),
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
                        Assign(
                            targets=[Name(id='unused_ids', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value=9998, kind=None),
                                    Constant(value=9999, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='bus.bus', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.guest', kind=None),
                                                            Attribute(
                                                                value=Name(id='test_guest', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel', kind=None),
                                                            Attribute(
                                                                value=Name(id='channel', ctx=Load()),
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
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel.rtc.session/ended', kind=None),
                                                            Dict(
                                                                keys=[Constant(value='sessionId', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='test_session', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='payload', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mail.channel/rtc_sessions_update', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='rtcSessions', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='channel', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='insert-and-unlink', kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Dict(
                                                                                                keys=[Constant(value='id', kind=None)],
                                                                                                values=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='test_session', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='current_rtc_sessions', ctx=Store()),
                                                Name(id='outdated_rtc_sessions', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channel_partner', ctx=Load()),
                                            attr='_rtc_sync_sessions',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='check_rtc_session_ids',
                                                value=BinOp(
                                                    left=List(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='join_call_values', ctx=Load()),
                                                                slice=Constant(value='sessionId', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Name(id='unused_ids', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                                        value=Name(id='channel_partner', ctx=Load()),
                                        attr='rtc_session_ids',
                                        ctx=Load(),
                                    ),
                                    Name(id='current_rtc_sessions', ctx=Load()),
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
                                    Name(id='unused_ids', ctx=Load()),
                                    Attribute(
                                        value=Name(id='outdated_rtc_sessions', ctx=Load()),
                                        attr='ids',
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='outdated_rtc_sessions', ctx=Load()),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='employee', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.models.unlink', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='RTC', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
