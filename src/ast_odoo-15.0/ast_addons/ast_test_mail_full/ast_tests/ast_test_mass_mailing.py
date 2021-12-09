Module(
    body=[
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.test_mail_full.tests.common',
            names=[alias(name='TestMailFullCommon', asname=None)],
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
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestMassMailing',
            bases=[Name(id='TestMailFullCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_mailing_w_blacklist_opt_out',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mailing', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mailing_model_id', kind=None)],
                                        values=[
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recipients', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
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
                                        value=Constant(value=10, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='recipients', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Subscript(
                                            value=Name(id='recipients', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='opt_out', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='email', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='recipients', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='email_normalized',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.blacklist', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='email', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='recipients', ctx=Load()),
                                                    slice=Constant(value=4, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='email_normalized',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='recipient_dup_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='recipients', ctx=Load()),
                                        slice=Constant(value=9, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recipient_void_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.test.optout', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='TestRecord_void_1', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recipient_falsy_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mailing.test.optout', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email_from', kind=None),
                                        ],
                                        values=[
                                            Constant(value='TestRecord_falsy_1', kind=None),
                                            Constant(value='falsymail', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recipients_all', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Name(id='recipients', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='recipient_dup_1', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Name(id='recipient_void_1', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='recipient_falsy_1', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mailing', ctx=Load()),
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
                                                                value=Name(id='recipients_all', ctx=Load()),
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
                        For(
                            target=Name(id='recipient', ctx=Store()),
                            iter=Name(id='recipients_all', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='recipient_info', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='email', kind=None),
                                            Constant(value='content', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='recipient', ctx=Load()),
                                                attr='email_normalized',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='Hello %s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='recipient', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='recipient', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='recipients', ctx=Load()),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=BitOr(),
                                                right=Subscript(
                                                    value=Name(id='recipients', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='recipient_info', ctx=Load()),
                                                    slice=Constant(value='trace_status', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='cancel', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='recipient_info', ctx=Load()),
                                                    slice=Constant(value='failure_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='mail_optout', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='recipient', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='recipients', ctx=Load()),
                                                            slice=Constant(value=3, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=BitOr(),
                                                        right=Subscript(
                                                            value=Name(id='recipients', ctx=Load()),
                                                            slice=Constant(value=4, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='recipient_info', ctx=Load()),
                                                            slice=Constant(value='trace_status', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='cancel', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='recipient_info', ctx=Load()),
                                                            slice=Constant(value='failure_type', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='mail_bl', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='recipient', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='recipient_dup_1', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                    slice=Constant(value='trace_status', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='cancel', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                    slice=Constant(value='failure_type', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='mail_dup', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='recipient', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='recipient_void_1', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='recipient_info', ctx=Load()),
                                                                            slice=Constant(value='trace_status', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='cancel', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='recipient_info', ctx=Load()),
                                                                            slice=Constant(value='failure_type', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='mail_email_missing', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='recipient', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='recipient_falsy_1', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                                    slice=Constant(value='trace_status', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='cancel', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                                    slice=Constant(value='failure_type', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='mail_email_invalid', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Subscript(
                                                                                    value=Name(id='recipient_info', ctx=Load()),
                                                                                    slice=Constant(value='email', kind=None),
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Attribute(
                                                                                value=Name(id='recipient', ctx=Load()),
                                                                                attr='email_from',
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[Name(id='email', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_find_sent_mail_wemail',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='recipient', ctx=Load()),
                                                                                        attr='email_normalized',
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
                                                                                    attr='assertIn',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='Hi %s :)', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Attribute(
                                                                                            value=Name(id='recipient', ctx=Load()),
                                                                                            attr='name',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    Subscript(
                                                                                        value=Name(id='email', ctx=Load()),
                                                                                        slice=Constant(value='body', kind=None),
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
                                                                                    attr='assertIn',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='%s/mail/mailing/%s/unsubscribe', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='mailing', ctx=Load()),
                                                                                                        attr='get_base_url',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                Attribute(
                                                                                                    value=Name(id='mailing', ctx=Load()),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    Subscript(
                                                                                        value=Name(id='email', ctx=Load()),
                                                                                        slice=Constant(value='body', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='unsubscribe_href', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_get_href_from_anchor_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='email', ctx=Load()),
                                                                                        slice=Constant(value='body', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value='url6', kind=None),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='unsubscribe_url', ctx=Store())],
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
                                                                                args=[Name(id='unsubscribe_href', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='unsubscribe_params', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='unsubscribe_url', ctx=Load()),
                                                                                            attr='decode_query',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='to_dict',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='flat',
                                                                                        value=Constant(value=True, kind=None),
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
                                                                                    Call(
                                                                                        func=Name(id='int', ctx=Load()),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='unsubscribe_params', ctx=Load()),
                                                                                                slice=Constant(value='res_id', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='recipient', ctx=Load()),
                                                                                        attr='id',
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
                                                                                    Subscript(
                                                                                        value=Name(id='unsubscribe_params', ctx=Load()),
                                                                                        slice=Constant(value='email', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='recipient', ctx=Load()),
                                                                                        attr='email_normalized',
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
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='mailing', ctx=Load()),
                                                                                            attr='_unsubscribe_token',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='unsubscribe_params', ctx=Load()),
                                                                                                slice=Constant(value='res_id', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Subscript(
                                                                                                value=Name(id='unsubscribe_params', ctx=Load()),
                                                                                                slice=Constant(value='email', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Subscript(
                                                                                        value=Name(id='unsubscribe_params', ctx=Load()),
                                                                                        slice=Constant(value='token', kind=None),
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
                                                                                    attr='assertIn',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    BinOp(
                                                                                        left=Constant(value='%s/mailing/%s/view', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='mailing', ctx=Load()),
                                                                                                        attr='get_base_url',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                Attribute(
                                                                                                    value=Name(id='mailing', ctx=Load()),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    Subscript(
                                                                                        value=Name(id='email', ctx=Load()),
                                                                                        slice=Constant(value='body', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='view_href', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_get_href_from_anchor_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='email', ctx=Load()),
                                                                                        slice=Constant(value='body', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value='url6', kind=None),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='view_url', ctx=Store())],
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
                                                                                args=[Name(id='view_href', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='view_params', ctx=Store())],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='view_url', ctx=Load()),
                                                                                            attr='decode_query',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='to_dict',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='flat',
                                                                                        value=Constant(value=True, kind=None),
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
                                                                                    Call(
                                                                                        func=Name(id='int', ctx=Load()),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='view_params', ctx=Load()),
                                                                                                slice=Constant(value='res_id', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='recipient', ctx=Load()),
                                                                                        attr='id',
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
                                                                                    Subscript(
                                                                                        value=Name(id='view_params', ctx=Load()),
                                                                                        slice=Constant(value='email', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='recipient', ctx=Load()),
                                                                                        attr='email_normalized',
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
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='mailing', ctx=Load()),
                                                                                            attr='_unsubscribe_token',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='view_params', ctx=Load()),
                                                                                                slice=Constant(value='res_id', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Subscript(
                                                                                                value=Name(id='view_params', ctx=Load()),
                                                                                                slice=Constant(value='email', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Subscript(
                                                                                        value=Name(id='view_params', ctx=Load()),
                                                                                        slice=Constant(value='token', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertMailTraces',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Name(id='recipient_info', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            Name(id='mailing', ctx=Load()),
                                            Name(id='recipient', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mail_links_info',
                                                value=List(
                                                    elts=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url0', kind=None),
                                                                        BinOp(
                                                                            left=Constant(value='https://www.odoo.tz/my/%s', kind=None),
                                                                            op=Mod(),
                                                                            right=Attribute(
                                                                                value=Name(id='recipient', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                        Constant(value=True, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url1', kind=None),
                                                                        Constant(value='https://www.odoo.be', kind=None),
                                                                        Constant(value=True, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url2', kind=None),
                                                                        Constant(value='https://www.odoo.com', kind=None),
                                                                        Constant(value=True, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url3', kind=None),
                                                                        Constant(value='https://www.odoo.eu', kind=None),
                                                                        Constant(value=True, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url4', kind=None),
                                                                        Constant(value='https://www.example.com/foo/bar?baz=qux', kind=None),
                                                                        Constant(value=True, kind=None),
                                                                        Dict(
                                                                            keys=[Constant(value='baz', kind=None)],
                                                                            values=[Constant(value='qux', kind=None)],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url5', kind=None),
                                                                        BinOp(
                                                                            left=Constant(value='%s/event/dummy-event-0', kind=None),
                                                                            op=Mod(),
                                                                            right=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='mailing', ctx=Load()),
                                                                                    attr='get_base_url',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Constant(value=True, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url6', kind=None),
                                                                        BinOp(
                                                                            left=Constant(value='%s/view', kind=None),
                                                                            op=Mod(),
                                                                            right=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='mailing', ctx=Load()),
                                                                                    attr='get_base_url',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Constant(value=False, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url7', kind=None),
                                                                        Constant(value='mailto:test@odoo.com', kind=None),
                                                                        Constant(value=False, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='url8', kind=None),
                                                                        BinOp(
                                                                            left=Constant(value='%s/unsubscribe_from_list', kind=None),
                                                                            op=Mod(),
                                                                            right=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='mailing', ctx=Load()),
                                                                                    attr='get_base_url',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        Constant(value=False, kind=None),
                                                                        Dict(keys=[], values=[]),
                                                                    ],
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
                                                arg='check_mail',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertMailingStatistics',
                                    ctx=Load(),
                                ),
                                args=[Name(id='mailing', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='expected',
                                        value=Constant(value=13, kind=None),
                                    ),
                                    keyword(
                                        arg='delivered',
                                        value=Constant(value=6, kind=None),
                                    ),
                                    keyword(
                                        arg='sent',
                                        value=Constant(value=6, kind=None),
                                    ),
                                    keyword(
                                        arg='canceled',
                                        value=Constant(value=7, kind=None),
                                    ),
                                    keyword(
                                        arg='failed',
                                        value=Constant(value=0, kind=None),
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
                            args=[Constant(value='odoo.addons.mail.models.mail_mail', kind=None)],
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
