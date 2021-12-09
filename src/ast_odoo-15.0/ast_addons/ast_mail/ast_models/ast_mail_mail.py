Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='smtplib', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_mail_server',
            names=[alias(name='MailDeliveryException', asname=None)],
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
                    value=Constant(value=' Model holding RFC2822 email messages to send. This model also provides\n        facilities to queue and send new email messages.  ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.mail', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Outgoing Mails', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherits', ctx=Store())],
                    value=Dict(
                        keys=[Constant(value='mail.message', kind=None)],
                        values=[Constant(value='mail_message_id', kind=None)],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='id desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='subject', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='default_type', kind=None)],
                                    keywords=[],
                                ),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Name(id='type', ctx=Load()),
                                                    args=[Name(id='self', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='message_type',
                                                ctx=Load(),
                                            ),
                                            attr='base_field',
                                            ctx=Load(),
                                        ),
                                        attr='selection',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='self', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='default_type',
                                                        value=Constant(value=None, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                                            Name(id='MailMail', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields', ctx=Load())],
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
                Assign(
                    targets=[Name(id='mail_message_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mail.message', kind=None),
                            Constant(value='Message', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='auto_join',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='body_html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Rich-text Contents', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Rich-text/HTML message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='references', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='References', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Message references, such as identifiers of previous messages', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='headers', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Headers', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_notification', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Notification Email', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Mail has been created to notify people of an existing mail.message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='To', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Message recipients (emails)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_cc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Cc', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Carbon copy message recipients', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='recipient_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='To (Partners)', kind=None),
                            ),
                            keyword(
                                arg='context',
                                value=Dict(
                                    keys=[Constant(value='active_test', kind=None)],
                                    values=[Constant(value=False, kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='outgoing', kind=None),
                                            Constant(value='Outgoing', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sent', kind=None),
                                            Constant(value='Sent', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='received', kind=None),
                                            Constant(value='Received', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='exception', kind=None),
                                            Constant(value='Delivery Failed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cancel', kind=None),
                                            Constant(value='Cancelled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Status', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='outgoing', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='failure_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='unknown', kind=None),
                                                Constant(value='Unknown error', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='mail_email_invalid', kind=None),
                                                Constant(value='Invalid email address', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='mail_email_missing', kind=None),
                                                Constant(value='Missing email', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='mail_smtp', kind=None),
                                                Constant(value='Connection failed (outgoing mail server problem)', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='mail_bl', kind=None),
                                                Constant(value='Blacklisted Address', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='mail_optout', kind=None),
                                                Constant(value='Opted Out', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='mail_dup', kind=None),
                                                Constant(value='Duplicated Email', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Failure type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='failure_reason', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Failure Reason', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Failure reason. This is usually the exception thrown by the email server, stored to ease the debugging of mailing issues.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto_delete', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Auto Delete', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="This option permanently removes any track of email after it's been sent, including from the Technical menu in the Settings, in order to preserve storage space of your Odoo database.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='scheduled_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Scheduled Send Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='If set, the queue manager will send the email after the date. If not set, the email will be send as soon as possible.', kind=None),
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
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='values_list', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='is_notification', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='values', ctx=Load())],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail_message_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='is_notification', kind=None),
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
                        Assign(
                            targets=[Name(id='new_mails', ctx=Store())],
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
                        Assign(
                            targets=[Name(id='new_mails_w_attach', ctx=Store())],
                            value=Name(id='self', ctx=Load()),
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
                                    Name(id='new_mails', ctx=Load()),
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
                                        args=[Constant(value='attachment_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='new_mails_w_attach', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='mail', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='new_mails_w_attach', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_mails_w_attach', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='attachment_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='check',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mode',
                                                value=Constant(value='read', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='new_mails', ctx=Load()),
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='attachment_ids', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='mail', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='mail', ctx=Load()),
                                                        attr='attachment_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='check',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mode',
                                                        value=Constant(value='read', kind=None),
                                                    ),
                                                ],
                                            ),
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
                    name='unlink',
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
                            targets=[Name(id='mail_msg_cascade_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Attribute(
                                        value=Name(id='mail', ctx=Load()),
                                        attr='mail_message_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='mail', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='is_notification',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
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
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='mail_msg_cascade_ids', ctx=Load()),
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
                                                        slice=Constant(value='mail.message', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='mail_msg_cascade_ids', ctx=Load())],
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
                    name='action_retry',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='mail', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='mail', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='exception', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='mark_outgoing',
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
                    name='mark_outgoing',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='outgoing', kind=None)],
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
                    name='cancel',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='cancel', kind=None)],
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
                    name='process_email_queue',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Send immediately queued messages, committing after each\n           message is sent - this is not transactional and should\n           not be called during another transaction!\n\n           :param list ids: optional list of emails ids to send. If passed\n                            no search is performed, and these ids are used\n                            instead.\n           :param dict context: if a 'filters' key is present in context,\n                                this value will be used as an additional\n                                filter to further restrict the outgoing\n                                messages to send (by default all 'outgoing'\n                                messages are sent).\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='filters', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='outgoing', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='scheduled_date', kind=None),
                                            Constant(value='<', kind=None),
                                            Call(
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
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='scheduled_date', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='filters', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='filters', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='filters', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='filtered_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='filters', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='limit',
                                            value=Constant(value=10000, kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='ids', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=Name(id='filtered_ids', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[Name(id='filtered_ids', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=BitAnd(),
                                                right=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[Name(id='ids', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ids', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='auto_commit', ctx=Store())],
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='threading', ctx=Load()),
                                                        attr='currentThread',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Constant(value='testing', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='send',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='auto_commit',
                                                value=Name(id='auto_commit', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Failed processing mail queue', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
                        Expr(
                            value=Constant(value='Perform any post-processing necessary after sending ``mail``\n        successfully, including deleting it completely along with its\n        attachment if the ``auto_delete`` flag of the mail was set.\n        Overridden by subclasses for extra post-processing behaviors.\n\n        :return: True\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='notif_mails_ids', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='mail', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='mail', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[
                                            Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='is_notification',
                                                ctx=Load(),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='notif_mails_ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='notifications', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.notification', kind=None),
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
                                                            Constant(value='notification_type', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='email', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='mail_mail_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='notif_mails_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='notification_status', kind=None),
                                                            Constant(value='not in', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='sent', kind=None),
                                                                    Constant(value='canceled', kind=None),
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
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='notifications', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='failed', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.notification', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='failure_type', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='failed', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='notifications', ctx=Load()),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='notif', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='notif', ctx=Load()),
                                                                        attr='res_partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotIn()],
                                                                    comparators=[Name(id='success_pids', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=Name(id='notifications', ctx=Load()),
                                                                op=Sub(),
                                                                right=Name(id='failed', ctx=Load()),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='notification_status', kind=None),
                                                            Constant(value='failure_type', kind=None),
                                                            Constant(value='failure_reason', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='sent', kind=None),
                                                            Constant(value='', kind=None),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Name(id='failed', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='failed', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='notification_status', kind=None),
                                                                    Constant(value='failure_type', kind=None),
                                                                    Constant(value='failure_reason', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='exception', kind=None),
                                                                    Name(id='failure_type', ctx=Load()),
                                                                    Name(id='failure_reason', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='messages', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='notifications', ctx=Load()),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='mail_message_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='is_thread_message',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
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
                                                            value=Name(id='messages', ctx=Load()),
                                                            attr='_notify_message_notification_update',
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
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='failure_type', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Name(id='failure_type', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='mail_email_invalid', kind=None),
                                                    Constant(value='mail_email_missing', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='mail_to_delete_ids', ctx=Store())],
                                    value=ListComp(
                                        elt=Attribute(
                                            value=Name(id='mail', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='mail', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[
                                                    Attribute(
                                                        value=Name(id='mail', ctx=Load()),
                                                        attr='auto_delete',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='mail_to_delete_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
                            value=Constant(value='Return a specific ir_email body. The main purpose of this method\n        is to be inherited to add custom content depending on some module.', kind=None),
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
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='body_html',
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
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
                        Expr(
                            value=Constant(value='Return a dictionary for specific email values, depending on a\n        partner, or generic to the whole recipients given by mail.email_to.\n\n            :param Model partner: specific recipient partner\n        ', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_send_prepare_body',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body_alternative', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='html2plaintext',
                                    ctx=Load(),
                                ),
                                args=[Name(id='body', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partner', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='email_to', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='formataddr',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='False', kind=None),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='email',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='False', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='email_to', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='email_split_and_format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='email_to',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='body', kind=None),
                                    Constant(value='body_alternative', kind=None),
                                    Constant(value='email_to', kind=None),
                                ],
                                values=[
                                    Name(id='body', ctx=Load()),
                                    Name(id='body_alternative', ctx=Load()),
                                    Name(id='email_to', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
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
                    name='_split_by_mail_configuration',
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
                            value=Constant(value='Group the <mail.mail> based on their "email_from" and their "mail_server_id".\n\n        The <mail.mail> will have the "same sending configuration" if they have the same\n        mail server or the same mail from. For performance purpose, we can use an SMTP\n        session in batch and therefore we need to group them by the parameter that will\n        influence the mail server used.\n\n        The same "sending configuration" may repeat in order to limit batch size\n        according to the `mail.session.batch.size` system parameter.\n\n        Return iterators over\n            mail_server_id, email_from, Records<mail.mail>.ids\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mail_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='email_from', kind=None),
                                            Constant(value='mail_server_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_per_email_from', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='mail_values', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='mail_server_id', ctx=Store())],
                                    value=IfExp(
                                        test=Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='mail_server_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='mail_server_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='group_per_email_from', ctx=Load()),
                                                slice=Tuple(
                                                    elts=[
                                                        Name(id='mail_server_id', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='email_from', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_servers', ctx=Store())],
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
                                                slice=Constant(value='ir.mail_server', kind=None),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='sequence', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_per_smtp_from', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Name(id='mail_server_id', ctx=Store()),
                                            Name(id='email_from', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    Name(id='mail_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='group_per_email_from', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='mail_server_id', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='mail_server', ctx=Store()),
                                                        Name(id='smtp_from', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.mail_server', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_find_mail_server',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='email_from', ctx=Load()),
                                                    Name(id='mail_servers', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mail_server_id', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='mail_server', ctx=Load()),
                                                body=Attribute(
                                                    value=Name(id='mail_server', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='smtp_from', ctx=Store())],
                                            value=Name(id='email_from', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='group_per_smtp_from', ctx=Load()),
                                                slice=Tuple(
                                                    elts=[
                                                        Name(id='mail_server_id', ctx=Load()),
                                                        Name(id='smtp_from', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='mail_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sys_params', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='batch_size', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='sys_params', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='mail.session.batch.size', kind=None),
                                            Constant(value=1000, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Name(id='mail_server_id', ctx=Store()),
                                            Name(id='smtp_from', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    Name(id='record_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='group_per_smtp_from', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='batch_ids', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='split_every',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='batch_size', ctx=Load()),
                                            Name(id='record_ids', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Tuple(
                                                    elts=[
                                                        Name(id='mail_server_id', ctx=Load()),
                                                        Name(id='smtp_from', ctx=Load()),
                                                        Name(id='batch_ids', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
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
                    name='send',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='auto_commit', annotation=None, type_comment=None),
                            arg(arg='raise_exception', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value=" Sends the selected emails immediately, ignoring their current\n            state (mails that have already been sent should not be passed\n            unless they should actually be re-sent).\n            Emails successfully delivered are marked as 'sent', and those\n            that fail to be deliver are marked as 'exception', and the\n            corresponding error mail is output in the server logs.\n\n            :param bool auto_commit: whether to force a commit of the mail status\n                after sending each mail (meant only for scheduler processing);\n                should never be True during normal transactions (default: False)\n            :param bool raise_exception: whether to raise an exception if the\n                email sending process has failed\n            :return: True\n        ", kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='mail_server_id', ctx=Store()),
                                    Name(id='smtp_from', ctx=Store()),
                                    Name(id='batch_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_split_by_mail_configuration',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='smtp_session', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='smtp_session', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.mail_server', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='connect',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_server_id',
                                                        value=Name(id='mail_server_id', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='smtp_from',
                                                        value=Name(id='smtp_from', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='exc',
                                            body=[
                                                If(
                                                    test=Name(id='raise_exception', ctx=Load()),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='MailDeliveryException', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Unable to connect to SMTP Server', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='exc', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='batch', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='browse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='batch_ids', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='batch', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='state', kind=None),
                                                                            Constant(value='failure_reason', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='exception', kind=None),
                                                                            Name(id='exc', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='batch', ctx=Load()),
                                                                    attr='_postprocess_sent_message',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='success_pids',
                                                                        value=List(elts=[], ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='failure_type',
                                                                        value=Constant(value='mail_smtp', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='batch_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='_send',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='auto_commit',
                                                        value=Name(id='auto_commit', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='raise_exception',
                                                        value=Name(id='raise_exception', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='smtp_session',
                                                        value=Name(id='smtp_session', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Sent batch %s emails via mail server ID #%s', kind=None),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='batch_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='mail_server_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    finalbody=[
                                        If(
                                            test=Name(id='smtp_session', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='smtp_session', ctx=Load()),
                                                            attr='quit',
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
                    name='_send',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='auto_commit', annotation=None, type_comment=None),
                            arg(arg='raise_exception', annotation=None, type_comment=None),
                            arg(arg='smtp_session', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='IrMailServer', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.mail_server', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrAttachment', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mail_id', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='success_pids', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='failure_type', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='processing_pid', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mail', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='mail', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='mail_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='outgoing', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='exception', kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='auto_delete',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='mail', ctx=Load()),
                                                                            attr='sudo',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
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
                                                    orelse=[],
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='body', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='mail', ctx=Load()),
                                                        attr='body_html',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attachments', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='attachment_ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='link', ctx=Store()),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='findall',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/web/(?:content|image)/([0-9]+)', kind=None),
                                                    Name(id='body', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='attachments', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='attachments', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='IrAttachment', ctx=Load()),
                                                                attr='browse',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='int', ctx=Load()),
                                                                    args=[Name(id='link', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attachments', ctx=Store())],
                                            value=ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='a', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='base64', ctx=Load()),
                                                                attr='b64decode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='a', ctx=Load()),
                                                                    slice=Constant(value='datas', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Subscript(
                                                            value=Name(id='a', ctx=Load()),
                                                            slice=Constant(value='mimetype', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='a', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='attachments', ctx=Load()),
                                                                        attr='sudo',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='read',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='datas', kind=None),
                                                                        Constant(value='mimetype', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='a', ctx=Load()),
                                                                    slice=Constant(value='datas', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[IsNot()],
                                                                comparators=[Constant(value=False, kind=None)],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='email_list', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='email_to',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='email_list', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='_send_prepare_values',
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
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='partner', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='recipient_ids',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='values', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='_send_prepare_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='partner',
                                                                value=Name(id='partner', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='partner_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='partner', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='email_list', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='values', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='headers', ctx=Store())],
                                            value=Dict(keys=[], values=[]),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ICP', ctx=Store())],
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
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='bounce_alias', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ICP', ctx=Load()),
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.bounce.alias', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='catchall_domain', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ICP', ctx=Load()),
                                                    attr='get_param',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mail.catchall.domain', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='bounce_alias', ctx=Load()),
                                                    Name(id='catchall_domain', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='headers', ctx=Load()),
                                                            slice=Constant(value='Return-Path', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Constant(value='%s@%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='bounce_alias', ctx=Load()),
                                                                Name(id='catchall_domain', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='headers',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='headers', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='ast', ctx=Load()),
                                                                            attr='literal_eval',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='mail', ctx=Load()),
                                                                                attr='headers',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='Exception', ctx=Load()),
                                                            name=None,
                                                            body=[Pass()],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='failure_reason', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='exception', kind=None),
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Error without exception. Probably due do sending an email without computed recipients.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='notifs', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.notification', kind=None),
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
                                                                    Constant(value='notification_type', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='email', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='mail_mail_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='mail', ctx=Load()),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='notification_status', kind=None),
                                                                    Constant(value='not in', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='sent', kind=None),
                                                                            Constant(value='canceled', kind=None),
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
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='notifs', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='notif_msg', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Error without exception. Probably due do concurrent access update of notification records. Please see with an administrator.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='notifs', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='notification_status', kind=None),
                                                                    Constant(value='failure_type', kind=None),
                                                                    Constant(value='failure_reason', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='exception', kind=None),
                                                                    Constant(value='unknown', kind=None),
                                                                    Name(id='notif_msg', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='notifs', ctx=Load()),
                                                            attr='flush',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='fnames',
                                                                value=List(
                                                                    elts=[
                                                                        Constant(value='notification_status', kind=None),
                                                                        Constant(value='failure_type', kind=None),
                                                                        Constant(value='failure_reason', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='records',
                                                                value=Name(id='notifs', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='email', ctx=Store()),
                                            iter=Name(id='email_list', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='IrMailServer', ctx=Load()),
                                                            attr='build_email',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='email_from',
                                                                value=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='email_from',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='email_to',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='email', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='email_to', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='subject',
                                                                value=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='subject',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='body',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='email', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='body', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='body_alternative',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='email', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='body_alternative', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='email_cc',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='tools', ctx=Load()),
                                                                        attr='email_split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='mail', ctx=Load()),
                                                                            attr='email_cc',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='reply_to',
                                                                value=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='reply_to',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='attachments',
                                                                value=Name(id='attachments', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='message_id',
                                                                value=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='message_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='references',
                                                                value=Attribute(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    attr='references',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='object_id',
                                                                value=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='mail', ctx=Load()),
                                                                            attr='res_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        BinOp(
                                                                            left=Constant(value='%s-%s', kind=None),
                                                                            op=Mod(),
                                                                            right=Tuple(
                                                                                elts=[
                                                                                    Attribute(
                                                                                        value=Name(id='mail', ctx=Load()),
                                                                                        attr='res_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='mail', ctx=Load()),
                                                                                        attr='model',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='subtype',
                                                                value=Constant(value='html', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='subtype_alternative',
                                                                value=Constant(value='plain', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='headers',
                                                                value=Name(id='headers', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='processing_pid', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='email', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='partner_id', kind=None),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='res', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='IrMailServer', ctx=Load()),
                                                                    attr='send_email',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='msg', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='mail_server_id',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='mail', ctx=Load()),
                                                                                attr='mail_server_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='smtp_session',
                                                                        value=Name(id='smtp_session', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='processing_pid', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='success_pids', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='processing_pid', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='processing_pid', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='AssertionError', ctx=Load()),
                                                            name='error',
                                                            body=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[Name(id='error', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='IrMailServer', ctx=Load()),
                                                                                attr='NO_VALID_RECIPIENT',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    UnaryOp(
                                                                                        op=Not(),
                                                                                        operand=Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='email', ctx=Load()),
                                                                                                attr='get',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='email_to', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Name(id='failure_type', ctx=Load()),
                                                                                        ops=[NotEq()],
                                                                                        comparators=[Constant(value='RECIPIENT', kind=None)],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='failure_type', ctx=Store())],
                                                                                    value=Constant(value='mail_email_missing', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='failure_type', ctx=Store())],
                                                                                    value=Constant(value='mail_email_invalid', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='_logger', ctx=Load()),
                                                                                    attr='info',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Constant(value='Ignoring invalid recipients for mail.mail %s: %s', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='mail', ctx=Load()),
                                                                                        attr='message_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='email', ctx=Load()),
                                                                                            attr='get',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='email_to', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[Raise(exc=None, cause=None)],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='res', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='message_id', kind=None),
                                                                    Constant(value='failure_reason', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='sent', kind=None),
                                                                    Name(id='res', ctx=Load()),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Mail with ID %r and Message-Id %r successfully sent', kind=None),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='message_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='_postprocess_sent_message',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='success_pids',
                                                        value=Name(id='success_pids', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='failure_type',
                                                        value=Name(id='failure_type', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='MemoryError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='MemoryError while processing mail with ID %r and Msg-Id %r. Consider raising the --limit-memory-hard startup option', kind=None),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='message_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Raise(exc=None, cause=None),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='psycopg2', ctx=Load()),
                                                        attr='Error',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='smtplib', ctx=Load()),
                                                        attr='SMTPServerDisconnected',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Exception while processing mail with ID %r and Msg-Id %r.', kind=None),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='message_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Raise(exc=None, cause=None),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Assign(
                                                    targets=[Name(id='failure_reason', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='tools', ctx=Load()),
                                                            attr='ustr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='failed sending mail (id: %s) due to %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='failure_reason', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='failure_reason', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='exception', kind=None),
                                                                    Name(id='failure_reason', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='_postprocess_sent_message',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='success_pids',
                                                                value=Name(id='success_pids', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='failure_reason',
                                                                value=Name(id='failure_reason', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='failure_type',
                                                                value=Constant(value='unknown', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                If(
                                                    test=Name(id='raise_exception', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='e', ctx=Load()),
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='AssertionError', ctx=Load()),
                                                                            Name(id='UnicodeEncodeError', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Name(id='e', ctx=Load()),
                                                                            Name(id='UnicodeEncodeError', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='value', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Constant(value='Invalid text: %s', kind=None),
                                                                                op=Mod(),
                                                                                right=Attribute(
                                                                                    value=Name(id='e', ctx=Load()),
                                                                                    attr='object',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[Name(id='value', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value='. ', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='e', ctx=Load()),
                                                                                        attr='args',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                                Raise(
                                                                    exc=Call(
                                                                        func=Name(id='MailDeliveryException', ctx=Load()),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    cause=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Raise(exc=None, cause=None),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='auto_commit', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=True, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='commit',
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
