Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='freezegun',
            names=[alias(name='freeze_time', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mass_mailing.models.mail_thread',
            names=[alias(name='BLACKLIST_MAX_BOUNCED_LIMIT', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.test_mass_mailing.tests',
            names=[alias(name='common', asname=None)],
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
        ImportFrom(
            module='odoo.sql_db',
            names=[alias(name='Cursor', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestAutoBlacklist',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TestMassMailCommon',
                    ctx=Load(),
                ),
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
                                            Name(id='TestAutoBlacklist', ctx=Load()),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='target_rec',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='_create_mailing_test_records',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='mailing_bl',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mailing_domain', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='target_rec',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='ids',
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
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mailing_bounce_w_auto_bl',
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
                                    attr='_test_mailing_bounce_w_auto_bl',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=None, kind=None)],
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
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mailing_bounce_w_auto_bl_partner',
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
                            targets=[Name(id='bounced_partner', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='message_bounce', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Bounced Partner', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='target_rec',
                                                    ctx=Load(),
                                                ),
                                                attr='email_from',
                                                ctx=Load(),
                                            ),
                                            Name(id='BLACKLIST_MAX_BOUNCED_LIMIT', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_mailing_bounce_w_auto_bl',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='bounced_partner', kind=None)],
                                        values=[Name(id='bounced_partner', ctx=Load())],
                                    ),
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
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_mailing_bounce_w_auto_bl_partner_duplicates',
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
                            targets=[Name(id='bounced_partners', ctx=Store())],
                            value=BinOp(
                                left=Call(
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
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                                Constant(value='message_bounce', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Bounced Partner1', kind=None),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='target_rec',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email_from',
                                                    ctx=Load(),
                                                ),
                                                Name(id='BLACKLIST_MAX_BOUNCED_LIMIT', ctx=Load()),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Call(
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
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='email', kind=None),
                                                Constant(value='message_bounce', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Bounced Partner2', kind=None),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='target_rec',
                                                        ctx=Load(),
                                                    ),
                                                    attr='email_from',
                                                    ctx=Load(),
                                                ),
                                                Name(id='BLACKLIST_MAX_BOUNCED_LIMIT', ctx=Load()),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_test_mailing_bounce_w_auto_bl',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='bounced_partner', kind=None)],
                                        values=[Name(id='bounced_partners', ctx=Load())],
                                    ),
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
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_test_mailing_bounce_w_auto_bl',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bounce_base_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mailing', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mailing_bl',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='target', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.test.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='target_rec',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='traces', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mailing.trace', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='idx', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=4, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_mailing', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_dt', ctx=Store())],
                                    value=BinOp(
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
                                                    value=BinOp(
                                                        left=Name(id='idx', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='freeze_time', ctx=Load()),
                                                args=[Name(id='new_dt', ctx=Load())],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='patch', ctx=Load()),
                                                    attr='object',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='Cursor', ctx=Load()),
                                                    Constant(value='now', kind=None),
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[],
                                                            vararg=arg(arg='args', annotation=None, type_comment=None),
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                                            defaults=[],
                                                        ),
                                                        body=Name(id='new_dt', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        AugAssign(
                                            target=Name(id='traces', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_create_bounce_trace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='new_mailing', ctx=Load()),
                                                    Name(id='target', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='dt',
                                                        value=BinOp(
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
                                                                        value=BinOp(
                                                                            left=Name(id='idx', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value=2, kind=None),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='gateway_mail_bounce',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='new_mailing', ctx=Load()),
                                                    Name(id='target', ctx=Load()),
                                                    Name(id='bounce_base_values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='action_put_in_queue',
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
                                            attr='mock_mail_gateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_unlink_sent',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mailing', ctx=Load()),
                                            attr='_process_mass_mailing_queue',
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
                                    attr='assertMailTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='email', kind=None)],
                                                values=[Constant(value='test.record.00@test.example.com', kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='mailing', ctx=Load()),
                                    Name(id='target', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='check_mail',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gateway_mail_bounce',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mailing', ctx=Load()),
                                    Name(id='target', ctx=Load()),
                                    Name(id='bounce_base_values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='blacklist_record', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='target', ctx=Load()),
                                                        attr='email_normalized',
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
                                        args=[Name(id='blacklist_record', ctx=Load())],
                                        keywords=[],
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='target', ctx=Load()),
                                        attr='is_blacklisted',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_mailing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='new_mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mailing_domain', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='target', ctx=Load()),
                                                                attr='ids',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='new_mailing', ctx=Load()),
                                    attr='action_put_in_queue',
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
                                            attr='mock_mail_gateway',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='mail_unlink_sent',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='new_mailing', ctx=Load()),
                                            attr='_process_mass_mailing_queue',
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
                                    attr='assertMailTraces',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='email', kind=None),
                                                    Constant(value='trace_status', kind=None),
                                                    Constant(value='failure_type', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='test.record.00@test.example.com', kind=None),
                                                    Constant(value='cancel', kind=None),
                                                    Constant(value='mail_bl', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='new_mailing', ctx=Load()),
                                    Name(id='target', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='check_mail',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.mail.models.mail_thread', kind=None)],
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
                    args=[Constant(value='mail_blacklist', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
