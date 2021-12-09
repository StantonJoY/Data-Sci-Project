Module(
    body=[
        ImportFrom(
            module='odoo.addons.test_mass_mailing.tests.common',
            names=[alias(name='TestMassMailCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='MockSmtplibCase', asname=None)],
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
            name='TestMassMailingServer',
            bases=[
                Name(id='TestMassMailCommon', ctx=Load()),
                Name(id='MockSmtplibCase', ctx=Load()),
            ],
            keywords=[],
            body=[
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
                                            Name(id='TestMassMailingServer', ctx=Load()),
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
                        Expr(
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
                                                slice=Constant(value='ir.mail_server', kind=None),
                                                ctx=Load(),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_init_mail_servers',
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
                                    attr='recipients',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_create_mailing_test_records',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Constant(value='mailing.test.optout', kind=None),
                                    ),
                                    keyword(
                                        arg='count',
                                        value=Constant(value=8, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_mailing_server_batch',
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
                            value=Constant(value='Test that the right mail server is chosen to send the mailing.\n\n        Test also the envelop and the SMTP headers.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='mailings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body_html', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='mailing_model_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mailing', kind=None),
                                                    Constant(value='Body for <t t-out="object.name" />', kind=None),
                                                    Constant(value='specific_user@test.com', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mailing.test.optout', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body_html', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='mailing_model_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mailing', kind=None),
                                                    Constant(value='Body for <t t-out="object.name" />', kind=None),
                                                    Constant(value='unknown_name@test.com', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mailing.test.optout', kind=None)],
                                                            keywords=[],
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
                                            attr='mock_smtplib_connection',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailings', ctx=Load()),
                                            attr='action_send_mail',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='find_mail_server_mocked',
                                            ctx=Load(),
                                        ),
                                        attr='call_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Must be called only once per mail from', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_email_sent_smtp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='smtp_from',
                                        value=Constant(value='specific_user@test.com', kind=None),
                                    ),
                                    keyword(
                                        arg='message_from',
                                        value=Constant(value='specific_user@test.com', kind=None),
                                    ),
                                    keyword(
                                        arg='from_filter',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_user',
                                                ctx=Load(),
                                            ),
                                            attr='from_filter',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='emails_count',
                                        value=Constant(value=8, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_email_sent_smtp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='smtp_from',
                                        value=Lambda(
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
                                                left=Constant(value='bounce', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='x', ctx=Load())],
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='message_from',
                                        value=Constant(value='unknown_name@test.com', kind=None),
                                    ),
                                    keyword(
                                        arg='from_filter',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_domain',
                                                ctx=Load(),
                                            ),
                                            attr='from_filter',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='emails_count',
                                        value=Constant(value=8, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                                Constant(value='odoo.addons.mass_mailing.models.mailing', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_mailing_server_default',
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
                            targets=[Name(id='mailings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body_html', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='mailing_model_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mailing', kind=None),
                                                    Constant(value='Body for <t t-out="object.name" />', kind=None),
                                                    Constant(value='"Testing" <unknow_email@unknow_domain.com>', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mailing.test.optout', kind=None)],
                                                            keywords=[],
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
                                            attr='mock_smtplib_connection',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailings', ctx=Load()),
                                            attr='action_send_mail',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='find_mail_server_mocked',
                                            ctx=Load(),
                                        ),
                                        attr='call_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_email_sent_smtp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='smtp_from',
                                        value=Constant(value='notifications@test.com', kind=None),
                                    ),
                                    keyword(
                                        arg='message_from',
                                        value=Constant(value='"Testing (unknow_email@unknow_domain.com)" <notifications@test.com>', kind=None),
                                    ),
                                    keyword(
                                        arg='from_filter',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_notification',
                                                ctx=Load(),
                                            ),
                                            attr='from_filter',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='emails_count',
                                        value=Constant(value=8, kind=None),
                                    ),
                                ],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='find_mail_server_mocked',
                                            ctx=Load(),
                                        ),
                                        attr='call_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Must be called only once', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                                Constant(value='odoo.addons.mass_mailing.models.mailing', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mass_mailing_server_forced',
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
                            targets=[Name(id='mailings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.mailing', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body_html', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='mailing_model_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mailing', kind=None),
                                                    Constant(value='Body for <t t-out="object.name" />', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='server_user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='from_filter',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mailing.test.optout', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='body_html', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='mailing_model_id', kind=None),
                                                    Constant(value='mail_server_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Mailing', kind=None),
                                                    Constant(value='Body for <t t-out="object.name" />', kind=None),
                                                    Constant(value='unknow_email@unknow_domain.com', kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='ir.model', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='mailing.test.optout', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='server_notification',
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
                                            attr='mock_smtplib_connection',
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailings', ctx=Load()),
                                            attr='action_send_mail',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='find_mail_server_mocked',
                                            ctx=Load(),
                                        ),
                                        attr='call_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Must not be called when mail server is forced', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_email_sent_smtp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='smtp_from',
                                        value=Constant(value='specific_user@test.com', kind=None),
                                    ),
                                    keyword(
                                        arg='message_from',
                                        value=Constant(value='specific_user@test.com', kind=None),
                                    ),
                                    keyword(
                                        arg='from_filter',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_user',
                                                ctx=Load(),
                                            ),
                                            attr='from_filter',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='emails_count',
                                        value=Constant(value=8, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assert_email_sent_smtp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='smtp_from',
                                        value=Constant(value='unknow_email@unknow_domain.com', kind=None),
                                    ),
                                    keyword(
                                        arg='message_from',
                                        value=Constant(value='unknow_email@unknow_domain.com', kind=None),
                                    ),
                                    keyword(
                                        arg='from_filter',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='server_notification',
                                                ctx=Load(),
                                            ),
                                            attr='from_filter',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='emails_count',
                                        value=Constant(value=8, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_marketing', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.addons.mail.models.mail_mail', kind=None),
                                Constant(value='odoo.models.unlink', kind=None),
                                Constant(value='odoo.addons.mass_mailing.models.mailing', kind=None),
                            ],
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
                    args=[Constant(value='mass_mailing', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
