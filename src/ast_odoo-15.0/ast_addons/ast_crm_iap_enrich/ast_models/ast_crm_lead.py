Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='OperationalError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
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
            name='Lead',
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
                    value=Constant(value='crm.lead', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='iap_enrich_done', ctx=Store())],
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
                                value=Constant(value='Enrichment done', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Whether IAP service for lead enrichment based on email has been performed on this lead.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_enrich_button', ctx=Store())],
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
                                value=Constant(value='Allow manual enrich', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_show_enrich_button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_show_enrich_button',
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
                            targets=[Name(id='config', ctx=Store())],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.iap.lead.enrich.setting', kind=None),
                                    Constant(value='manual', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='config', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Name(id='config', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='manual', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='show_enrich_button',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Return(value=None),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='lead', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='active',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='email_from',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='email_state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='incorrect', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='lead', ctx=Load()),
                                                attr='iap_enrich_done',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='lead', ctx=Load()),
                                                attr='reveal_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='probability',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=100, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='show_enrich_button',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='show_enrich_button',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='email_from', kind=None),
                                Constant(value='probability', kind=None),
                                Constant(value='iap_enrich_done', kind=None),
                                Constant(value='reveal_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_iap_enrich_leads_cron',
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
                            targets=[Name(id='timeDelta', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='fields', ctx=Load()),
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
                                            arg='hours',
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='iap_enrich_done', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='reveal_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='probability', kind=None),
                                                    Constant(value='<', kind=None),
                                                    Constant(value=100, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_date', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Name(id='timeDelta', ctx=Load()),
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
                                    value=Name(id='leads', ctx=Load()),
                                    attr='iap_enrich',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='from_cron',
                                        value=Constant(value=True, kind=None),
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
                FunctionDef(
                    name='iap_enrich',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_cron', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='batches', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='self', ctx=Load()),
                                    slice=Slice(
                                        lower=Name(id='index', ctx=Load()),
                                        upper=BinOp(
                                            left=Name(id='index', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=50, kind=None),
                                        ),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='index', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Constant(value=0, kind=None),
                                                Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='self', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Constant(value=50, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='leads', ctx=Store()),
                            iter=Name(id='batches', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lead_emails', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Try(
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
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value='SELECT 1 FROM {} WHERE id in %(lead_ids)s FOR UPDATE NOWAIT', kind=None),
                                                                    attr='format',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_table',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Dict(
                                                                keys=[Constant(value='lead_ids', kind=None)],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='tuple', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='leads', ctx=Load()),
                                                                                attr='ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='log_exceptions',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                For(
                                                    target=Name(id='lead', ctx=Store()),
                                                    iter=Name(id='leads', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='lead', ctx=Load()),
                                                                            attr='probability',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=100, kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='lead', ctx=Load()),
                                                                        attr='iap_enrich_done',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[Continue()],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='normalized_email', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='tools', ctx=Load()),
                                                                    attr='email_normalize',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='lead', ctx=Load()),
                                                                        attr='email_from',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='normalized_email', ctx=Load()),
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='lead', ctx=Load()),
                                                                            attr='message_post_with_view',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='crm_iap_enrich.mail_message_lead_enrich_no_email', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='subtype_id',
                                                                                value=Attribute(
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
                                                                                        args=[Constant(value='mail.mt_note', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                                Continue(),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='email_domain', ctx=Store())],
                                                            value=Subscript(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='normalized_email', ctx=Load()),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='@', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='email_domain', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='iap_tools', ctx=Load()),
                                                                        attr='_MAIL_DOMAIN_BLACKLIST',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='lead', ctx=Load()),
                                                                            attr='write',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[Constant(value='iap_enrich_done', kind=None)],
                                                                                values=[Constant(value=True, kind=None)],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='lead', ctx=Load()),
                                                                            attr='message_post_with_view',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='crm_iap_enrich.mail_message_lead_enrich_notfound', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='subtype_id',
                                                                                value=Attribute(
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
                                                                                        args=[Constant(value='mail.mt_note', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='lead_emails', ctx=Load()),
                                                                            slice=Attribute(
                                                                                value=Name(id='lead', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='email_domain', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='lead_emails', ctx=Load()),
                                                    body=[
                                                        Try(
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='iap_response', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='iap.enrich.api', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_request_enrich',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='lead_emails', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            handlers=[
                                                                ExceptHandler(
                                                                    type=Attribute(
                                                                        value=Name(id='iap_tools', ctx=Load()),
                                                                        attr='InsufficientCreditError',
                                                                        ctx=Load(),
                                                                    ),
                                                                    name=None,
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='_logger', ctx=Load()),
                                                                                    attr='info',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Constant(value='Sent batch %s enrich requests: failed because of credit', kind=None),
                                                                                    Call(
                                                                                        func=Name(id='len', ctx=Load()),
                                                                                        args=[Name(id='lead_emails', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        If(
                                                                            test=UnaryOp(
                                                                                op=Not(),
                                                                                operand=Name(id='from_cron', ctx=Load()),
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='data', ctx=Store())],
                                                                                    value=Dict(
                                                                                        keys=[Constant(value='url', kind=None)],
                                                                                        values=[
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='env',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value='iap.account', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='get_credits_url',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Constant(value='reveal', kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Subscript(
                                                                                                value=Name(id='leads', ctx=Load()),
                                                                                                slice=Constant(value=0, kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='message_post_with_view',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='crm_iap_enrich.mail_message_lead_enrich_no_credit', kind=None)],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='values',
                                                                                                value=Name(id='data', ctx=Load()),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='subtype_id',
                                                                                                value=Attribute(
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
                                                                                                        args=[Constant(value='mail.mt_note', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        Break(),
                                                                    ],
                                                                ),
                                                                ExceptHandler(
                                                                    type=Name(id='Exception', ctx=Load()),
                                                                    name='e',
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='_logger', ctx=Load()),
                                                                                    attr='info',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Constant(value='Sent batch %s enrich requests: failed with exception %s', kind=None),
                                                                                    Call(
                                                                                        func=Name(id='len', ctx=Load()),
                                                                                        args=[Name(id='lead_emails', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    Name(id='e', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='info',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='Sent batch %s enrich requests: success', kind=None),
                                                                            Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[Name(id='lead_emails', ctx=Load())],
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
                                                                            attr='_iap_enrich_from_response',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='iap_response', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            finalbody=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='OperationalError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='A batch of leads could not be enriched :%s', kind=None),
                                                                    Call(
                                                                        func=Name(id='repr', ctx=Load()),
                                                                        args=[Name(id='leads', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='registry',
                                                    ctx=Load(),
                                                ),
                                                attr='in_test_mode',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_iap_enrich_from_response',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='iap_response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Handle from the service and enrich the lead accordingly\n\n        :param iap_response: dict{lead_id: company data or False}\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='lead', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='iap_response', ctx=Load()),
                                                                    attr='keys',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
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
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='iap_data', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='iap_response', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='lead', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='iap_data', ctx=Load()),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='iap_enrich_done', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='message_post_with_view',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='crm_iap_enrich.mail_message_lead_enrich_notfound', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='subtype_id',
                                                        value=Attribute(
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
                                                                args=[Constant(value='mail.mt_note', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='iap_enrich_done', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lead_fields', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='partner_name', kind=None),
                                            Constant(value='reveal_id', kind=None),
                                            Constant(value='street', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='zip', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='iap_fields', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Constant(value='clearbit_id', kind=None),
                                            Constant(value='location', kind=None),
                                            Constant(value='city', kind=None),
                                            Constant(value='postal_code', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='lead_field', ctx=Store()),
                                            Name(id='iap_field', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='lead_fields', ctx=Load()),
                                            Name(id='iap_fields', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Subscript(
                                                            value=Name(id='lead', ctx=Load()),
                                                            slice=Name(id='lead_field', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='iap_data', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='iap_field', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Name(id='lead_field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='iap_data', ctx=Load()),
                                                        slice=Name(id='iap_field', ctx=Load()),
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='phone',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='iap_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='phone_numbers', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='phone', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='iap_data', ctx=Load()),
                                                    slice=Constant(value='phone_numbers', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='mobile',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='iap_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='phone_numbers', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='iap_data', ctx=Load()),
                                                            slice=Constant(value='phone_numbers', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='mobile', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='iap_data', ctx=Load()),
                                                    slice=Constant(value='phone_numbers', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='iap_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='country_code', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='country', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.country', kind=None),
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
                                                                    Constant(value='code', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='iap_data', ctx=Load()),
                                                                                slice=Constant(value='country_code', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='upper',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
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
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='country_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='country', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='country', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='lead', ctx=Load()),
                                                attr='country_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='lead', ctx=Load()),
                                                    attr='state_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='country', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='iap_data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='state_code', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='state', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.country.state', kind=None),
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
                                                                    Constant(value='code', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='iap_data', ctx=Load()),
                                                                        slice=Constant(value='state_code', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='country_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='country', ctx=Load()),
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
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='state_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='state', ctx=Load()),
                                                attr='id',
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
                                            value=Name(id='lead', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='template_values', ctx=Store())],
                                    value=Name(id='iap_data', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='template_values', ctx=Load()),
                                            slice=Constant(value='flavor_text', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Lead enriched based on email address', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lead', ctx=Load()),
                                            attr='message_post_with_view',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='iap_mail.enrich_company', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Name(id='template_values', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='subtype_id',
                                                value=Attribute(
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
                                                        args=[Constant(value='mail.mt_note', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
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
