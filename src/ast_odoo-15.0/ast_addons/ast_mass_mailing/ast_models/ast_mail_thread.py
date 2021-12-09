Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='BLACKLIST_MAX_BOUNCED_LIMIT', ctx=Store())],
            value=Constant(value=5, kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='MailThread',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Update MailThread to add the support of bounce management in mass mailing traces. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.thread', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_message_route_process',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='message_dict', annotation=None, type_comment=None),
                            arg(arg='routes', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override to update the parent mailing traces. The parent is found\n        by using the References header of the incoming message and looking for\n        matching message_id in mailing.trace. ', kind=None),
                        ),
                        If(
                            test=Name(id='routes', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='thread_references', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='message_dict', ctx=Load()),
                                                slice=Constant(value='references', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='message_dict', ctx=Load()),
                                                slice=Constant(value='in_reply_to', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='msg_references', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='mail_header_msgid_re',
                                                ctx=Load(),
                                            ),
                                            attr='findall',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='thread_references', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='msg_references', ctx=Load()),
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
                                                        slice=Constant(value='mailing.trace', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='set_opened',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='domain',
                                                        value=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='message_id', kind=None),
                                                                        Constant(value='in', kind=None),
                                                                        Name(id='msg_references', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                                        slice=Constant(value='mailing.trace', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='set_replied',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='domain',
                                                        value=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='message_id', kind=None),
                                                                        Constant(value='in', kind=None),
                                                                        Name(id='msg_references', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailThread', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_message_route_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message', ctx=Load()),
                                    Name(id='message_dict', ctx=Load()),
                                    Name(id='routes', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='message_post_with_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='no_massmail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='default_mass_mailing_name',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='default_mass_mailing_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailThread', ctx=Load()),
                                            Name(id='no_massmail', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='message_post_with_template',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template_id', ctx=Load())],
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
                FunctionDef(
                    name='_routing_handle_bounce',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email_message', annotation=None, type_comment=None),
                            arg(arg='message_dict', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' In addition, an auto blacklist rule check if the email can be blacklisted\n        to avoid sending mails indefinitely to this email address.\n        This rule checks if the email bounced too much. If this is the case,\n        the email address is added to the blacklist in order to avoid continuing\n        to send mass_mail to that email address. If it bounced too much times\n        in the last month and the bounced are at least separated by one week,\n        to avoid blacklist someone because of a temporary mail server error,\n        then the email is considered as invalid and is blacklisted.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailThread', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_routing_handle_bounce',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='email_message', ctx=Load()),
                                    Name(id='message_dict', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='bounced_email', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message_dict', ctx=Load()),
                                slice=Constant(value='bounced_email', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bounced_msg_id', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message_dict', ctx=Load()),
                                slice=Constant(value='bounced_msg_id', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bounced_partner', ctx=Store())],
                            value=Subscript(
                                value=Name(id='message_dict', ctx=Load()),
                                slice=Constant(value='bounced_partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='bounced_msg_id', ctx=Load()),
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
                                                slice=Constant(value='mailing.trace', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='set_bounced',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='message_id', kind=None),
                                                                Constant(value='in', kind=None),
                                                                Name(id='bounced_msg_id', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='bounced_email', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='three_months_ago', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='datetime',
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
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='timedelta',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='weeks',
                                                            value=Constant(value=13, kind=None),
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
                                    targets=[Name(id='stats', ctx=Store())],
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
                                                        slice=Constant(value='mailing.trace', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='&', kind=None),
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='trace_status', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='bounce', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='write_date', kind=None),
                                                                    Constant(value='>', kind=None),
                                                                    Name(id='three_months_ago', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='email', kind=None),
                                                                    Constant(value='=ilike', kind=None),
                                                                    Name(id='bounced_email', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='write_date', kind=None)],
                                        keywords=[],
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
                                                    args=[Name(id='stats', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[GtE()],
                                                comparators=[Name(id='BLACKLIST_MAX_BOUNCED_LIMIT', ctx=Load())],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='bounced_partner', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Name(id='any', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='p', ctx=Load()),
                                                                        attr='message_bounce',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[GtE()],
                                                                    comparators=[Name(id='BLACKLIST_MAX_BOUNCED_LIMIT', ctx=Load())],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='p', ctx=Store()),
                                                                        iter=Name(id='bounced_partner', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='max', ctx=Load()),
                                                    args=[Name(id='stats', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='min', ctx=Load()),
                                                            args=[Name(id='stats', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='datetime', ctx=Load()),
                                                                attr='timedelta',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='weeks',
                                                                    value=Constant(value=1, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='blacklist_rec', ctx=Store())],
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
                                                                        slice=Constant(value='mail.blacklist', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='_add',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='bounced_email', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='blacklist_rec', ctx=Load()),
                                                            attr='_message_log',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Constant(value='This email has been automatically blacklisted because of too much bounced.', kind=None),
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
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='message_new',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='msg_dict', annotation=None, type_comment=None),
                            arg(arg='custom_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Overrides mail_thread message_new that is called by the mailgateway\n            through message_process.\n            This override updates the document according to the email.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='defaults', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='issubclass', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pool',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='utm.mixin', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='thread_references', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='msg_dict', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='references', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='msg_dict', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='in_reply_to', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='msg_references', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='mail_header_msgid_re',
                                                ctx=Load(),
                                            ),
                                            attr='findall',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='thread_references', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='msg_references', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='traces', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mailing.trace', kind=None),
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
                                                                    Constant(value='message_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='msg_references', ctx=Load()),
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
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='traces', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='defaults', ctx=Load()),
                                                            slice=Constant(value='campaign_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='traces', ctx=Load()),
                                                            attr='campaign_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='defaults', ctx=Load()),
                                                            slice=Constant(value='source_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='traces', ctx=Load()),
                                                                attr='mass_mailing_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='source_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='defaults', ctx=Load()),
                                                            slice=Constant(value='medium_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='traces', ctx=Load()),
                                                                attr='mass_mailing_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='medium_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='custom_values', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='defaults', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='custom_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailThread', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='message_new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='msg_dict', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='custom_values',
                                        value=Name(id='defaults', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
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
