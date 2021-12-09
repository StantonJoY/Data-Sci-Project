Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='PaymentTransaction',
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
                    value=Constant(value='payment.transaction', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_donation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Is donation', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Is the payment a donation', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_finalize_post_processing',
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
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_finalize_post_processing',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='tx', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='is_donation', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tx', ctx=Load()),
                                            attr='_send_donation_email',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Payment received from donation with following details:', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=List(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='partner_name', kind=None),
                                            Constant(value='partner_country_id', kind=None),
                                            Constant(value='partner_email', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='tx', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Name(id='field', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='string',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='tx', ctx=Load()),
                                                slice=Name(id='field', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='value', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='name', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='value', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='value', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='msg', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='<br/>- %s: %s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='field_name', ctx=Load()),
                                                                        Name(id='value', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tx', ctx=Load()),
                                                attr='payment_id',
                                                ctx=Load(),
                                            ),
                                            attr='_message_log',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Constant(value='', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='msg', ctx=Load())],
                                                    keywords=[],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_donation_email',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='is_internal_notification', annotation=None, type_comment=None),
                            arg(arg='comment', annotation=None, type_comment=None),
                            arg(arg='recipient_email', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
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
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='is_internal_notification', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='done', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='subject', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='is_internal_notification', ctx=Load()),
                                        body=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='A donation has been made on your website', kind=None)],
                                            keywords=[],
                                        ),
                                        orelse=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Donation confirmation', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
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
                                                args=[Constant(value='website_payment.donation_mail_body', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='is_internal_notification', kind=None),
                                                    Constant(value='tx', kind=None),
                                                    Constant(value='comment', kind=None),
                                                ],
                                                values=[
                                                    Name(id='is_internal_notification', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='comment', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='engine',
                                                value=Constant(value='ir.qweb', kind=None),
                                            ),
                                            keyword(
                                                arg='minimal_qcontext',
                                                value=Constant(value=True, kind=None),
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
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='website_payment.mail_template_donation', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='send_mail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='notif_layout',
                                                value=Constant(value='mail.mail_notification_light', kind=None),
                                            ),
                                            keyword(
                                                arg='force_send',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='email_values',
                                                value=Dict(
                                                    keys=[
                                                        Constant(value='email_to', kind=None),
                                                        Constant(value='email_from', kind=None),
                                                        Constant(value='author_id', kind=None),
                                                        Constant(value='subject', kind=None),
                                                        Constant(value='body_html', kind=None),
                                                    ],
                                                    values=[
                                                        IfExp(
                                                            test=Name(id='is_internal_notification', ctx=Load()),
                                                            body=Name(id='recipient_email', ctx=Load()),
                                                            orelse=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_email',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='email_formatted',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='subject', ctx=Load()),
                                                        Name(id='body', ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
