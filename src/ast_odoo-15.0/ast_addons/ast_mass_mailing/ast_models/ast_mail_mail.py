Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailMail',
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
                    value=Constant(value='Add the mass mailing campaign data to mail', kind=None),
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='mail.mail', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mailing.mailing', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mass Mailing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_trace_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mailing.trace', kind=None),
                            Constant(value='mail_mail_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Statistics', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override mail_mail creation to create an entry in mail.mail.statistics ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mails', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailMail', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='mail', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='mails', ctx=Load()),
                                    Name(id='values_list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mailing_trace_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='mail', ctx=Load()),
                                                        attr='mailing_trace_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='message_id', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='message_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                        Return(
                            value=Name(id='mails', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_tracking_url',
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
                            targets=[Name(id='token', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='hmac',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='su',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='mass_mailing-mail_mail-open', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='urls',
                                        ctx=Load(),
                                    ),
                                    attr='url_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Constant(value='mail/track/%s/%s/blank.gif', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='token', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
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
                    name='_send_prepare_body',
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
                            value=Constant(value=' Override to add the tracking URL to the body and to add\n        trace ID in shortened urls ', kind=None),
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
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailMail', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_send_prepare_body',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='body', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing_trace_ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='match', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='findall',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='URL_REGEX',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='body_html',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='href', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='match', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='url', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='match', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='parsed', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='urls',
                                                        ctx=Load(),
                                                    ),
                                                    attr='url_parse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='url', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='scheme',
                                                        value=Constant(value='http', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='parsed', ctx=Load()),
                                                                attr='scheme',
                                                                ctx=Load(),
                                                            ),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='http', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='parsed', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='/r/', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='new_href', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='href', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='url', ctx=Load()),
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='url', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value='/m/', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='mailing_trace_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='body', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='body', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='href', ctx=Load()),
                                                            Name(id='new_href', ctx=Load()),
                                                        ],
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
                                Assign(
                                    targets=[Name(id='tracking_url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_tracking_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='append_content_to_html',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='body', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='<img src="%s"/>', kind=None),
                                                op=Mod(),
                                                right=Name(id='tracking_url', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='plaintext',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
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
                                args=[Name(id='body', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='body', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_prepare_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailMail', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_send_prepare_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='partner', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mailing_id',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='body', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email_to', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='base_url', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mailing_id',
                                                ctx=Load(),
                                            ),
                                            attr='get_base_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='emails', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='res', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='email_to', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='email_to', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='emails', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='emails', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='urls_to_replace', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Name(id='base_url', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='/unsubscribe_from_list', kind=None),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='mailing_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_unsubscribe_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='email_to', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='res_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    BinOp(
                                                        left=Name(id='base_url', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='/view', kind=None),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='mailing_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_view_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='email_to', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='res_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='url_to_replace', ctx=Store()),
                                            Name(id='new_url', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='urls_to_replace', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='url_to_replace', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='body', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Constant(value='body', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Constant(value='body', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='url_to_replace', ctx=Load()),
                                                            IfExp(
                                                                test=Name(id='new_url', ctx=Load()),
                                                                body=Name(id='new_url', ctx=Load()),
                                                                orelse=Constant(value='#', kind=None),
                                                            ),
                                                        ],
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_postprocess_sent_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='success_pids', annotation=None, type_comment=None),
                            arg(arg='failure_reason', annotation=None, type_comment=None),
                            arg(arg='failure_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mail_sent', ctx=Store())],
                            value=UnaryOp(
                                op=Not(),
                                operand=Name(id='failure_type', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='mail', ctx=Load()),
                                        attr='mailing_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='mail_sent', ctx=Load()),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=True, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='mail', ctx=Load()),
                                                        attr='mailing_trace_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='mailing_trace_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='set_sent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                                                                left=Name(id='mail_sent', ctx=Load()),
                                                                ops=[Is()],
                                                                comparators=[Constant(value=False, kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='mailing_trace_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='mail', ctx=Load()),
                                                                        attr='mailing_trace_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='set_failed',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='failure_type',
                                                                        value=Name(id='failure_type', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
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
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailMail', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_postprocess_sent_message',
                                    ctx=Load(),
                                ),
                                args=[Name(id='success_pids', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='failure_reason',
                                        value=Name(id='failure_reason', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='failure_type',
                                        value=Name(id='failure_type', ctx=Load()),
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
