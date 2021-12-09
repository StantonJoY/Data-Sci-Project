Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='html_escape', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MailChannel',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Chat Session\n        Reprensenting a conversation between users.\n        It extends the base method for anonymous usage.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.channel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='mail.channel', kind=None),
                            Constant(value='rating.mixin', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='anonymous_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Anonymous Name', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='channel_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='livechat', kind=None),
                                                Constant(value='Livechat Conversation', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='livechat_active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is livechat ongoing?', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Livechat session is active until visitor leave the conversation.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='livechat_channel_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='im_livechat.channel', kind=None),
                            Constant(value='Channel', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='livechat_operator_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Operator', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Operator for this specific channel', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.country', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Country', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Country of the visitor of the channel', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='livechat_operator_id', kind=None),
                                    Constant(value="CHECK((channel_type = 'livechat' and livechat_operator_id is not null) or (channel_type != 'livechat'))", kind=None),
                                    Constant(value='Livechat Operator ID is required for a channel of type livechat.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_chat',
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
                                        args=[
                                            Name(id='MailChannel', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_is_chat',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='channel_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='livechat', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='is_chat',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
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
                    name='_channel_message_notifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='message_format', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' When a anonymous user create a mail.channel, the operator is not notify (to avoid massive polling when\n            clicking on livechat button). So when the anonymous person is sending its FIRST message, the channel header\n            should be added to the notification, since the user cannot be listining to the channel.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='livechat_channels', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='channel_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='livechat', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='other_channels', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='x', ctx=Load()),
                                                attr='channel_type',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='livechat', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notifications', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='MailChannel', ctx=Load()),
                                                Name(id='livechat_channels', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_channel_message_notifications',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='im_livechat_use_username',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='MailChannel', ctx=Load()),
                                                Name(id='other_channels', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_channel_message_notifications',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='message', ctx=Load()),
                                        Name(id='message_format', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='channel', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='channel', ctx=Load()),
                                                    attr='channel_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='livechat', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='channel', ctx=Load()),
                                                    attr='public',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='private', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
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
                                                                value=Name(id='channel', ctx=Load()),
                                                                attr='uuid',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='mail.channel/new_message', kind=None),
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='notifications', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=2, kind=None),
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
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='message', ctx=Load()),
                                    attr='author_id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='unpinned_channel_partner', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                                                    args=[arg(arg='cp', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='cp', ctx=Load()),
                                                        attr='is_pinned',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='unpinned_channel_partner', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='unpinned_channel_partner', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='is_pinned', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='notifications', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_channel_channel_notifications',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='unpinned_channel_partner', ctx=Load()),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='partner_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='notifications', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='notifications', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_channel_fetch_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='last_id', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=20, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override to add the context of the livechat username.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='channel', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='channel_type',
                                        ctx=Load(),
                                    ),
                                    ops=[Eq()],
                                    comparators=[Constant(value='livechat', kind=None)],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='with_context',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='im_livechat_use_username',
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                ),
                                orelse=Name(id='self', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailChannel', ctx=Load()),
                                            Name(id='channel', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_channel_fetch_message',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='last_id',
                                        value=Name(id='last_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
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
                    name='channel_info',
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
                            value=Constant(value=" Extends the channel header by adding the livechat operator and the 'anonymous' profile\n            :rtype : list(dict)\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='channel_infos', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='channel_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channel_infos_dict', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='c', ctx=Load()),
                                                    slice=Constant(value='id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='c', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='c', ctx=Store()),
                                                iter=Name(id='channel_infos', ctx=Load()),
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
                        For(
                            target=Name(id='channel', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='channel', ctx=Load()),
                                            attr='channel_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='livechat', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='channel', ctx=Load()),
                                                attr='livechat_operator_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='channel', ctx=Load()),
                                                                            attr='livechat_operator_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='with_context',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='im_livechat_use_username',
                                                                            value=Constant(value=True, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                                attr='name_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='channel_infos_dict', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='channel', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='operator_pid', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Tuple(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='res', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=',', kind=None),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='channel_infos_dict', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='channel', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='livechat_visitor', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='channel', ctx=Load()),
                                                    attr='_channel_get_livechat_visitor_info',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='channel_infos_dict', ctx=Load()),
                                            attr='values',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_channel_get_livechat_visitor_info',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='channel_partner_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
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
                                attr='channel_partner_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=BinOp(
                                left=Name(id='channel_partner_ids', ctx=Load()),
                                op=Sub(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='livechat_operator_id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='partners', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partners', ctx=Store())],
                                    value=Name(id='channel_partner_ids', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='first_partner', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='partners', ctx=Load()),
                                    Subscript(
                                        value=Name(id='partners', ctx=Load()),
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
                                    Name(id='first_partner', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='first_partner', ctx=Load()),
                                                    attr='user_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='any', ctx=Load()),
                                                    args=[
                                                        GeneratorExp(
                                                            elt=Call(
                                                                func=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='_is_public',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='user', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Name(id='first_partner', ctx=Load()),
                                                                        attr='user_ids',
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
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='country', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            IfExp(
                                                test=Attribute(
                                                    value=Name(id='first_partner', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                body=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='first_partner', ctx=Load()),
                                                                attr='country_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            Attribute(
                                                value=Name(id='first_partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='first_partner', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='country', kind=None),
                                    Constant(value='id', kind=None),
                                    Constant(value='name', kind=None),
                                ],
                                values=[
                                    IfExp(
                                        test=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        body=Subscript(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name_get',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    Constant(value=False, kind=None),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='anonymous_name',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Visitor', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                    name='_channel_get_livechat_partner_name',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='livechat_operator_id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='channel_partner_ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partners', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='channel_partner_ids',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='livechat_operator_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='partners', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner_name', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='partner', ctx=Store()),
                                            iter=Name(id='partners', ctx=Load()),
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='partner_name', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='partner_name', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        AugAssign(
                                                            target=Name(id='partner_name', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Constant(value=', %s', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='partner_name', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Constant(value=' (%s)', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='country_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='partner_name', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='anonymous_name',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='anonymous_name',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Visitor', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_gc_empty_livechat_sessions',
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
                            targets=[Name(id='hours', ctx=Store())],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
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
                                    Constant(value="\n            SELECT id as id\n            FROM mail_channel C\n            WHERE NOT EXISTS (\n                SELECT *\n                FROM mail_message M\n                WHERE M.res_id = C.id AND m.model = 'mail.channel'\n            ) AND C.channel_type = 'livechat' AND livechat_channel_id IS NOT NULL AND\n                COALESCE(write_date, create_date, (now() at time zone 'UTC'))::timestamp\n                < ((now() at time zone 'UTC') - interval %s)", kind=None),
                                    Tuple(
                                        elts=[
                                            BinOp(
                                                left=Constant(value='%s hours', kind=None),
                                                op=Mod(),
                                                right=Name(id='hours', ctx=Load()),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='empty_channel_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='item', ctx=Load()),
                                    slice=Constant(value='id', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='item', ctx=Store()),
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
                                                attr='dictfetchall',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='empty_channel_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='autovacuum',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_execute_command_help_message_extra',
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
                            targets=[Name(id='msg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailChannel', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_execute_command_help_message_extra',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='msg', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='Type <b>:shortcut</b> to insert a canned response in your message.<br>', kind=None)],
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
                    name='execute_command_history',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
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
                                        slice=Constant(value='bus.bus', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_sendone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='uuid',
                                        ctx=Load(),
                                    ),
                                    Constant(value='im_livechat.history_command', kind=None),
                                    Dict(
                                        keys=[Constant(value='id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_history_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pid', annotation=None, type_comment=None),
                            arg(arg='page_history', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='message_body', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='No history found', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='page_history', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='html_links', ctx=Store())],
                                    value=ListComp(
                                        elt=BinOp(
                                            left=Constant(value='<li><a href="%s" target="_blank">%s</a></li>', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Name(id='html_escape', ctx=Load()),
                                                        args=[Name(id='page', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='html_escape', ctx=Load()),
                                                        args=[Name(id='page', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='page', ctx=Store()),
                                                iter=Name(id='page_history', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='message_body', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='<ul>%s</ul>', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value='', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='html_links', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_send_transient_message',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='message_body', ctx=Load()),
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
                    name='_get_visitor_leave_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='cancel', annotation=None, type_comment=None),
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
                        Return(
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Visitor has left the conversation.', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_close_livechat_session',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Set deactivate the livechat channel and notify (the operator) the reason of closing the session.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='livechat_active',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='livechat_active',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='author_id',
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
                                                        args=[Constant(value='base.partner_root', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='body',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_get_visitor_leave_message',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg=None,
                                                            value=Name(id='kwargs', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg='message_type',
                                                value=Constant(value='comment', kind=None),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
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
                    name='_rating_get_parent_field_name',
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
                            value=Constant(value='livechat_channel_id', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_email_livechat_transcript',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
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
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='render_context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='company', kind=None),
                                    Constant(value='channel', kind=None),
                                ],
                                values=[
                                    Name(id='company', ctx=Load()),
                                    Name(id='self', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='template', ctx=Store())],
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
                                args=[Constant(value='im_livechat.livechat_email_template', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='template', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='render_context', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Constant(value='ir.qweb', kind=None),
                                    ),
                                    keyword(
                                        arg='minimal_qcontext',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.render.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_replace_local_links',
                                    ctx=Load(),
                                ),
                                args=[Name(id='mail_body', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail', ctx=Store())],
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
                                                slice=Constant(value='mail.mail', kind=None),
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
                                            Constant(value='subject', kind=None),
                                            Constant(value='email_from', kind=None),
                                            Constant(value='author_id', kind=None),
                                            Constant(value='email_to', kind=None),
                                            Constant(value='body_html', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Conversation with %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='livechat_operator_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='catchall_formatted',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='email_formatted',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
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
                                            Name(id='email', ctx=Load()),
                                            Name(id='mail_body', ctx=Load()),
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
                                    value=Name(id='mail', ctx=Load()),
                                    attr='send',
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
