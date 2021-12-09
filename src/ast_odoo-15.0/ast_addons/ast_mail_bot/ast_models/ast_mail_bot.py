Module(
    body=[
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailBot',
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
                    value=Constant(value='mail.bot', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Bot', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_apply_logic',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='command', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Apply bot logic to generate an answer (or not) for the user\n        The logic will only be applied if odoobot is in a chat with a user or\n        if someone pinged odoobot.\n\n         :param record: the mail_thread (or mail_channel) where the user\n            message was posted/odoobot will answer.\n         :param values: msg_values of the message_post or other values needed by logic\n         :param command: the name of the called command if the logic is not triggered by a message_post\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='odoobot_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.partner_root', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='record', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='author_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='odoobot_id', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_bot_pinged',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_bot_in_private_channel',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='record', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='body', kind=None),
                                                                            Constant(value='', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='\xa0', kind='u'),
                                                                    Constant(value=' ', kind='u'),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='lower',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.!', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='answer', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_answer',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='body', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                            Name(id='command', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='answer', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_type', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='comment', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='subtype_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='subtype_id', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.model.data', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_xmlid_to_res_id',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='mail.mt_comment', kind=None)],
                                                        keywords=[],
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
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='mail_create_nosubscribe',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='answer', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='author_id',
                                                        value=Name(id='odoobot_id', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='message_type',
                                                        value=Name(id='message_type', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='subtype_id',
                                                        value=Name(id='subtype_id', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_get_answer',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='command', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='odoobot_state', ctx=Store())],
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
                                attr='odoobot_state',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_bot_in_private_channel',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='odoobot_state', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='onboarding_emoji', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_body_contains_emoji',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='body', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
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
                                                    attr='odoobot_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='onboarding_command', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
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
                                                    attr='odoobot_failed',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Great! 👍<br/>To access special commands, <b>start your sentence with</b> <span class="o_odoobot_command">/</span>. Try getting help.', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='onboarding_command', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='command', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='help', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
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
                                                            attr='odoobot_state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='onboarding_ping', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
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
                                                            attr='odoobot_failed',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Wow you are a natural!<br/>Ping someone with @username to grab their attention. <b>Try to ping me using</b> <span class="o_odoobot_command">@OdooBot</span> in a sentence.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='odoobot_state', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='onboarding_ping', kind=None)],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_is_bot_pinged',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
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
                                                                    attr='odoobot_state',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='onboarding_attachement', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
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
                                                                    attr='odoobot_failed',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Return(
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Yep, I am here! 🎉 <br/>Now, try <b>sending an attachment</b>, like a picture of your cute dog...', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='onboarding_attachement', kind=None)],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='attachment_ids', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
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
                                                                            attr='odoobot_state',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='idle', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
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
                                                                            attr='odoobot_failed',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=False, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Return(
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value="I am a simple bot, but if that's a dog, he is the cutest 😊 <br/>Congratulations, you finished this tour. You can now <b>close this chat window</b>. Enjoy discovering Odoo.", kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='odoobot_state', ctx=Load()),
                                                                                ops=[In()],
                                                                                comparators=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value=False, kind=None),
                                                                                            Constant(value='idle', kind=None),
                                                                                            Constant(value='not_initialized', kind=None),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Compare(
                                                                                left=Call(
                                                                                    func=Name(id='_', ctx=Load()),
                                                                                    args=[Constant(value='start the tour', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[In()],
                                                                                comparators=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='body', ctx=Load()),
                                                                                            attr='lower',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
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
                                                                                    attr='odoobot_state',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='onboarding_emoji', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                        Return(
                                                                            value=Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[Constant(value='To start, try to send me an emoji :)', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='idle', kind=None)],
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Name(id='body', ctx=Load()),
                                                                                        ops=[In()],
                                                                                        comparators=[
                                                                                            List(
                                                                                                elts=[
                                                                                                    Constant(value='❤️', kind=None),
                                                                                                    Call(
                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                        args=[Constant(value='i love you', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    Call(
                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                        args=[Constant(value='love', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[Constant(value="Aaaaaw that's really cute but, you know, bots don't work that way. You're too human for me! Let's keep it professional ❤️", kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Call(
                                                                                                    func=Name(id='_', ctx=Load()),
                                                                                                    args=[Constant(value='fuck', kind=None)],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                ops=[In()],
                                                                                                comparators=[Name(id='body', ctx=Load())],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Constant(value='fuck', kind=None),
                                                                                                ops=[In()],
                                                                                                comparators=[Name(id='body', ctx=Load())],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[
                                                                                        Return(
                                                                                            value=Call(
                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                args=[Constant(value="That's not nice! I'm a bot but I have feelings... 💔", kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=Or(),
                                                                                                values=[
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='_is_help_requested',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[Name(id='body', ctx=Load())],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    Compare(
                                                                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='idle', kind=None)],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Return(
                                                                                                    value=Call(
                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                        args=[Constant(value='Unfortunately, I\'m just a bot 😞 I don\'t understand! If you need help discovering our product, please check <a href="https://www.odoo.com/documentation" target="_blank">our documentation</a> or <a href="https://www.odoo.com/slides" target="_blank">our videos</a>.', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                If(
                                                                                                    test=Compare(
                                                                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value='onboarding_emoji', kind=None)],
                                                                                                    ),
                                                                                                    body=[
                                                                                                        Assign(
                                                                                                            targets=[
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
                                                                                                                    attr='odoobot_failed',
                                                                                                                    ctx=Store(),
                                                                                                                ),
                                                                                                            ],
                                                                                                            value=Constant(value=True, kind=None),
                                                                                                            type_comment=None,
                                                                                                        ),
                                                                                                        Return(
                                                                                                            value=Call(
                                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                                args=[Constant(value='Not exactly. To continue the tour, send an emoji: <b>type</b> <span class="o_odoobot_command">:)</span> and press enter.', kind=None)],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ),
                                                                                                    ],
                                                                                                    orelse=[
                                                                                                        If(
                                                                                                            test=Compare(
                                                                                                                left=Name(id='odoobot_state', ctx=Load()),
                                                                                                                ops=[Eq()],
                                                                                                                comparators=[Constant(value='onboarding_attachement', kind=None)],
                                                                                                            ),
                                                                                                            body=[
                                                                                                                Assign(
                                                                                                                    targets=[
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
                                                                                                                            attr='odoobot_failed',
                                                                                                                            ctx=Store(),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    value=Constant(value=True, kind=None),
                                                                                                                    type_comment=None,
                                                                                                                ),
                                                                                                                Return(
                                                                                                                    value=Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value='To <b>send an attachment</b>, click on the <i class="fa fa-paperclip" aria-hidden="true"></i> icon and select a file.', kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                ),
                                                                                                            ],
                                                                                                            orelse=[
                                                                                                                If(
                                                                                                                    test=Compare(
                                                                                                                        left=Name(id='odoobot_state', ctx=Load()),
                                                                                                                        ops=[Eq()],
                                                                                                                        comparators=[Constant(value='onboarding_command', kind=None)],
                                                                                                                    ),
                                                                                                                    body=[
                                                                                                                        Assign(
                                                                                                                            targets=[
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
                                                                                                                                    attr='odoobot_failed',
                                                                                                                                    ctx=Store(),
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            value=Constant(value=True, kind=None),
                                                                                                                            type_comment=None,
                                                                                                                        ),
                                                                                                                        Return(
                                                                                                                            value=Call(
                                                                                                                                func=Name(id='_', ctx=Load()),
                                                                                                                                args=[Constant(value='Not sure what you are doing. Please, type <span class="o_odoobot_command">/</span> and wait for the propositions. Select <span class="o_odoobot_command">help</span> and press enter', kind=None)],
                                                                                                                                keywords=[],
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                    orelse=[
                                                                                                                        If(
                                                                                                                            test=Compare(
                                                                                                                                left=Name(id='odoobot_state', ctx=Load()),
                                                                                                                                ops=[Eq()],
                                                                                                                                comparators=[Constant(value='onboarding_ping', kind=None)],
                                                                                                                            ),
                                                                                                                            body=[
                                                                                                                                Assign(
                                                                                                                                    targets=[
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
                                                                                                                                            attr='odoobot_failed',
                                                                                                                                            ctx=Store(),
                                                                                                                                        ),
                                                                                                                                    ],
                                                                                                                                    value=Constant(value=True, kind=None),
                                                                                                                                    type_comment=None,
                                                                                                                                ),
                                                                                                                                Return(
                                                                                                                                    value=Call(
                                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                                        args=[Constant(value='Sorry, I am not listening. To get someone\'s attention, <b>ping him</b>. Write <span class="o_odoobot_command">@OdooBot</span> and select me.', kind=None)],
                                                                                                                                        keywords=[],
                                                                                                                                    ),
                                                                                                                                ),
                                                                                                                            ],
                                                                                                                            orelse=[],
                                                                                                                        ),
                                                                                                                    ],
                                                                                                                ),
                                                                                                            ],
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                                Return(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='random', ctx=Load()),
                                                                                                            attr='choice',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            List(
                                                                                                                elts=[
                                                                                                                    Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value='I\'m not smart enough to answer your question.<br/>To follow my guide, ask: <span class="o_odoobot_command">start the tour</span>.', kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value='Hmmm...', kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value="I'm afraid I don't understand. Sorry!", kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    Call(
                                                                                                                        func=Name(id='_', ctx=Load()),
                                                                                                                        args=[Constant(value='Sorry I\'m sleepy. Or not! Maybe I\'m just trying to hide my unawareness of human language...<br/>I can show you features if you write: <span class="o_odoobot_command">start the tour</span>.', kind=None)],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                ],
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_body_contains_emoji',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='emoji_list', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='chain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=8986, kind=None),
                                            Constant(value=8988, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9193, kind=None),
                                            Constant(value=9204, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9208, kind=None),
                                            Constant(value=9211, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9642, kind=None),
                                            Constant(value=9644, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9723, kind=None),
                                            Constant(value=9727, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9728, kind=None),
                                            Constant(value=9733, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9748, kind=None),
                                            Constant(value=9750, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9762, kind=None),
                                            Constant(value=9764, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9774, kind=None),
                                            Constant(value=9776, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9784, kind=None),
                                            Constant(value=9787, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9800, kind=None),
                                            Constant(value=9812, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9823, kind=None),
                                            Constant(value=9825, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9829, kind=None),
                                            Constant(value=9831, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9854, kind=None),
                                            Constant(value=9856, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9874, kind=None),
                                            Constant(value=9880, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9883, kind=None),
                                            Constant(value=9885, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9888, kind=None),
                                            Constant(value=9890, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9898, kind=None),
                                            Constant(value=9900, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9904, kind=None),
                                            Constant(value=9906, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9917, kind=None),
                                            Constant(value=9919, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9924, kind=None),
                                            Constant(value=9926, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9939, kind=None),
                                            Constant(value=9941, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9961, kind=None),
                                            Constant(value=9963, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9968, kind=None),
                                            Constant(value=9974, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9975, kind=None),
                                            Constant(value=9979, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9992, kind=None),
                                            Constant(value=9994, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9994, kind=None),
                                            Constant(value=9996, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=9996, kind=None),
                                            Constant(value=9998, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=10035, kind=None),
                                            Constant(value=10037, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=10067, kind=None),
                                            Constant(value=10070, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=10083, kind=None),
                                            Constant(value=10085, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=10133, kind=None),
                                            Constant(value=10136, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=10548, kind=None),
                                            Constant(value=10550, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=11013, kind=None),
                                            Constant(value=11016, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=11035, kind=None),
                                            Constant(value=11037, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127344, kind=None),
                                            Constant(value=127346, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127377, kind=None),
                                            Constant(value=127387, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127462, kind=None),
                                            Constant(value=127488, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127489, kind=None),
                                            Constant(value=127491, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127538, kind=None),
                                            Constant(value=127547, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127568, kind=None),
                                            Constant(value=127570, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127744, kind=None),
                                            Constant(value=127777, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127780, kind=None),
                                            Constant(value=127789, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127789, kind=None),
                                            Constant(value=127792, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127792, kind=None),
                                            Constant(value=127798, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127799, kind=None),
                                            Constant(value=127869, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127870, kind=None),
                                            Constant(value=127872, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127872, kind=None),
                                            Constant(value=127892, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127894, kind=None),
                                            Constant(value=127896, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127897, kind=None),
                                            Constant(value=127900, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127902, kind=None),
                                            Constant(value=127904, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127904, kind=None),
                                            Constant(value=127941, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127942, kind=None),
                                            Constant(value=127947, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127947, kind=None),
                                            Constant(value=127951, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127951, kind=None),
                                            Constant(value=127956, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127956, kind=None),
                                            Constant(value=127968, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127968, kind=None),
                                            Constant(value=127985, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127987, kind=None),
                                            Constant(value=127990, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=127992, kind=None),
                                            Constant(value=128000, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128000, kind=None),
                                            Constant(value=128063, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128066, kind=None),
                                            Constant(value=128248, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128249, kind=None),
                                            Constant(value=128253, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128256, kind=None),
                                            Constant(value=128318, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128329, kind=None),
                                            Constant(value=128331, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128331, kind=None),
                                            Constant(value=128335, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128336, kind=None),
                                            Constant(value=128360, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128367, kind=None),
                                            Constant(value=128369, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128371, kind=None),
                                            Constant(value=128378, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128394, kind=None),
                                            Constant(value=128398, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128405, kind=None),
                                            Constant(value=128407, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128433, kind=None),
                                            Constant(value=128435, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128450, kind=None),
                                            Constant(value=128453, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128465, kind=None),
                                            Constant(value=128468, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128476, kind=None),
                                            Constant(value=128479, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128507, kind=None),
                                            Constant(value=128512, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128513, kind=None),
                                            Constant(value=128529, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128530, kind=None),
                                            Constant(value=128533, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128540, kind=None),
                                            Constant(value=128543, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128544, kind=None),
                                            Constant(value=128550, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128550, kind=None),
                                            Constant(value=128552, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128552, kind=None),
                                            Constant(value=128556, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128558, kind=None),
                                            Constant(value=128560, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128560, kind=None),
                                            Constant(value=128564, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128565, kind=None),
                                            Constant(value=128577, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128577, kind=None),
                                            Constant(value=128579, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128579, kind=None),
                                            Constant(value=128581, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128581, kind=None),
                                            Constant(value=128592, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128640, kind=None),
                                            Constant(value=128710, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128715, kind=None),
                                            Constant(value=128720, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128721, kind=None),
                                            Constant(value=128723, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128736, kind=None),
                                            Constant(value=128742, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128747, kind=None),
                                            Constant(value=128749, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128756, kind=None),
                                            Constant(value=128759, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=128759, kind=None),
                                            Constant(value=128761, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129296, kind=None),
                                            Constant(value=129305, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129305, kind=None),
                                            Constant(value=129311, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129312, kind=None),
                                            Constant(value=129320, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129320, kind=None),
                                            Constant(value=129328, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129329, kind=None),
                                            Constant(value=129331, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129331, kind=None),
                                            Constant(value=129339, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129340, kind=None),
                                            Constant(value=129343, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129344, kind=None),
                                            Constant(value=129350, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129351, kind=None),
                                            Constant(value=129356, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129357, kind=None),
                                            Constant(value=129360, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129360, kind=None),
                                            Constant(value=129375, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129375, kind=None),
                                            Constant(value=129388, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129388, kind=None),
                                            Constant(value=129393, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129395, kind=None),
                                            Constant(value=129399, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129404, kind=None),
                                            Constant(value=129408, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129408, kind=None),
                                            Constant(value=129413, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129413, kind=None),
                                            Constant(value=129426, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129426, kind=None),
                                            Constant(value=129432, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129432, kind=None),
                                            Constant(value=129443, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129456, kind=None),
                                            Constant(value=129466, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129473, kind=None),
                                            Constant(value=129475, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129488, kind=None),
                                            Constant(value=129511, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=129511, kind=None),
                                            Constant(value=129536, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value=9000, kind=None),
                                            Constant(value=9167, kind=None),
                                            Constant(value=9410, kind=None),
                                            Constant(value=9654, kind=None),
                                            Constant(value=9664, kind=None),
                                            Constant(value=9742, kind=None),
                                            Constant(value=9745, kind=None),
                                            Constant(value=9752, kind=None),
                                            Constant(value=9757, kind=None),
                                            Constant(value=9760, kind=None),
                                            Constant(value=9766, kind=None),
                                            Constant(value=9770, kind=None),
                                            Constant(value=9792, kind=None),
                                            Constant(value=9794, kind=None),
                                            Constant(value=9827, kind=None),
                                            Constant(value=9832, kind=None),
                                            Constant(value=9851, kind=None),
                                            Constant(value=9881, kind=None),
                                            Constant(value=9928, kind=None),
                                            Constant(value=9934, kind=None),
                                            Constant(value=9935, kind=None),
                                            Constant(value=9937, kind=None),
                                            Constant(value=9981, kind=None),
                                            Constant(value=9986, kind=None),
                                            Constant(value=9989, kind=None),
                                            Constant(value=9999, kind=None),
                                            Constant(value=10002, kind=None),
                                            Constant(value=10004, kind=None),
                                            Constant(value=10006, kind=None),
                                            Constant(value=10013, kind=None),
                                            Constant(value=10017, kind=None),
                                            Constant(value=10024, kind=None),
                                            Constant(value=10052, kind=None),
                                            Constant(value=10055, kind=None),
                                            Constant(value=10060, kind=None),
                                            Constant(value=10062, kind=None),
                                            Constant(value=10071, kind=None),
                                            Constant(value=10145, kind=None),
                                            Constant(value=10160, kind=None),
                                            Constant(value=10175, kind=None),
                                            Constant(value=11088, kind=None),
                                            Constant(value=11093, kind=None),
                                            Constant(value=12336, kind=None),
                                            Constant(value=12349, kind=None),
                                            Constant(value=12951, kind=None),
                                            Constant(value=12953, kind=None),
                                            Constant(value=126980, kind=None),
                                            Constant(value=127183, kind=None),
                                            Constant(value=127358, kind=None),
                                            Constant(value=127359, kind=None),
                                            Constant(value=127374, kind=None),
                                            Constant(value=127514, kind=None),
                                            Constant(value=127535, kind=None),
                                            Constant(value=127777, kind=None),
                                            Constant(value=127798, kind=None),
                                            Constant(value=127869, kind=None),
                                            Constant(value=127941, kind=None),
                                            Constant(value=127991, kind=None),
                                            Constant(value=128063, kind=None),
                                            Constant(value=128064, kind=None),
                                            Constant(value=128065, kind=None),
                                            Constant(value=128248, kind=None),
                                            Constant(value=128253, kind=None),
                                            Constant(value=128255, kind=None),
                                            Constant(value=128378, kind=None),
                                            Constant(value=128391, kind=None),
                                            Constant(value=128400, kind=None),
                                            Constant(value=128420, kind=None),
                                            Constant(value=128421, kind=None),
                                            Constant(value=128424, kind=None),
                                            Constant(value=128444, kind=None),
                                            Constant(value=128481, kind=None),
                                            Constant(value=128483, kind=None),
                                            Constant(value=128488, kind=None),
                                            Constant(value=128495, kind=None),
                                            Constant(value=128499, kind=None),
                                            Constant(value=128506, kind=None),
                                            Constant(value=128512, kind=None),
                                            Constant(value=128529, kind=None),
                                            Constant(value=128533, kind=None),
                                            Constant(value=128534, kind=None),
                                            Constant(value=128535, kind=None),
                                            Constant(value=128536, kind=None),
                                            Constant(value=128537, kind=None),
                                            Constant(value=128538, kind=None),
                                            Constant(value=128539, kind=None),
                                            Constant(value=128543, kind=None),
                                            Constant(value=128556, kind=None),
                                            Constant(value=128557, kind=None),
                                            Constant(value=128564, kind=None),
                                            Constant(value=128720, kind=None),
                                            Constant(value=128745, kind=None),
                                            Constant(value=128752, kind=None),
                                            Constant(value=128755, kind=None),
                                            Constant(value=128761, kind=None),
                                            Constant(value=129311, kind=None),
                                            Constant(value=129328, kind=None),
                                            Constant(value=129356, kind=None),
                                            Constant(value=129402, kind=None),
                                            Constant(value=129472, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Call(
                                                func=Name(id='chr', ctx=Load()),
                                                args=[Name(id='emoji', ctx=Load())],
                                                keywords=[],
                                            ),
                                            ops=[In()],
                                            comparators=[Name(id='body', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='emoji', ctx=Store()),
                                                iter=Name(id='emoji_list', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_bot_pinged',
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
                        Assign(
                            targets=[Name(id='odoobot_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.partner_root', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Compare(
                                left=Name(id='odoobot_id', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='partner_ids', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
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
                    name='_is_bot_in_private_channel',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='odoobot_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_xmlid_to_res_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.partner_root', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='mail.channel', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='channel_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='chat', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Compare(
                                        left=Name(id='odoobot_id', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
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
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_help_requested',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns whether a message linking to the documentation and videos\n        should be sent back to the user.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='token', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='body', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='token', ctx=Store()),
                                                        iter=List(
                                                            elts=[
                                                                Constant(value='help', kind=None),
                                                                Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='help', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                Constant(value='?', kind=None),
                                                            ],
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
                                        attr='odoobot_failed',
                                        ctx=Load(),
                                    ),
                                ],
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
