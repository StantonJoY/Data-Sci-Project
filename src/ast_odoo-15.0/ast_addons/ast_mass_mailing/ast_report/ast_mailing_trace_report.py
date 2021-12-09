Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailingTraceReport',
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
                    value=Constant(value='mailing.trace.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mass Mailing Statistics', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mass Mail', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mailing_type', ctx=Store())],
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
                                            Constant(value='mail', kind=None),
                                            Constant(value='Mail', kind=None),
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
                                value=Constant(value='Type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='mail', kind=None),
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
                    targets=[Name(id='campaign', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Mailing Campaign', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
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
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Scheduled Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
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
                                            Constant(value='draft', kind=None),
                                            Constant(value='Draft', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='test', kind=None),
                                            Constant(value='Tested', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='done', kind=None),
                                            Constant(value='Sent', kind=None),
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
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='email_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='From', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='scheduled', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sent', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='delivered', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='error', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='opened', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='replied', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='bounced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='canceled', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='clicked', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
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
                            value=Constant(value='Mass Mail Statistical Report: based on mailing.trace that models the various\n        statistics collected for each mailing, and mailing.mailing model that models the\n        various mailing performed. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='mailing_trace_report', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_report_get_request',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_report_get_request',
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
                            targets=[Name(id='sql_select', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='SELECT %s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value=', ', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_report_get_request_select_items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sql_from', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='FROM %s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value=' ', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_report_get_request_from_items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sql_where_items', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_report_get_request_where_items',
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
                                    Name(id='sql_where_items', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='sql_where_items', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sql_where', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='WHERE %s', kind=None),
                                        op=Mod(),
                                        right=Subscript(
                                            value=Name(id='sql_where_items', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='sql_where_items', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sql_where', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='WHERE %s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value=' AND ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='sql_where_items', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='sql_where', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='sql_group_by', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='GROUP BY %s', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Constant(value=', ', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_report_get_request_group_by_items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='CREATE OR REPLACE VIEW mailing_trace_report AS (', kind=None),
                                    FormattedValue(
                                        value=Name(id='sql_select', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' ', kind=None),
                                    FormattedValue(
                                        value=Name(id='sql_from', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' ', kind=None),
                                    FormattedValue(
                                        value=Name(id='sql_where', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' ', kind=None),
                                    FormattedValue(
                                        value=Name(id='sql_group_by', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' )', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_report_get_request_select_items',
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
                            value=List(
                                elts=[
                                    Constant(value='min(trace.id) as id', kind=None),
                                    Constant(value='utm_source.name as name', kind=None),
                                    Constant(value='mailing.mailing_type', kind=None),
                                    Constant(value='utm_campaign.name as campaign', kind=None),
                                    Constant(value='trace.create_date as scheduled_date', kind=None),
                                    Constant(value='mailing.state', kind=None),
                                    Constant(value='mailing.email_from', kind=None),
                                    Constant(value='COUNT(trace.id) as scheduled', kind=None),
                                    Constant(value='COUNT(trace.sent_datetime) as sent', kind=None),
                                    Constant(value="(COUNT(trace.id) - COUNT(trace.trace_status) FILTER (WHERE trace.trace_status IN ('error', 'bounce', 'cancel'))) as delivered", kind=None),
                                    Constant(value="COUNT(trace.trace_status) FILTER (WHERE trace.trace_status = 'error') as error", kind=None),
                                    Constant(value="COUNT(trace.trace_status) FILTER (WHERE trace.trace_status = 'bounce') as bounced", kind=None),
                                    Constant(value="COUNT(trace.trace_status) FILTER (WHERE trace.trace_status = 'cancel') as canceled", kind=None),
                                    Constant(value="COUNT(trace.trace_status) FILTER (WHERE trace.trace_status = 'open') as opened", kind=None),
                                    Constant(value="COUNT(trace.trace_status) FILTER (WHERE trace.trace_status = 'reply') as replied", kind=None),
                                    Constant(value='COUNT(trace.links_click_datetime) as clicked', kind=None),
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
                    name='_report_get_request_from_items',
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
                            value=List(
                                elts=[
                                    Constant(value='mailing_trace as trace', kind=None),
                                    Constant(value='LEFT JOIN mailing_mailing as mailing ON (trace.mass_mailing_id=mailing.id)', kind=None),
                                    Constant(value='LEFT JOIN utm_campaign as utm_campaign ON (mailing.campaign_id = utm_campaign.id)', kind=None),
                                    Constant(value='LEFT JOIN utm_source as utm_source ON (mailing.source_id = utm_source.id)', kind=None),
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
                    name='_report_get_request_where_items',
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
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_report_get_request_group_by_items',
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
                            value=List(
                                elts=[
                                    Constant(value='trace.create_date', kind=None),
                                    Constant(value='utm_source.name', kind=None),
                                    Constant(value='utm_campaign.name', kind=None),
                                    Constant(value='mailing.mailing_type', kind=None),
                                    Constant(value='mailing.state', kind=None),
                                    Constant(value='mailing.email_from', kind=None),
                                ],
                                ctx=Load(),
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
