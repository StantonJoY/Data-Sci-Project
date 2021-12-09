Module(
    body=[
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MailNotification',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.notification', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_table', ctx=Store())],
                    value=Constant(value='mail_notification', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='res_partner_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_log_access', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Message Notifications', kind=None),
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
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mail_mail_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mail.mail', kind=None),
                            Constant(value='Mail', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Optional mail_mail ID. Used mainly to optimize searches.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='Recipient', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='notification_type', ctx=Store())],
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
                                            Constant(value='inbox', kind=None),
                                            Constant(value='Inbox', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='email', kind=None),
                                            Constant(value='Email', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Notification Type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='inbox', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='notification_status', ctx=Store())],
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
                                            Constant(value='ready', kind=None),
                                            Constant(value='Ready to Send', kind=None),
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
                                            Constant(value='bounce', kind=None),
                                            Constant(value='Bounced', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='exception', kind=None),
                                            Constant(value='Exception', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='canceled', kind=None),
                                            Constant(value='Canceled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Status', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='ready', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_read', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Is Read', kind=None)],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='read_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Read Date', kind=None)],
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
                                                Constant(value='Missing email addresss', kind=None),
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
                        args=[Constant(value='Failure reason', kind=None)],
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
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='notification_partner_required', kind=None),
                                    Constant(value="CHECK(notification_type NOT IN ('email', 'inbox') OR res_partner_id IS NOT NULL)", kind=None),
                                    Constant(value='Customer is required for inbox / email notification', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            CREATE INDEX IF NOT EXISTS mail_notification_res_partner_id_is_read_notification_status_mail_message_id\n                                    ON mail_notification (res_partner_id, is_read, notification_status, mail_message_id)\n        ', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='messages', ctx=Store())],
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
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='mail_message_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='vals', ctx=Store()),
                                                iter=Name(id='vals_list', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='messages', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='messages', ctx=Load()),
                                    attr='check_access_rule',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='is_read', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='read_date', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
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
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailNotification', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='mail_message_id', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='res_partner_id', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='is_admin',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Can not update the message or recipient of a notification.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='is_read', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='read_date', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
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
                                            Name(id='MailNotification', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_gc_notifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='max_age_days', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=180, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='is_read', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='read_date', kind=None),
                                            Constant(value='<', kind=None),
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
                                                            value=Name(id='max_age_days', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='res_partner_id.partner_share', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='notification_status', kind=None),
                                            Constant(value='in', kind=None),
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
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
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
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='format_failure_reason',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='failure_type',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='unknown', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Call(
                                                                func=Name(id='type', ctx=Load()),
                                                                args=[Name(id='self', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='failure_type',
                                                            ctx=Load(),
                                                        ),
                                                        attr='selection',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='failure_type',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='No Error', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Unknown error', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=BinOp(
                                            left=Constant(value=': %s', kind=None),
                                            op=Mod(),
                                            right=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='failure_reason',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filtered_for_web_client',
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
                            value=Constant(value='Returns only the notifications to show on the web client.', kind=None),
                        ),
                        Return(
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
                                            args=[arg(arg='n', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='n', ctx=Load()),
                                                        attr='notification_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='inbox', kind=None)],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='n', ctx=Load()),
                                                                attr='notification_status',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='bounce', kind=None),
                                                                        Constant(value='exception', kind=None),
                                                                        Constant(value='canceled', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='n', ctx=Load()),
                                                                attr='res_partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_share',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
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
                    name='_notification_format',
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
                            value=Constant(value='Returns the current notifications in the format expected by the web\n        client.', kind=None),
                        ),
                        Return(
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='id', kind=None),
                                        Constant(value='notification_type', kind=None),
                                        Constant(value='notification_status', kind=None),
                                        Constant(value='failure_type', kind=None),
                                        Constant(value='res_partner_id', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            value=Name(id='notif', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='notif', ctx=Load()),
                                            attr='notification_type',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='notif', ctx=Load()),
                                            attr='notification_status',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='notif', ctx=Load()),
                                            attr='failure_type',
                                            ctx=Load(),
                                        ),
                                        IfExp(
                                            test=Attribute(
                                                value=Name(id='notif', ctx=Load()),
                                                attr='res_partner_id',
                                                ctx=Load(),
                                            ),
                                            body=List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='notif', ctx=Load()),
                                                            attr='res_partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='notif', ctx=Load()),
                                                            attr='res_partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            orelse=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='notif', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
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
