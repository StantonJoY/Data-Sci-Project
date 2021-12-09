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
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.channel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='livechat_visitor_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='website.visitor', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Visitor', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_execute_channel_pin',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pinned', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Override to clean an empty livechat channel.\n         This is typically called when the operator send a chat request to a website.visitor\n         but don't speak to him and closes the chatter.\n         This allows operators to send the visitor a new chat request.\n         If active empty livechat channel,\n         delete mail_channel as not useful to keep empty chat\n         ", kind=None),
                        ),
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
                                    attr='_execute_channel_pin',
                                    ctx=Load(),
                                ),
                                args=[Name(id='pinned', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='livechat_active',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                            value=Constant(value='\n        Override to add visitor information on the mail channel infos.\n        This will be used to display a banner with visitor informations\n        at the top of the livechat channel discussion view in discuss module.\n        ', kind=None),
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
                                Assign(
                                    targets=[Name(id='visitor', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='channel', ctx=Load()),
                                        attr='livechat_visitor_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='visitor', ctx=Load()),
                                    body=[
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
                                                    slice=Constant(value='visitor', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='country_code', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='is_connected', kind=None),
                                                    Constant(value='history', kind=None),
                                                    Constant(value='website_name', kind=None),
                                                    Constant(value='lang_name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=Attribute(
                                                            value=Name(id='visitor', ctx=Load()),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        body=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='visitor', ctx=Load()),
                                                                        attr='country_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='code',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='lower',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        orelse=Constant(value=False, kind=None),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visitor', ctx=Load()),
                                                            attr='country_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='is_connected',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='_get_visitor_history',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='visitor', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visitor', ctx=Load()),
                                                            attr='website_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visitor', ctx=Load()),
                                                            attr='lang_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visitor', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    name='_get_visitor_history',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='visitor', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Prepare history string to render it in the visitor info div on discuss livechat channel view.\n        :param visitor: website.visitor of the channel\n        :return: arrow separated string containing navigation history information\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='recent_history', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website.track', kind=None),
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
                                                    Constant(value='page_id', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='visitor_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
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
                                        arg='limit',
                                        value=Constant(value=3, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' → ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visit', ctx=Load()),
                                                            attr='page_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value=' (', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='visit', ctx=Load()),
                                                            attr='visit_datetime',
                                                            ctx=Load(),
                                                        ),
                                                        attr='strftime',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='%H:%M', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            op=Add(),
                                            right=Constant(value=')', kind=None),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='visit', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='reversed', ctx=Load()),
                                                    args=[Name(id='recent_history', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='livechat_visitor_id',
                                        ctx=Load(),
                                    ),
                                ),
                                body=Call(
                                    func=Name(id='_', ctx=Load()),
                                    args=[Constant(value='The visitor', kind=None)],
                                    keywords=[],
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='livechat_visitor_id',
                                        ctx=Load(),
                                    ),
                                    attr='display_name',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='cancel', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='%s has started a conversation with %s. \n                        The chat request has been canceled.', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='name', ctx=Load()),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='operator', ctx=Load()),
                                                        Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='an operator', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[
                                            Constant(value='%s has left the conversation.', kind=None),
                                            Name(id='name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='message', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='message_post',
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
                            value=Constant(value="Override to mark the visitor as still connected.\n        If the message sent is not from the operator (so if it's the visitor or\n        odoobot sending closing chat notification, the visitor last action date is updated.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
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
                                    attr='message_post',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='message_author_id', ctx=Store())],
                            value=Attribute(
                                value=Name(id='message', ctx=Load()),
                                attr='author_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='visitor', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='livechat_visitor_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Name(id='visitor', ctx=Load()),
                                    Compare(
                                        left=Name(id='message_author_id', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='livechat_operator_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='visitor', ctx=Load()),
                                            attr='_update_visitor_last_visit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='message', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='returns',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='mail.message', kind=None),
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
