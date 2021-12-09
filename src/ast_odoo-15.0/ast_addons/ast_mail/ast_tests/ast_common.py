Module(
    body=[
        Import(
            names=[alias(name='email', asname=None)],
        ),
        Import(
            names=[alias(name='email.policy', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='contextlib',
            names=[alias(name='contextmanager', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='html', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='smtplib',
            names=[alias(name='SMTPServerDisconnected', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='exceptions', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_mail_server',
            names=[
                alias(name='IrMailServer', asname=None),
                alias(name='MailDeliveryException', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.bus.models.bus',
            names=[
                alias(name='ImBus', asname=None),
                alias(name='json_dump', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.models.mail_mail',
            names=[alias(name='MailMail', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.models.mail_message',
            names=[alias(name='Message', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.models.mail_notification',
            names=[alias(name='MailNotification', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='common', asname=None),
                alias(name='new_test_user', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='formataddr', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='mail_new_test_user', ctx=Store())],
            value=Call(
                func=Name(id='partial', ctx=Load()),
                args=[Name(id='new_test_user', ctx=Load())],
                keywords=[
                    keyword(
                        arg='context',
                        value=Dict(
                            keys=[
                                Constant(value='mail_create_nolog', kind=None),
                                Constant(value='mail_create_nosubscribe', kind=None),
                                Constant(value='mail_notrack', kind=None),
                                Constant(value='no_reset_password', kind=None),
                            ],
                            values=[
                                Constant(value=True, kind=None),
                                Constant(value=True, kind=None),
                                Constant(value=True, kind=None),
                                Constant(value=True, kind=None),
                            ],
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='MockEmail',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='BaseCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Tools, helpers and asserts for mailgateway-related tests\n\n    Useful reminders\n        Mail state: ('outgoing', 'Outgoing'), ('sent', 'Sent'),\n                    ('received', 'Received'), ('exception', 'Delivery Failed'),\n                    ('cancel', 'Cancelled')\n    ", kind=None),
                ),
                FunctionDef(
                    name='mock_mail_gateway',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mail_unlink_sent', annotation=None, type_comment=None),
                            arg(arg='sim_error', annotation=None, type_comment=None),
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
                            targets=[Name(id='build_email_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='IrMailServer', ctx=Load()),
                                attr='build_email',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_create_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='MailMail', ctx=Load()),
                                attr='create',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mail_unlink_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='MailMail', ctx=Load()),
                                attr='unlink',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mail_unlink_sent',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='mail_unlink_sent', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_init_mail_mock',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='_ir_mail_server_connect',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='sim_error', ctx=Load()),
                                            Compare(
                                                left=Name(id='sim_error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='connect_smtp_notfound', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='exceptions', ctx=Load()),
                                                    attr='UserError',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Missing SMTP Server\nPlease define at least one SMTP server, or provide the SMTP parameters explicitly.', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='sim_error', ctx=Load()),
                                            Compare(
                                                left=Name(id='sim_error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='connect_failure', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[Constant(value='Some exception', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_ir_mail_server_build_email',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mails',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='kwargs', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mails_args',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='args', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='build_email_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
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
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_ir_mail_server_send_email',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='model', annotation=None, type_comment=None),
                                    arg(arg='message', annotation=None, type_comment=None),
                                ],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='@', kind=None),
                                        ops=[NotIn()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='message', ctx=Load()),
                                                slice=Constant(value='To', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssertionError', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='NO_VALID_RECIPIENT',
                                                        ctx=Load(),
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='sim_error', ctx=Load()),
                                            Compare(
                                                left=Name(id='sim_error', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='send_assert', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssertionError', ctx=Load()),
                                                args=[Constant(value='AssertionError', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='sim_error', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='sim_error', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='send_disconnect', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='SMTPServerDisconnected', ctx=Load()),
                                                        args=[Constant(value='SMTPServerDisconnected', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='sim_error', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='sim_error', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='send_delivery', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='MailDeliveryException', ctx=Load()),
                                                                args=[Constant(value='MailDeliveryException', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='Message-Id', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='_mail_mail_create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='mail_create_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_mails',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                            name='_mail_mail_unlink',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='mail_unlink_sent',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='mail_unlink_origin', ctx=Load()),
                                                args=[
                                                    Name(id='model', ctx=Load()),
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='IrMailServer', ctx=Load()),
                                            Constant(value='connect', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='IrMailServer', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_ir_mail_server_connect', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='ir_mail_server_connect_mock', ctx=Store()),
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='IrMailServer', ctx=Load()),
                                            Constant(value='build_email', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='IrMailServer', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_ir_mail_server_build_email', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='ir_mail_server_build_email_mock', ctx=Store()),
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='IrMailServer', ctx=Load()),
                                            Constant(value='send_email', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='IrMailServer', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_ir_mail_server_send_email', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='ir_mail_server_send_email_mock', ctx=Store()),
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='MailMail', ctx=Load()),
                                            Constant(value='create', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='MailMail', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_mail_mail_create', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='_mail_mail_create_mock', ctx=Store()),
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='MailMail', ctx=Load()),
                                            Constant(value='unlink', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='MailMail', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_mail_mail_unlink', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='mail_mail_unlink_mock', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_init_mail_mock',
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
                                    attr='_mails',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_mails_args',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_new_mails',
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
                                        slice=Constant(value='mail.mail', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_init_mail_gateway',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='alias_domain',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='test.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='alias_catchall',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='catchall.test', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='alias_bounce',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='bounce.test', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='default_from',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='notifications', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.bounce.alias', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='alias_bounce',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.catchall.domain', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='alias_domain',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.catchall.alias', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='alias_catchall',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.default.from', kind=None),
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='default_from',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='mailer_daemon_email',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='formataddr', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='MAILER-DAEMON', kind=None),
                                            BinOp(
                                                left=Constant(value='%s@%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='alias_bounce',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='alias_domain',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='format',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='to', annotation=None, type_comment=None),
                            arg(arg='subject', annotation=None, type_comment=None),
                            arg(arg='email_from', annotation=None, type_comment=None),
                            arg(arg='return_path', annotation=None, type_comment=None),
                            arg(arg='cc', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='msg_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value='groups@example.com, other@gmail.com', kind=None),
                            Constant(value='Frogs', kind=None),
                            Constant(value='Sylvie Lelitre <test.sylvie.lelitre@agrolait.com>', kind=None),
                            Constant(value='', kind=None),
                            Constant(value='', kind=None),
                            Constant(value='', kind=None),
                            Constant(value='<1198923581.41972151344608186760.JavaMail@agrolait.com>', kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='template', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='subject',
                                        value=Name(id='subject', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='to',
                                        value=Name(id='to', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='cc',
                                        value=Name(id='cc', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='email_from',
                                        value=Name(id='email_from', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='return_path',
                                        value=Name(id='return_path', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=Name(id='extra', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='msg_id',
                                        value=Name(id='msg_id', ctx=Load()),
                                    ),
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
                    name='format_and_process',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='email_from', annotation=None, type_comment=None),
                            arg(arg='to', annotation=None, type_comment=None),
                            arg(arg='subject', annotation=None, type_comment=None),
                            arg(arg='cc', annotation=None, type_comment=None),
                            arg(arg='return_path', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='msg_id', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='target_model', annotation=None, type_comment=None),
                            arg(arg='target_field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value='Frogs', kind=None),
                            Constant(value='', kind=None),
                            Constant(value='', kind=None),
                            Constant(value='', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='mail.test.gateway', kind=None),
                            Constant(value='name', kind=None),
                        ],
                    ),
                    body=[
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
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='target_model', ctx=Load()),
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
                                                            Name(id='target_field', ctx=Load()),
                                                            Constant(value='=', kind=None),
                                                            Name(id='subject', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='msg_id', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='msg_id', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='<%.7f-test@iron.sky>', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='time', ctx=Load()),
                                                attr='time',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='mail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='to',
                                        value=Name(id='to', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='subject',
                                        value=Name(id='subject', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='cc',
                                        value=Name(id='cc', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='return_path',
                                        value=Name(id='return_path', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=Name(id='extra', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='email_from',
                                        value=Name(id='email_from', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='msg_id',
                                        value=Name(id='msg_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
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
                                        slice=Constant(value='mail.thread', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='message_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Name(id='mail', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='target_model', ctx=Load()),
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
                                                    Name(id='target_field', ctx=Load()),
                                                    Constant(value='=', kind=None),
                                                    Name(id='subject', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='gateway_reply_wrecord',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='use_in_reply_to', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Deprecated, remove in 14.4 ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gateway_mail_reply_wrecord',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Name(id='record', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='use_in_reply_to',
                                        value=Name(id='use_in_reply_to', ctx=Load()),
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
                    name='gateway_mail_reply_wrecord',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='use_in_reply_to', annotation=None, type_comment=None),
                            arg(arg='target_model', annotation=None, type_comment=None),
                            arg(arg='target_field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Simulate a reply through the mail gateway. Usage: giving a record,\n        find an email sent to him and use its message-ID to simulate a reply.\n\n        Some noise is added in References just to test some robustness. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mail_mail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_mail_mail_wrecord',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='use_in_reply_to', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='extra', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='In-Reply-To:\r\n\t%s\n', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='mail_mail', ctx=Load()),
                                            attr='message_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='disturbing_other_msg_id', ctx=Store())],
                                    value=Constant(value='<123456.654321@another.host.com>', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='extra', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='References:\r\n\t%s\n\r%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='mail_mail', ctx=Load()),
                                                    attr='message_id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='disturbing_other_msg_id', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='format_and_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Attribute(
                                        value=Name(id='mail_mail', ctx=Load()),
                                        attr='email_to',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='mail_mail', ctx=Load()),
                                        attr='reply_to',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='subject',
                                        value=BinOp(
                                            left=Constant(value='Re: %s', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='mail_mail', ctx=Load()),
                                                attr='subject',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=Name(id='extra', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='msg_id',
                                        value=BinOp(
                                            left=Constant(value='<123456.%s.%d@test.example.com>', kind=None),
                                            op=Mod(),
                                            right=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='target_model',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='target_model', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='target_field',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='target_field', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_rec_name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
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
                    name='gateway_mail_reply_wemail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='email_to', annotation=None, type_comment=None),
                            arg(arg='use_in_reply_to', annotation=None, type_comment=None),
                            arg(arg='target_model', annotation=None, type_comment=None),
                            arg(arg='target_field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Simulate a reply through the mail gateway. Usage: giving a record,\n        find an email sent to him and use its message-ID to simulate a reply.\n\n        Some noise is added in References just to test some robustness. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sent_mail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_sent_mail_wemail',
                                    ctx=Load(),
                                ),
                                args=[Name(id='email_to', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='use_in_reply_to', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='extra', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='In-Reply-To:\r\n\t%s\n', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='sent_mail', ctx=Load()),
                                            slice=Constant(value='message_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='disturbing_other_msg_id', ctx=Store())],
                                    value=Constant(value='<123456.654321@another.host.com>', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='extra', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='References:\r\n\t%s\n\r%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='sent_mail', ctx=Load()),
                                                    slice=Constant(value='message_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='disturbing_other_msg_id', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='format_and_process',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Subscript(
                                        value=Name(id='sent_mail', ctx=Load()),
                                        slice=Constant(value='email_to', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='sent_mail', ctx=Load()),
                                        slice=Constant(value='reply_to', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='subject',
                                        value=BinOp(
                                            left=Constant(value='Re: %s', kind=None),
                                            op=Mod(),
                                            right=Subscript(
                                                value=Name(id='sent_mail', ctx=Load()),
                                                slice=Constant(value='subject', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=Name(id='extra', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='target_model',
                                        value=Name(id='target_model', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='target_field',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='target_field', ctx=Load()),
                                                Constant(value='name', kind=None),
                                            ],
                                        ),
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
                    name='from_string',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='email', ctx=Load()),
                                    attr='message_from_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pycompat', ctx=Load()),
                                            attr='to_text',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='text', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='policy',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='email', ctx=Load()),
                                                attr='policy',
                                                ctx=Load(),
                                            ),
                                            attr='SMTP',
                                            ctx=Load(),
                                        ),
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
                    name='assertHtmlEqual',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fragment_fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='parser',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='html', ctx=Load()),
                                                attr='HTMLParser',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='encoding',
                                                    value=Constant(value='utf-8', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='create_parent',
                                        value=Constant(value='body', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='base_node', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='xpath',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='//base', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='base_node', ctx=Load()),
                                                    attr='getparent',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='base_node', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_node', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fragment_fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expected', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='create_parent',
                                        value=Constant(value='body', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='message', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Name(id='expected_node', ctx=Load()),
                                            Name(id='message', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tree', ctx=Load()),
                                            Name(id='expected_node', ctx=Load()),
                                        ],
                                        keywords=[],
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
                    name='_find_sent_mail_wemail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email_to', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find a sent email with a given list of recipients. Email should match\n        exactly the recipients.\n\n        :param email-to: a list of emails that will be compared to email_to\n          of sent emails (also a list of emails);\n\n        :return email: an email which is a dictionary mapping values given to\n          ``build_email``;\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='sent_email', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_mails',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='sent_email', ctx=Load()),
                                                    slice=Constant(value='email_to', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[Name(id='email_to', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='sent mail not found for email_to %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='email_to', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='sent_email', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_mail_mail_wid',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mail_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find a ``mail.mail`` record based on a given ID (used notably when having\n        mail ID in mailing traces).\n\n        :return mail: a ``mail.mail`` record generated during the mock and matching\n          given ID;\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_new_mails',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='mail', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='mail_id', ctx=Load())],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='mail.mail not found for ID %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='mail_id', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='mail', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_mail_mail_wpartners',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='mail_message', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find a mail.mail record based on various parameters, notably a list\n        of recipients (partners).\n\n        :param recipients: a ``res.partner`` recordset Check all of them are in mail\n          recipients to find the right mail.mail record;\n        :param status: state of mail.mail. If not void use it to filter mail.mail\n          record;\n        :param mail_message: optional check/filter on mail_message_id field aka\n          a ``mail.message`` record;\n        :param author: optional check/filter on author_id field aka a ``res.partner``\n          record;\n\n        :return mail: a ``mail.mail`` record generated during the mock and matching\n          given parameters and filters;\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_new_mails',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='author', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='author_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='author', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='mail_message', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='mail_message_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='mail_message', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='status', ctx=Load()),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='status', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='p', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='recipient_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='p', ctx=Store()),
                                                        iter=Name(id='recipients', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='mail.mail not found for message %s / status %s / recipients %s / author %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='mail_message', ctx=Load()),
                                                        Name(id='status', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='recipients', ctx=Load()),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='author', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='mail', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_mail_mail_wemail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='email_to', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='mail_message', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Find a mail.mail record based on various parameters, notably a list\n        of email to (string emails).\n\n        :param email_to: either matching mail.email_to value, either a mail sent\n          to a single recipient whose email is email_to;\n        :param status: state of mail.mail. If not void use it to filter mail.mail\n          record;\n        :param mail_message: optional check/filter on mail_message_id field aka\n          a ``mail.message`` record;\n        :param author: optional check/filter on author_id field aka a ``res.partner``\n          record;\n\n        :return mail: a ``mail.mail`` record generated during the mock and matching\n          given parameters and filters;\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_new_mails',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='author', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='author_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='author', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='mail_message', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='mail_message_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='mail_message', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='status', ctx=Load()),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Name(id='status', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='email_to',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='email_to', ctx=Load())],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='recipient_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='mail', ctx=Load()),
                                                            attr='email_to',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='recipient_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='email',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='email_to', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='mail.mail not found for email_to %s / status %s in %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='email_to', ctx=Load()),
                                                        Name(id='status', ctx=Load()),
                                                        Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                ListComp(
                                                                    elt=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='email_to',
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='m', ctx=Store()),
                                                                            iter=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_new_mails',
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
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='mail', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_mail_mail_wrecord',
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
                        Expr(
                            value=Constant(value=' Find a mail.mail record based on model / res_id of a record.\n\n        :return mail: a ``mail.mail`` record generated during the mock;\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_new_mails',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='res_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='mail.mail not found for record %s in %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='record', ctx=Load()),
                                                        Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                ListComp(
                                                                    elt=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='email_to',
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='m', ctx=Store()),
                                                                            iter=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_new_mails',
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
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='mail', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertMailMail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='check_mail_mail', annotation=None, type_comment=None),
                            arg(arg='mail_message', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                            arg(arg='email_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Assert mail.mail records are created and maybe sent as emails. Allow\n        asserting their content. Records to check are the one generated when\n        using mock (mail.mail and outgoing emails). This method takes partners\n        as source of record fetch and assert.\n\n        :param recipients: a ``res.partner`` recordset. See ``_find_mail_mail_wpartners``;\n        :param status: mail.mail state used to filter mails. If ``sent`` this method\n          also check that emails have been sent trough gateway;\n        :param mail_message: see ``_find_mail_mail_wpartners``;\n        :param author: see ``_find_mail_mail_wpartners``;\n        :param content: if given, check it is contained within mail html body;\n        :param fields_values: if given, should be a dictionary of field names /\n          values allowing to check ``mail.mail`` additional values (subject,\n          reply_to, ...);\n        :param email_values: if given, should be a dictionary of keys / values\n          allowing to check sent email additional values (if any).\n          See ``assertSentEmail``;\n\n        :param check_mail_mail: deprecated, use ``assertSentEmail`` if False\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='found_mail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_mail_mail_wpartners',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='recipients', ctx=Load()),
                                    Name(id='status', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='mail_message',
                                        value=Name(id='mail_message', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='author',
                                        value=Name(id='author', ctx=Load()),
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
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='found_mail', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='content', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='content', ctx=Load()),
                                            Attribute(
                                                value=Name(id='found_mail', ctx=Load()),
                                                attr='body_html',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='fname', ctx=Store()),
                                    Name(id='fvalue', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='fields_values', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='found_mail', ctx=Load()),
                                                slice=Name(id='fname', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='fvalue', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Mail: expected %s for %s, got %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='fvalue', ctx=Load()),
                                                        Name(id='fname', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='found_mail', ctx=Load()),
                                                            slice=Name(id='fname', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='status', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sent', kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='recipient', ctx=Store()),
                                    iter=Name(id='recipients', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertSentEmail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    IfExp(
                                                        test=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Name(id='email_values', ctx=Load()),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='email_values', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='email_from', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        body=Subscript(
                                                            value=Name(id='email_values', ctx=Load()),
                                                            slice=Constant(value='email_from', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Name(id='author', ctx=Load()),
                                                    ),
                                                    List(
                                                        elts=[Name(id='recipient', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Name(id='email_values', ctx=Load()),
                                                                Dict(keys=[], values=[]),
                                                            ],
                                                        ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertMailMailWEmails',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='emails', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='mail_message', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                            arg(arg='email_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Assert mail.mail records are created and maybe sent as emails. Allow\n        asserting their content. Records to check are the one generated when\n        using mock (mail.mail and outgoing emails). This method takes emails\n        as source of record fetch and assert.\n\n        :param emails: a list of emails. See ``_find_mail_mail_wemail``;\n        :param status: mail.mail state used to filter mails. If ``sent`` this method\n          also check that emails have been sent trough gateway;\n        :param mail_message: see ``_find_mail_mail_wemail``;\n        :param author: see ``_find_mail_mail_wemail``;;\n        :param content: if given, check it is contained within mail html body;\n        :param fields_values: if given, should be a dictionary of field names /\n          values allowing to check ``mail.mail`` additional values (subject,\n          reply_to, ...);\n        :param email_values: if given, should be a dictionary of keys / values\n          allowing to check sent email additional values (if any).\n          See ``assertSentEmail``;\n\n        :param check_mail_mail: deprecated, use ``assertSentEmail`` if False\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='email_to', ctx=Store()),
                            iter=Name(id='emails', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='found_mail', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_find_mail_mail_wemail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='email_to', ctx=Load()),
                                            Name(id='status', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mail_message',
                                                value=Name(id='mail_message', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='author',
                                                value=Name(id='author', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='content', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='content', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='found_mail', ctx=Load()),
                                                        attr='body_html',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='fname', ctx=Store()),
                                            Name(id='fvalue', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='fields_values', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='found_mail', ctx=Load()),
                                                        slice=Name(id='fname', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='fvalue', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='Mail: expected %s for %s, got %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='fvalue', ctx=Load()),
                                                                Name(id='fname', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='found_mail', ctx=Load()),
                                                                    slice=Name(id='fname', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
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
                        If(
                            test=Compare(
                                left=Name(id='status', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sent', kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='email_to', ctx=Store()),
                                    iter=Name(id='emails', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertSentEmail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    IfExp(
                                                        test=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Name(id='email_values', ctx=Load()),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='email_values', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='email_from', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        body=Subscript(
                                                            value=Name(id='email_values', ctx=Load()),
                                                            slice=Constant(value='email_from', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Name(id='author', ctx=Load()),
                                                    ),
                                                    List(
                                                        elts=[Name(id='email_to', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg=None,
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Name(id='email_values', ctx=Load()),
                                                                Dict(keys=[], values=[]),
                                                            ],
                                                        ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertMailMailWId',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='mail_id', annotation=None, type_comment=None),
                            arg(arg='status', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='fields_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Assert mail.mail records are created and maybe sent as emails. Allow\n        asserting their content. Records to check are the one generated when\n        using mock (mail.mail and outgoing emails). This method takes partners\n        as source of record fetch and assert.\n\n        :param mail_id: a ``mail.mail`` DB ID. See ``_find_mail_mail_wid``;\n        :param status: mail.mail state to check upon found mail;\n        :param content: if given, check it is contained within mail html body;\n        :param fields_values: if given, should be a dictionary of field names /\n          values allowing to check ``mail.mail`` additional values (subject,\n          reply_to, ...);\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='found_mail', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_mail_mail_wid',
                                    ctx=Load(),
                                ),
                                args=[Name(id='mail_id', ctx=Load())],
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
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='found_mail', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='status', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='found_mail', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            Name(id='status', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='content', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='content', ctx=Load()),
                                            Attribute(
                                                value=Name(id='found_mail', ctx=Load()),
                                                attr='body_html',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='fname', ctx=Store()),
                                    Name(id='fvalue', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='fields_values', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='found_mail', ctx=Load()),
                                                slice=Name(id='fname', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Name(id='fvalue', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Mail: expected %s for %s, got %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='fvalue', ctx=Load()),
                                                        Name(id='fname', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='found_mail', ctx=Load()),
                                                            slice=Name(id='fname', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                    name='assertNoMail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients', annotation=None, type_comment=None),
                            arg(arg='mail_message', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check no mail.mail and email was generated during gateway mock. ', kind=None),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_find_mail_mail_wpartners',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='recipients', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mail_message',
                                                value=Name(id='mail_message', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='author',
                                                value=Name(id='author', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AssertionError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AssertionError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='mail.mail exists for message %s / recipients %s but should not exist', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='mail_message', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='recipients', ctx=Load()),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotSentEmail',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='assertNotSentEmail',
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
                            value=Constant(value=' Check no email was generated during gateway mock. ', kind=None),
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
                                                value=Name(id='self', ctx=Load()),
                                                attr='_mails',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                    name='assertSentEmail',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                            arg(arg='recipients', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='values', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Tool method to ease the check of send emails.\n\n        :param author: email author, either a string (email), either a partner\n          record;\n        :param recipients: list of recipients, each being either a string (email),\n          either a partner record;\n        :param values: dictionary of additional values to check email content;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='base_expected', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='fname', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='reply_to', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='attachments', kind=None),
                                    Constant(value='body', kind=None),
                                    Constant(value='references', kind=None),
                                    Constant(value='body_content', kind=None),
                                    Constant(value='body_alternative_content', kind=None),
                                    Constant(value='references_content', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='fname', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='base_expected', ctx=Load()),
                                                    slice=Name(id='fname', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Name(id='fname', ctx=Load()),
                                                ctx=Load(),
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
                            targets=[Name(id='expected', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='base_expected', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='author', ctx=Load()),
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='__class__',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='expected', ctx=Load()),
                                            slice=Constant(value='email_from', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='formataddr', ctx=Load()),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='author', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='author', ctx=Load()),
                                                        attr='email',
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
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='expected', ctx=Load()),
                                            slice=Constant(value='email_from', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='author', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='email_to_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='email_to', ctx=Store()),
                            iter=Name(id='recipients', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='email_to', ctx=Load()),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.partner', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='__class__',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='email_to_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='formataddr', ctx=Load()),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='email_to', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='email_to', ctx=Load()),
                                                                        attr='email',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='email_to_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email_to', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='expected', ctx=Load()),
                                    slice=Constant(value='email_to', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='email_to_list', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sent_mail', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='mail', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='mail', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_mails',
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='mail', ctx=Load()),
                                                                            slice=Constant(value='email_to', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Name(id='set', ctx=Load()),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='expected', ctx=Load()),
                                                                                slice=Constant(value='email_to', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='mail', ctx=Load()),
                                                                    slice=Constant(value='email_from', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Name(id='expected', ctx=Load()),
                                                                        slice=Constant(value='email_from', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='debug_info', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='sent_mail', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Constant(value='-', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        GeneratorExp(
                                            elt=BinOp(
                                                left=Constant(value='From: %s-To: %s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='mail', ctx=Load()),
                                                            slice=Constant(value='email_from', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='mail', ctx=Load()),
                                                            slice=Constant(value='email_to', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='mail', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_mails',
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
                                orelse=Constant(value='', kind=None),
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
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='sent_mail', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Constant(value='Expected mail from %s to %s not found in %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='expected', ctx=Load()),
                                                    slice=Constant(value='email_from', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='expected', ctx=Load()),
                                                    slice=Constant(value='email_to', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='debug_info', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='val', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='reply_to', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='references', kind=None),
                                    Constant(value='attachments', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='val', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='expected', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='expected', ctx=Load()),
                                                        slice=Name(id='val', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='sent_mail', ctx=Load()),
                                                        slice=Name(id='val', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Value for %s: expected %s, received %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='val', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='expected', ctx=Load()),
                                                                    slice=Name(id='val', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='sent_mail', ctx=Load()),
                                                                    slice=Name(id='val', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                            test=Compare(
                                left=Constant(value='attachments_info', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attachments', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='sent_mail', ctx=Load()),
                                        slice=Constant(value='attachments', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='attachment_info', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='attachments_info', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attachment', ctx=Store())],
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='attach', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='attach', ctx=Store()),
                                                                iter=Name(id='attachments', ctx=Load()),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='attach', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Subscript(
                                                                                value=Name(id='attachment_info', ctx=Load()),
                                                                                slice=Constant(value='name', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='attachment_info', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='raw', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='attachment_info', ctx=Load()),
                                                                slice=Constant(value='raw', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='attachment_info', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='type', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                slice=Constant(value=2, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='attachment_info', ctx=Load()),
                                                                slice=Constant(value='type', kind=None),
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
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='attachments_info', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='attachments', ctx=Load())],
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
                            target=Name(id='val', ctx=Store()),
                            iter=List(
                                elts=[Constant(value='body', kind=None)],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='val', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='expected', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertHtmlEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='expected', ctx=Load()),
                                                        slice=Name(id='val', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='sent_mail', ctx=Load()),
                                                        slice=Name(id='val', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Value for %s: expected %s, received %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='val', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='expected', ctx=Load()),
                                                                    slice=Name(id='val', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='sent_mail', ctx=Load()),
                                                                    slice=Name(id='val', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                        For(
                            target=Name(id='val', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='body_content', kind=None),
                                    Constant(value='body_alternative', kind=None),
                                    Constant(value='references_content', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='val', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='expected', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='expected', ctx=Load()),
                                                        slice=Name(id='val', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='sent_mail', ctx=Load()),
                                                        slice=Subscript(
                                                            value=Name(id='val', ctx=Load()),
                                                            slice=Slice(
                                                                lower=None,
                                                                upper=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=8, kind=None),
                                                                ),
                                                                step=None,
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='Value for %s: %s does not contain %s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='val', ctx=Load()),
                                                                Subscript(
                                                                    value=Name(id='sent_mail', ctx=Load()),
                                                                    slice=Subscript(
                                                                        value=Name(id='val', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=None,
                                                                            upper=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=8, kind=None),
                                                                            ),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='expected', ctx=Load()),
                                                                    slice=Name(id='val', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MailCase',
            bases=[Name(id='MockEmail', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Tools, helpers and asserts for mail-related tests, including mail\n    gateway mock and helpers (see ´´MockEmail´´).\n\n    Useful reminders\n        Notif type:  (\'inbox\', \'Inbox\'), (\'email\', \'Email\')\n        Notif status: (\'ready\', \'Ready to Send\'), (\'sent\', \'Sent\'),\n                      (\'bounce\', \'Bounced\'), (\'exception\', \'Exception\'),\n                      (\'canceled\', \'Canceled\')\n        Notif failure type: ("SMTP", "Connection failed (outgoing mail server problem)"),\n                            ("RECIPIENT", "Invalid email address"),\n                            ("BOUNCE", "Email address rejected by destination"),\n                            ("UNKNOWN", "Unknown error")\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_test_context', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='mail_create_nolog', kind=None),
                            Constant(value='mail_create_nosubscribe', kind=None),
                            Constant(value='mail_notrack', kind=None),
                            Constant(value='no_reset_password', kind=None),
                        ],
                        values=[
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_reset_mail_context',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                        ],
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
                                    value=Name(id='record', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='mail_create_nolog',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='mail_create_nosubscribe',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='mail_notrack',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='flush_tracking',
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
                            value=Constant(value=' Force the creation of tracking values. ', kind=None),
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
                                        slice=Constant(value='base', kind=None),
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='flush',
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
                    name='mock_bus',
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
                            targets=[Name(id='bus_bus_create_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='ImBus', ctx=Load()),
                                attr='create',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_init_mock_bus',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='_bus_bus_create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='bus_bus_create_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_bus_notifs',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ImBus', ctx=Load()),
                                            Constant(value='create', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='ImBus', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_bus_bus_create', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='_bus_bus_create_mock', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_init_mock_bus',
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
                                    attr='_new_bus_notifs',
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
                                        slice=Constant(value='bus.bus', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_reset_bus',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='mock_mail_app',
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
                            targets=[Name(id='message_create_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='Message', ctx=Load()),
                                attr='create',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notification_create_origin', ctx=Store())],
                            value=Attribute(
                                value=Name(id='MailNotification', ctx=Load()),
                                attr='create',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_init_mock_mail',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        FunctionDef(
                            name='_mail_message_create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='message_create_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_msgs',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                            name='_mail_notification_create',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='model', annotation=None, type_comment=None)],
                                vararg=arg(arg='args', annotation=None, type_comment=None),
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Name(id='notification_create_origin', ctx=Load()),
                                        args=[
                                            Name(id='model', ctx=Load()),
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
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_notifs',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='Message', ctx=Load()),
                                            Constant(value='create', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='Message', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_mail_message_create', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='_mail_message_create_mock', ctx=Store()),
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='patch', ctx=Load()),
                                            attr='object',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='MailNotification', ctx=Load()),
                                            Constant(value='create', kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='autospec',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='wraps',
                                                value=Name(id='MailNotification', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='side_effect',
                                                value=Name(id='_mail_notification_create', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='_mail_notification_create_mock', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_init_mock_mail',
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
                                    attr='_new_msgs',
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
                                        slice=Constant(value='mail.message', kind=None),
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_new_notifs',
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
                                        slice=Constant(value='mail.notification', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_messages',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='body_content', annotation=None, type_comment=None),
                            arg(arg='count', annotation=None, type_comment=None),
                            arg(arg='author', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Helper: add #count messages in record history ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='author', ctx=Store())],
                            value=IfExp(
                                test=Name(id='author', ctx=Load()),
                                body=Name(id='author', ctx=Load()),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='partner_id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='email_from', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='kwargs', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='kwargs', ctx=Load()),
                                            slice=Constant(value='email_from', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='author', ctx=Load()),
                                        attr='email_formatted',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='subtype_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='subtype_id', kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='mail.mt_comment', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='author_id', kind=None),
                                    Constant(value='subtype_id', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='author', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='subtype_id', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[Name(id='kwargs', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='create_vals', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[Name(id='values', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='body',
                                            value=BinOp(
                                                left=Constant(value='%s/%02d', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='body_content', ctx=Load()),
                                                        Name(id='counter', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='counter', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[Name(id='count', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mail.message', kind=None),
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
                                args=[Name(id='create_vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='template_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='create_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='subject', kind=None),
                                    Constant(value='body_html', kind=None),
                                    Constant(value='model_id', kind=None),
                                ],
                                values=[
                                    Constant(value='TestTemplate', kind=None),
                                    Constant(value='About {{ object.name }}', kind=None),
                                    Constant(value='<p>Hello <t t-out="object.name"/></p>', kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.model', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='_get',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='model', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='template_values', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='create_values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='email_template',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='create_values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='email_template',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_notify_recipients',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partners', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Tool method to generate recipients data according to structure used\n        in notification methods. Purpose is to allow testing of internals of\n        some notification methods, notably testing links or group-based notification\n        details.\n\n        See notably ``MailThread._notify_compute_recipients()``.\n        ', kind=None),
                        ),
                        Return(
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='id', kind=None),
                                        Constant(value='active', kind=None),
                                        Constant(value='share', kind=None),
                                        Constant(value='groups', kind=None),
                                        Constant(value='notif', kind=None),
                                        Constant(value='type', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Constant(value=True, kind=None),
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='partner_share',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='user_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='groups_id',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='user_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='notification_type',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='email', kind=None),
                                            ],
                                        ),
                                        IfExp(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='user_ids',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='partner_share',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=Constant(value='user', kind=None),
                                            orelse=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='user_ids',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='portal', kind=None),
                                                        ],
                                                    ),
                                                    Constant(value='customer', kind=None),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='partner', ctx=Store()),
                                        iter=Name(id='partners', ctx=Load()),
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
                FunctionDef(
                    name='assertSinglePostNotifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='message_info', annotation=None, type_comment=None),
                            arg(arg='mail_unlink_sent', annotation=None, type_comment=None),
                            arg(arg='sim_error', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut to assertMsgNotifications when having a single message to check. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='r_info', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    IfExp(
                                        test=Name(id='message_info', ctx=Load()),
                                        body=Name(id='message_info', ctx=Load()),
                                        orelse=Dict(keys=[], values=[]),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='r_info', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='content', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='r_info', ctx=Load()),
                                    slice=Constant(value='notif', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='recipients_info', ctx=Load()),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertPostNotifications',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Name(id='r_info', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mail_unlink_sent',
                                                value=Name(id='mail_unlink_sent', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='sim_error',
                                                value=Name(id='sim_error', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Yield(value=None),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertPostNotifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='mail_unlink_sent', annotation=None, type_comment=None),
                            arg(arg='sim_error', annotation=None, type_comment=None),
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
                            value=Constant(value=' Check content of notifications. ', kind=None),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_mail_gateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_unlink_sent',
                                                        value=Name(id='mail_unlink_sent', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='sim_error',
                                                        value=Name(id='sim_error', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_bus',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_mail_app',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Yield(value=None),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='done_msgs', ctx=Store()),
                                                Name(id='done_notifs', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertMailNotifications',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_new_msgs',
                                                ctx=Load(),
                                            ),
                                            Name(id='recipients_info', ctx=Load()),
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
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_new_msgs',
                                                ctx=Load(),
                                            ),
                                            Name(id='done_msgs', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Mail: invalid message creation (%s) / expected (%s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_new_msgs',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='done_msgs', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                                                value=Name(id='self', ctx=Load()),
                                                attr='_new_notifs',
                                                ctx=Load(),
                                            ),
                                            Name(id='done_notifs', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Mail: invalid notification creation (%s) / expected (%s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_new_notifs',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='done_notifs', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertBus',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channels', annotation=None, type_comment=None),
                            arg(arg='message_items', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Check content of bus notifications. ', kind=None),
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_bus',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Yield(value=None),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Assign(
                                    targets=[Name(id='found_bus_notifs', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertBusNotifications',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='channels', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='message_items',
                                                value=Name(id='message_items', ctx=Load()),
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
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_new_bus_notifs',
                                                ctx=Load(),
                                            ),
                                            Name(id='found_bus_notifs', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertNoNotifications',
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
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_mail_gateway',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_unlink_sent',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='sim_error',
                                                        value=Constant(value=None, kind=None),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_bus',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mock_mail_app',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Yield(value=None),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertFalse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_new_msgs',
                                                        ctx=Load(),
                                                    ),
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
                                            attr='assertFalse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_new_notifs',
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
                        ),
                    ],
                    decorator_list=[Name(id='contextmanager', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertMailNotifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='messages', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check bus notifications content. Mandatory and basic check is about\n        channels being notified. Content check is optional.\n\n        GNERATED INPUT\n        :param messages: generated messages to check;\n\n        EXPECTED\n        :param recipients_info: list of data dict: [\n          {'content': message content,\n           'message_type': message_type (default: 'comment'),\n           'subtype': xml id of message subtype (default: 'mail.mt_comment'),\n           'notif': list of notified recipients: [\n             {'partner': res.partner record (may be empty),\n              'email': NOT SUPPORTED YET,\n              'status': notification_status to check,\n              'type': notification_type to check,\n              'is_read': is_read to check,\n              'check_send': whether outgoing stuff has to be checked;\n              'failure_type': optional: one of failure_type key\n             }, { ... }]\n          }, {...}]\n\n        PARAMETERS\n        :param unlink_sent: to know whether to compute\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
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
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='concat',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Subscript(
                                                        value=Name(id='p', ctx=Load()),
                                                        slice=Constant(value='partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='i', ctx=Store()),
                                                            iter=Name(id='recipients_info', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                        comprehension(
                                                            target=Name(id='p', ctx=Store()),
                                                            iter=Subscript(
                                                                value=Name(id='i', ctx=Load()),
                                                                slice=Constant(value='notif', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ifs=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='p', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='partner', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='res_partner_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='partners', ctx=Load()),
                                                attr='ids',
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
                        If(
                            test=Compare(
                                left=Name(id='messages', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='base_domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='mail_message_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='messages', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='notifications', ctx=Store())],
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
                                                slice=Constant(value='mail.notification', kind=None),
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
                                args=[Name(id='base_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='done_msgs', ctx=Store())],
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
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='done_notifs', ctx=Store())],
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
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='message_info', ctx=Store()),
                            iter=Name(id='recipients_info', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='mbody', ctx=Store()),
                                                Name(id='mtype', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='message_info', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='content', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='message_info', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='message_type', kind=None),
                                                    Constant(value='comment', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='msubtype', ctx=Store())],
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
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='message_info', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='subtype', kind=None),
                                                    Constant(value='mail.mt_comment', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='messages', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='messages', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='message', annotation=None, type_comment=None)],
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
                                                                    left=Name(id='mbody', ctx=Load()),
                                                                    ops=[In()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='message', ctx=Load()),
                                                                            attr='body',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='message_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='mtype', ctx=Load())],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='subtype_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='msubtype', ctx=Load())],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
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
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='body', kind=None),
                                                                    Constant(value='ilike', kind=None),
                                                                    Name(id='mbody', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='message_type', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='mtype', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='subtype_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='msubtype', ctx=Load()),
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
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='id DESC', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='message', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Mail: not found message (content: %s, message_type: %s, subtype: %s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='mbody', ctx=Load()),
                                                        Name(id='mtype', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='msubtype', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='email_groups', ctx=Store())],
                                    value=Call(
                                        func=Name(id='defaultdict', ctx=Load()),
                                        args=[Name(id='list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mail_groups', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='failure', kind=None)],
                                        values=[List(elts=[], ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='recipient', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='message_info', ctx=Load()),
                                        slice=Constant(value='notif', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='partner', ctx=Store()),
                                                        Name(id='ntype', ctx=Store()),
                                                        Name(id='ngroup', ctx=Store()),
                                                        Name(id='nstatus', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='recipient', ctx=Load()),
                                                        slice=Constant(value='partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='recipient', ctx=Load()),
                                                        slice=Constant(value='type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='recipient', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='group', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='recipient', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='status', kind=None),
                                                            Constant(value='sent', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='nis_read', ctx=Store()),
                                                        Name(id='ncheck_send', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='recipient', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='is_read', kind=None),
                                                            IfExp(
                                                                test=Compare(
                                                                    left=Subscript(
                                                                        value=Name(id='recipient', ctx=Load()),
                                                                        slice=Constant(value='type', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='inbox', kind=None)],
                                                                ),
                                                                body=Constant(value=False, kind=None),
                                                                orelse=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='recipient', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='check_send', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='ngroup', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ngroup', ctx=Store())],
                                                    value=Constant(value='user', kind=None),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='partner', ctx=Load()),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='user_ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='ngroup', ctx=Store())],
                                                            value=Constant(value='customer', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='partner', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='partner_share',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='ngroup', ctx=Store())],
                                                                    value=Constant(value='portal', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='partner_notif', ctx=Store())],
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
                                                                        attr='mail_message_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='message', ctx=Load())],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='res_partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='partner', ctx=Load())],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='notification_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='ntype', ctx=Load())],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='notification_status',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='nstatus', ctx=Load())],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='is_read',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='nis_read', ctx=Load())],
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
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertTrue',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='partner_notif', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='Mail: not found notification for %s (type: %s, state: %s, message: %s)', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='partner', ctx=Load()),
                                                                Name(id='ntype', ctx=Load()),
                                                                Name(id='nstatus', ctx=Load()),
                                                                Attribute(
                                                                    value=Name(id='message', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='ntype', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='email', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='nstatus', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='sent', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Name(id='ncheck_send', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='email_groups', ctx=Load()),
                                                                                slice=Name(id='ngroup', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='partner', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='nstatus', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='exception', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='mail_groups', ctx=Load()),
                                                                                slice=Constant(value='failure', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='partner', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=Name(id='ncheck_send', ctx=Load()),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='email_groups', ctx=Load()),
                                                                                        slice=Name(id='ngroup', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='partner', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='nstatus', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='canceled', kind=None)],
                                                                    ),
                                                                    body=[Pass()],
                                                                    orelse=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='NotImplementedError', ctx=Load()),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
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
                                        AugAssign(
                                            target=Name(id='done_notifs', ctx=Store()),
                                            op=BitOr(),
                                            value=Name(id='partner_notif', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='done_msgs', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='message', ctx=Load()),
                                ),
                                Assign(
                                    targets=[Name(id='bus_notifications', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='message', ctx=Load()),
                                                        attr='notification_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_filtered_for_web_client',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='n', ctx=Load()),
                                                        attr='notification_status',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='exception', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='bus_notifications', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertMessageBusNotifications',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='message', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='recipients', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='email_groups', ctx=Load()),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partners', ctx=Store())],
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
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='concat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=Name(id='recipients', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='p', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                Subscript(
                                                                    value=Name(id='mail_groups', ctx=Load()),
                                                                    slice=Constant(value='failure', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='p', ctx=Store()),
                                                                iter=Name(id='partners', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='mail_unlink_sent',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertMailMail',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partners', ctx=Load()),
                                                                    Constant(value='exception', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='author',
                                                                        value=Attribute(
                                                                            value=Name(id='message', ctx=Load()),
                                                                            attr='author_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='mail_message',
                                                                        value=Name(id='message', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        For(
                                                            target=Name(id='recipient', ctx=Store()),
                                                            iter=Name(id='partners', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='assertSentEmail',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='message', ctx=Load()),
                                                                                attr='author_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            List(
                                                                                elts=[Name(id='recipient', ctx=Load())],
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
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='mail_unlink_sent',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertMailMail',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='partners', ctx=Load()),
                                                                    Constant(value='sent', kind=None),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='author',
                                                                        value=IfExp(
                                                                            test=Attribute(
                                                                                value=Name(id='message', ctx=Load()),
                                                                                attr='author_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            body=Attribute(
                                                                                value=Name(id='message', ctx=Load()),
                                                                                attr='author_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            orelse=Attribute(
                                                                                value=Name(id='message', ctx=Load()),
                                                                                attr='email_from',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='mail_message',
                                                                        value=Name(id='message', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='email_values',
                                                                        value=Dict(
                                                                            keys=[Constant(value='body_content', kind=None)],
                                                                            values=[Name(id='mbody', ctx=Load())],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        For(
                                                            target=Name(id='recipient', ctx=Store()),
                                                            iter=Name(id='partners', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='assertSentEmail',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            IfExp(
                                                                                test=Attribute(
                                                                                    value=Name(id='message', ctx=Load()),
                                                                                    attr='author_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                body=Attribute(
                                                                                    value=Name(id='message', ctx=Load()),
                                                                                    attr='author_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                orelse=Attribute(
                                                                                    value=Name(id='message', ctx=Load()),
                                                                                    attr='email_from',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            List(
                                                                                elts=[Name(id='recipient', ctx=Load())],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='email_values',
                                                                                value=Dict(
                                                                                    keys=[Constant(value='body_content', kind=None)],
                                                                                    values=[Name(id='mbody', ctx=Load())],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='any', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Name(id='p', ctx=Load()),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='recipients', ctx=Store()),
                                                            iter=Call(
                                                                func=Attribute(
                                                                    value=Name(id='email_groups', ctx=Load()),
                                                                    attr='values',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                        comprehension(
                                                            target=Name(id='p', ctx=Store()),
                                                            iter=Name(id='recipients', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertNoMail',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='partners', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='mail_message',
                                                        value=Name(id='message', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='author',
                                                        value=Attribute(
                                                            value=Name(id='message', ctx=Load()),
                                                            attr='author_id',
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
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='done_msgs', ctx=Load()),
                                    Name(id='done_notifs', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertMessageBusNotifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Asserts that the expected notification updates have been sent on the\n        bus for the given message.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertBusNotifications',
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
                                                            value=Name(id='message', ctx=Load()),
                                                            attr='author_id',
                                                            ctx=Load(),
                                                        ),
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
                                                    Constant(value='mail.message/notification_update', kind=None),
                                                    Dict(
                                                        keys=[Constant(value='elements', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='message', ctx=Load()),
                                                                    attr='_message_notification_format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='check_unique',
                                        value=Constant(value=False, kind=None),
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
                    name='assertBusNotifications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channels', annotation=None, type_comment=None),
                            arg(arg='message_items', annotation=None, type_comment=None),
                            arg(arg='check_unique', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Check bus notifications content. Mandatory and basic check is about\n        channels being notified. Content check is optional.\n\n        EXPECTED\n        :param channels: list of expected bus channels, like [\n          (self.cr.dbname, 'mail.channel', self.channel_1.id),\n          (self.cr.dbname, 'res.partner', self.partner_employee_2.id)\n        ]\n        :param message_items: if given, list of expected message making a valid\n          pair (channel, message) to be found in bus.bus, like [\n            {'type': 'mail.message/notification_update',\n             'elements': {self.msg.id: {\n                'message_id': self.msg.id,\n                'message_type': 'sms',\n                'notifications': {...},\n                ...\n              }}\n            }, {...}]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='bus_notifs', ctx=Store())],
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
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='channel', kind=None),
                                                    Constant(value='in', kind=None),
                                                    ListComp(
                                                        elt=Call(
                                                            func=Name(id='json_dump', ctx=Load()),
                                                            args=[Name(id='channel', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='channel', ctx=Store()),
                                                                iter=Name(id='channels', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='check_unique', ctx=Load()),
                            body=[
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
                                                args=[Name(id='bus_notifs', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='channels', ctx=Load())],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='bus_notifs', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='channel', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Call(
                                                    func=Name(id='json_dump', ctx=Load()),
                                                    args=[Name(id='channel', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='channel', ctx=Store()),
                                                        iter=Name(id='channels', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='notif_messages', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='n', ctx=Load()),
                                    attr='message',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='n', ctx=Store()),
                                        iter=Name(id='bus_notifs', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='expected', ctx=Store()),
                            iter=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='message_items', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='notification', ctx=Store()),
                                    iter=Name(id='notif_messages', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='json_dump', ctx=Load()),
                                                    args=[Name(id='expected', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='notification', ctx=Load())],
                                            ),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssertionError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='No notification was found with the expected value.\nExpected:\n%s\nReturned:\n%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Call(
                                                                    func=Name(id='json_dump', ctx=Load()),
                                                                    args=[Name(id='expected', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Constant(value='\n', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        ListComp(
                                                                            elt=Name(id='n', ctx=Load()),
                                                                            generators=[
                                                                                comprehension(
                                                                                    target=Name(id='n', ctx=Store()),
                                                                                    iter=Name(id='notif_messages', ctx=Load()),
                                                                                    ifs=[],
                                                                                    is_async=0,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='bus_notifs', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertNotified',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='recipients_info', annotation=None, type_comment=None),
                            arg(arg='is_complete', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Lightweight check for notifications (mail.notification).\n\n        :param recipients_info: list notified recipients: [\n          {'partner': res.partner record (may be empty),\n           'type': notification_type to check,\n           'is_read': is_read to check,\n          }, {...}]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='notifications', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_new_notifs',
                                        ctx=Load(),
                                    ),
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
                                            left=Name(id='notif', ctx=Load()),
                                            ops=[In()],
                                            comparators=[
                                                Attribute(
                                                    value=Name(id='message', ctx=Load()),
                                                    attr='notification_ids',
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
                        If(
                            test=Name(id='is_complete', ctx=Load()),
                            body=[
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
                                                args=[Name(id='notifications', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='recipients_info', ctx=Load())],
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
                            target=Name(id='rinfo', ctx=Store()),
                            iter=Name(id='recipients_info', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='recipient_notif', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='notif', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='notif', ctx=Store()),
                                                        iter=Name(id='notifications', ctx=Load()),
                                                        ifs=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='notif', ctx=Load()),
                                                                    attr='res_partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Subscript(
                                                                        value=Name(id='rinfo', ctx=Load()),
                                                                        slice=Constant(value='partner', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
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
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='recipient_notif', ctx=Load())],
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
                                                value=Name(id='recipient_notif', ctx=Load()),
                                                attr='is_read',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='rinfo', ctx=Load()),
                                                slice=Constant(value='is_read', kind=None),
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
                                                value=Name(id='recipient_notif', ctx=Load()),
                                                attr='notification_type',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='rinfo', ctx=Load()),
                                                slice=Constant(value='type', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertTracking',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tracking_values', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='message', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='tracking_value_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='field_name', ctx=Store()),
                                    Name(id='value_type', ctx=Store()),
                                    Name(id='old_value', ctx=Store()),
                                    Name(id='new_value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='tracking', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tracking_values', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='track', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='track', ctx=Load()),
                                                            attr='field',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='field_name', ctx=Load())],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='tracking', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='value_type', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='char', kind=None),
                                                    Constant(value='integer', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='tracking', ctx=Load()),
                                                        attr='old_value_char',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='old_value', ctx=Load()),
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
                                                        value=Name(id='tracking', ctx=Load()),
                                                        attr='new_value_char',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='new_value', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='value_type', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Constant(value='many2one', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='tracking', ctx=Load()),
                                                                attr='old_value_integer',
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='old_value', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='old_value', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
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
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='tracking', ctx=Load()),
                                                                attr='new_value_integer',
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='new_value', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='new_value', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
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
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='tracking', ctx=Load()),
                                                                attr='old_value_char',
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='old_value', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='old_value', ctx=Load()),
                                                                                attr='display_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value='', kind=None),
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
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='tracking', ctx=Load()),
                                                                attr='new_value_char',
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='new_value', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='new_value', ctx=Load()),
                                                                                attr='display_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='value_type', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Constant(value='monetary', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertEqual',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='tracking', ctx=Load()),
                                                                        attr='old_value_monetary',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='old_value', ctx=Load()),
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
                                                                        value=Name(id='tracking', ctx=Load()),
                                                                        attr='new_value_monetary',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='new_value', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='assertEqual',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=0, kind=None),
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='MailCommon',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
                Name(id='MailCase', ctx=Load()),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Almost-void class definition setting the savepoint case + mock of mail.\n    Used mainly for class inheritance in other applications and test modules. ', kind=None),
                ),
                FunctionDef(
                    name='setUpClass',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='MailCommon', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_init_mail_gateway',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_admin',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.user_admin', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='user_admin',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='notification_type', kind=None)],
                                        values=[Constant(value='inbox', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_admin',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.partner_admin', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_admin',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_admin',
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='company_admin',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='email', kind=None)],
                                        values=[Constant(value='company@example.com', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_root',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.user_root', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_root',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_root',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.restrict.template.rendering', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_employee',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='employee', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user,mail.group_mail_template_editor', kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_admin',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Ernest Employee', kind=None),
                                    ),
                                    keyword(
                                        arg='notification_type',
                                        value=Constant(value='inbox', kind=None),
                                    ),
                                    keyword(
                                        arg='signature',
                                        value=Constant(value='--\nErnest', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_employee',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_employee',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_portal_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_portal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='portal_test', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_portal', kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_admin',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Chell Gladys', kind=None),
                                    ),
                                    keyword(
                                        arg='notification_type',
                                        value=Constant(value='email', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_portal',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_portal',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='user_portal',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_activate_multi_company',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create another company, add it to admin and create an user that\n        belongs to that new company. It allows to test flows with users from\n        different companies. ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='company_2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
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
                                            Constant(value='Company 2', kind=None),
                                            Constant(value='company_2@test.example.com', kind=None),
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
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='user_admin',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='company_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='company_2',
                                                                    ctx=Load(),
                                                                ),
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
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_employee_c2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='mail_new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='employee_c2', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user', kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_2',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='company_ids',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value=4, kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='cls', ctx=Load()),
                                                                attr='company_2',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Enguerrand Employee C2', kind=None),
                                    ),
                                    keyword(
                                        arg='notification_type',
                                        value=Constant(value='inbox', kind=None),
                                    ),
                                    keyword(
                                        arg='signature',
                                        value=Constant(value='--\nEnguerrand', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='partner_employee_c2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_employee_c2',
                                    ctx=Load(),
                                ),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
