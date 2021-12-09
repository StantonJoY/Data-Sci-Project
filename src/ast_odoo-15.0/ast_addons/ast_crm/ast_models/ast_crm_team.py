Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='exceptions', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_round', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[alias(name='safe_eval', asname=None)],
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
            name='Team',
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
                    value=Constant(value='crm.team', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='mail.alias.mixin', kind=None),
                            Constant(value='crm.team', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Sales Team', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_leads', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Leads', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Check this box to filter and qualify incoming requests as leads before converting them into opportunities and assigning them to a salesperson.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_opportunities', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Pipeline', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Check this box to manage a presales process with opportunities.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.alias', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Alias', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The email address associated with this channel. New emails received will automatically create new leads assigned to the channel.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='assignment_enabled', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lead Assign', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_assignment_enabled', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='assignment_auto_enabled', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Auto Assignment', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_assignment_enabled', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='assignment_optout', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Skip auto assignment', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='assignment_max', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lead Average Capacity', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_assignment_max', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Monthly average leads capacity for all salesmen belonging to the team', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='assignment_domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Assignment Domain', kind=None)],
                        keywords=[
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Additional filter domain when fetching unassigned leads to allocate to the team.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_unassigned_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Unassigned Leads', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_lead_unassigned_count', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_all_assigned_month_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Leads/Opps assigned this month', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_lead_all_assigned_month_count', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Number of leads and opportunities assigned this last month.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='opportunities_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Opportunities', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_opportunities_data', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='opportunities_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Opportunities Revenues', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_opportunities_data', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='opportunities_overdue_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Overdue Opportunities', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_opportunities_overdue_data', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='opportunities_overdue_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Overdue Opportunities Revenues', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_opportunities_overdue_data', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='alias_id.alias_user_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='inherited',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='groups_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
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
                                                            args=[Constant(value='sales_team.group_sale_salesman_all_leads', kind=None)],
                                                            keywords=[],
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
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_assignment_max',
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
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='assignment_max',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='member', ctx=Load()),
                                                    attr='assignment_max',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='member', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='team', ctx=Load()),
                                                            attr='crm_team_member_ids',
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
                                    type_comment=None,
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
                            args=[Constant(value='crm_team_member_ids.assignment_max', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_assignment_enabled',
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
                            targets=[Name(id='assign_enabled', ctx=Store())],
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
                                    Constant(value='crm.lead.auto.assignment', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='auto_assign_enabled', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='assign_enabled', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='assign_cron', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='crm.ir_cron_crm_lead_assign', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='auto_assign_enabled', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='assign_cron', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='assign_cron', ctx=Load()),
                                            attr='active',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assignment_enabled',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='assign_enabled', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assignment_auto_enabled',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='auto_assign_enabled', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_lead_unassigned_count',
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
                            targets=[Name(id='leads_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='team_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='lead', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='team_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='team_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='counts', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='datum', ctx=Load()),
                                        slice=Constant(value='team_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='datum', ctx=Load()),
                                    slice=Constant(value='team_id_count', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='datum', ctx=Store()),
                                        iter=Name(id='leads_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='lead_unassigned_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='counts', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                    name='_compute_lead_all_assigned_month_count',
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
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='lead_all_assigned_month_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='member', ctx=Load()),
                                                    attr='lead_month_count',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='member', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='team', ctx=Load()),
                                                            attr='crm_team_member_ids',
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
                                    type_comment=None,
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
                            args=[Constant(value='crm_team_member_ids.lead_month_count', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_opportunities_data',
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
                            targets=[Name(id='opportunity_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='team_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
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
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='opportunity', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='expected_revenue:sum', kind=None),
                                            Constant(value='team_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='team_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='counts', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='datum', ctx=Load()),
                                        slice=Constant(value='team_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='datum', ctx=Load()),
                                    slice=Constant(value='team_id_count', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='datum', ctx=Store()),
                                        iter=Name(id='opportunity_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amounts', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='datum', ctx=Load()),
                                        slice=Constant(value='team_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='datum', ctx=Load()),
                                    slice=Constant(value='expected_revenue', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='datum', ctx=Store()),
                                        iter=Name(id='opportunity_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='opportunities_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='counts', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='opportunities_amount',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='amounts', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                    name='_compute_opportunities_overdue_data',
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
                            targets=[Name(id='opportunity_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='team_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
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
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='opportunity', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='date_deadline', kind=None),
                                                    Constant(value='<', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
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
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='expected_revenue', kind=None),
                                            Constant(value='team_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='team_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='counts', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='datum', ctx=Load()),
                                        slice=Constant(value='team_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='datum', ctx=Load()),
                                    slice=Constant(value='team_id_count', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='datum', ctx=Store()),
                                        iter=Name(id='opportunity_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='amounts', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Subscript(
                                        value=Name(id='datum', ctx=Load()),
                                        slice=Constant(value='team_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='datum', ctx=Load()),
                                    slice=Constant(value='expected_revenue', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='datum', ctx=Store()),
                                        iter=Name(id='opportunity_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='opportunities_overdue_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='counts', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='opportunities_overdue_amount',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='amounts', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
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
                    name='_onchange_use_leads_opportunities',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='use_leads',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='use_opportunities',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_name',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='use_leads', kind=None),
                                Constant(value='use_opportunities', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_constrains_assignment_domain',
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
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='literal_eval', ctx=Load()),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='team', ctx=Load()),
                                                                attr='assignment_domain',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='[]', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='domain', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='crm.lead', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='domain', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='limit',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='exceptions', ctx=Load()),
                                                            attr='ValidationError',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Assignment domain for team %(team)s is incorrectly formatted', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='team',
                                                                        value=Attribute(
                                                                            value=Name(id='team', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='assignment_domain', kind=None)],
                            keywords=[],
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Team', ctx=Load()),
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
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='use_leads', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='use_opportunities', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='team', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='alias_vals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='team', ctx=Load()),
                                                    attr='_alias_get_creation_values',
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
                                                    value=Name(id='team', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='alias_name', kind=None),
                                                            Constant(value='alias_defaults', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='alias_vals', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='alias_name', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='team', ctx=Load()),
                                                                        attr='alias_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='alias_vals', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='alias_defaults', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                        Expr(
                            value=Constant(value=' When unlinking, concatenate ``crm.lead.scoring.frequency`` linked to\n        the team into "no team" statistics. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='frequencies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead.scoring.frequency', kind=None),
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
                                                    Constant(value='team_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='frequencies', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='existing_noteam', ctx=Store())],
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
                                                        slice=Constant(value='crm.lead.scoring.frequency', kind=None),
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
                                                            Constant(value='team_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='variable', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='frequencies', ctx=Load()),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='variable', kind=None)],
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
                                For(
                                    target=Name(id='frequency', ctx=Store()),
                                    iter=Name(id='frequencies', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='frequency', ctx=Load()),
                                                                    attr='won_count',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=0.1, kind=None),
                                                                Constant(value=2, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='frequency', ctx=Load()),
                                                                    attr='lost_count',
                                                                    ctx=Load(),
                                                                ),
                                                                Constant(value=0.1, kind=None),
                                                                Constant(value=2, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='match', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='existing_noteam', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='frequ_nt', annotation=None, type_comment=None)],
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
                                                                        value=Name(id='frequ_nt', ctx=Load()),
                                                                        attr='variable',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='frequency', ctx=Load()),
                                                                            attr='variable',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='frequ_nt', ctx=Load()),
                                                                        attr='value',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='frequency', ctx=Load()),
                                                                            attr='value',
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
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='match', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='exist_won_count', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='match', ctx=Load()),
                                                                attr='won_count',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='exist_lost_count', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='match', ctx=Load()),
                                                                attr='lost_count',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='add_won_count', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='frequency', ctx=Load()),
                                                                attr='won_count',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='add_lost_count', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='frequency', ctx=Load()),
                                                                attr='lost_count',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=0, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='new_won_count', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='exist_won_count', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='add_won_count', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='new_lost_count', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='exist_lost_count', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='add_lost_count', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='won_count',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Call(
                                                                func=Name(id='float_compare', ctx=Load()),
                                                                args=[
                                                                    Name(id='new_won_count', ctx=Load()),
                                                                    Constant(value=0.1, kind=None),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value=1, kind=None)],
                                                        ),
                                                        body=Name(id='new_won_count', ctx=Load()),
                                                        orelse=Constant(value=0.1, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='match', ctx=Load()),
                                                            attr='lost_count',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Call(
                                                                func=Name(id='float_compare', ctx=Load()),
                                                                args=[
                                                                    Name(id='new_lost_count', ctx=Load()),
                                                                    Constant(value=0.1, kind=None),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value=1, kind=None)],
                                                        ),
                                                        body=Name(id='new_lost_count', ctx=Load()),
                                                        orelse=Constant(value=0.1, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                AugAssign(
                                                    target=Name(id='existing_noteam', ctx=Store()),
                                                    op=Add(),
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
                                                                        slice=Constant(value='crm.lead.scoring.frequency', kind=None),
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
                                                                    Constant(value='lost_count', kind=None),
                                                                    Constant(value='team_id', kind=None),
                                                                    Constant(value='value', kind=None),
                                                                    Constant(value='variable', kind=None),
                                                                    Constant(value='won_count', kind=None),
                                                                ],
                                                                values=[
                                                                    IfExp(
                                                                        test=Compare(
                                                                            left=Call(
                                                                                func=Name(id='float_compare', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='frequency', ctx=Load()),
                                                                                        attr='lost_count',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0.1, kind=None),
                                                                                    Constant(value=2, kind=None),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value=1, kind=None)],
                                                                        ),
                                                                        body=Attribute(
                                                                            value=Name(id='frequency', ctx=Load()),
                                                                            attr='lost_count',
                                                                            ctx=Load(),
                                                                        ),
                                                                        orelse=Constant(value=0.1, kind=None),
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='frequency', ctx=Load()),
                                                                        attr='value',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='frequency', ctx=Load()),
                                                                        attr='variable',
                                                                        ctx=Load(),
                                                                    ),
                                                                    IfExp(
                                                                        test=Compare(
                                                                            left=Call(
                                                                                func=Name(id='float_compare', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='frequency', ctx=Load()),
                                                                                        attr='won_count',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Constant(value=0.1, kind=None),
                                                                                    Constant(value=2, kind=None),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value=1, kind=None)],
                                                                        ),
                                                                        body=Attribute(
                                                                            value=Name(id='frequency', ctx=Load()),
                                                                            attr='won_count',
                                                                            ctx=Load(),
                                                                        ),
                                                                        orelse=Constant(value=0.1, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
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
                                            Name(id='Team', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_alias_get_creation_values',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_alias_get_creation_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='alias_model_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
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
                                    args=[Constant(value='crm.lead', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='use_leads',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='use_opportunities',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='alias_name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='alias_defaults', kind=None),
                                            ctx=Store(),
                                        ),
                                        Name(id='defaults', ctx=Store()),
                                    ],
                                    value=Call(
                                        func=Name(id='literal_eval', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='alias_defaults',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='{}', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='has_group_use_lead', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='crm.group_use_lead', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='defaults', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='has_group_use_lead', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='use_leads',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Constant(value='lead', kind=None),
                                        orelse=Constant(value='opportunity', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='defaults', ctx=Load()),
                                            slice=Constant(value='team_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_cron_assign_leads',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='work_days', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Cron method assigning leads. Leads are allocated to all teams and\n        assigned to their members. It is based on either cron configuration\n        either forced through ``work_days`` parameter.\n\n        When based on cron configuration purpose of cron is to assign leads to\n        sales persons. Assigned workload is set to the workload those sales\n        people should perform between two cron iterations. If their maximum\n        capacity is reached assign process will not assign them any more lead.\n\n        e.g. cron is active with interval_number 3, interval_type days. This\n        means cron runs every 3 days. Cron will assign leads for 3 work days\n        to salespersons each 3 days unless their maximum capacity is reached.\n\n        If cron runs on an hour- or minute-based schedule minimum assignment\n        performed is equivalent to 0.2 workdays to avoid rounding issues.\n        Max assignment performed is for 30 days as it is better to run more\n        often than planning for more than one month. Assign process is best\n        designed to run every few hours (~4 times / day) or each few days.\n\n        See ``CrmTeam.action_assign_leads()`` and its sub methods for more\n        details about assign process.\n\n        :param float work_days: see ``CrmTeam.action_assign_leads()``;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='assign_cron', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='crm.ir_cron_crm_lead_assign', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='work_days', ctx=Load()),
                                    ),
                                    Name(id='assign_cron', ctx=Load()),
                                    Attribute(
                                        value=Name(id='assign_cron', ctx=Load()),
                                        attr='active',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='assign_cron', ctx=Load()),
                                            attr='interval_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='months', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='work_days', ctx=Store())],
                                            value=Constant(value=30, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='assign_cron', ctx=Load()),
                                                    attr='interval_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='weeks', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='work_days', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='min', ctx=Load()),
                                                        args=[
                                                            Constant(value=30, kind=None),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='assign_cron', ctx=Load()),
                                                                    attr='interval_number',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Mult(),
                                                                right=Constant(value=7, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='assign_cron', ctx=Load()),
                                                            attr='interval_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='days', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='work_days', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='min', ctx=Load()),
                                                                args=[
                                                                    Constant(value=30, kind=None),
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='assign_cron', ctx=Load()),
                                                                            attr='interval_number',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Mult(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='assign_cron', ctx=Load()),
                                                                    attr='interval_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='hours', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='work_days', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='max', ctx=Load()),
                                                                        args=[
                                                                            Constant(value=0.2, kind=None),
                                                                            BinOp(
                                                                                left=Attribute(
                                                                                    value=Name(id='assign_cron', ctx=Load()),
                                                                                    attr='interval_number',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Div(),
                                                                                right=Constant(value=24, kind=None),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='assign_cron', ctx=Load()),
                                                                            attr='interval_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='minutes', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='work_days', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='max', ctx=Load()),
                                                                                args=[
                                                                                    Constant(value=0.2, kind=None),
                                                                                    BinOp(
                                                                                        left=Attribute(
                                                                                            value=Name(id='assign_cron', ctx=Load()),
                                                                                            attr='interval_number',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        op=Div(),
                                                                                        right=Constant(value=1440, kind=None),
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
                        Assign(
                            targets=[Name(id='work_days', ctx=Store())],
                            value=IfExp(
                                test=Name(id='work_days', ctx=Load()),
                                body=Name(id='work_days', ctx=Load()),
                                orelse=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
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
                                                slice=Constant(value='crm.team', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Constant(value='|', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='use_leads', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='use_opportunities', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='assignment_optout', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_action_assign_leads',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='work_days',
                                        value=Name(id='work_days', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
                    name='action_assign_leads',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='work_days', annotation=None, type_comment=None),
                            arg(arg='log', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=1, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Manual (direct) leads assignment. This method both\n\n          * assigns leads to teams given by self;\n          * assigns leads to salespersons belonging to self;\n\n        See sub methods for more details about assign process.\n\n        :param float work_days: number of work days to consider when assigning leads\n          to teams or salespersons. We consider that Member.assignment_max (or\n          its equivalent on team model) targets 30 work days. We make a ratio\n          between expected number of work days and maximum assignment for those\n          30 days to know lead count to assign.\n\n        :return action: a client notification giving some insights on assign\n          process;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='teams_data', ctx=Store()),
                                        Name(id='members_data', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_assign_leads',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='work_days',
                                        value=Name(id='work_days', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='logs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_assign_leads_logs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='teams_data', ctx=Load()),
                                    Name(id='members_data', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html_message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='<br />', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='logs', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='notif_message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='logs', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='log_action', ctx=Store())],
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='Lead Assignment requested by %(user_name)s', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='user_name',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='log_message', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='<p>%s<br /><br />%s</p>', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='log_action', ctx=Load()),
                                        Name(id='html_message', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_message_log_batch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bodies',
                                        value=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='team', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='log_message', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='team', ctx=Store()),
                                                            iter=Name(id='self', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.client', kind=None),
                                    Constant(value='display_notification', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='title', kind=None),
                                            Constant(value='message', kind=None),
                                            Constant(value='next', kind=None),
                                        ],
                                        values=[
                                            Constant(value='success', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Leads Assigned', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='notif_message', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='type', kind=None)],
                                                values=[Constant(value='ir.actions.act_window_close', kind=None)],
                                            ),
                                        ],
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
                    name='_action_assign_leads',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='work_days', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Private method for lead assignment. This method both\n\n          * assigns leads to teams given by self;\n          * assigns leads to salespersons belonging to self;\n\n        See sub methods for more details about assign process.\n\n        :param float work_days: see ``CrmTeam.action_assign_leads()``;\n\n        :return teams_data, members_data: structure-based result of assignment\n          process. For more details about data see ``CrmTeam._allocate_leads()``\n          and ``CrmTeamMember._assign_and_convert_leads``;\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='sales_team.group_sale_manager', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='base.group_system', kind=None)],
                                            keywords=[],
                                        ),
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
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Lead/Opportunities automatic assignment is limited to managers or administrators', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='### START Lead Assignment (%d teams, %d sales persons, %.2f work_days)', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='crm_team_member_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='work_days', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='teams_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_allocate_leads',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='work_days',
                                        value=Name(id='work_days', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='### Team repartition done. Starting salesmen assignment.', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='members_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='crm_team_member_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_assign_and_convert_leads',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='work_days',
                                        value=Name(id='work_days', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='### END Lead Assignment', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='teams_data', ctx=Load()),
                                    Name(id='members_data', ctx=Load()),
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
                    name='_action_assign_leads_logs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='teams_data', annotation=None, type_comment=None),
                            arg(arg='members_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Tool method to prepare notification about assignment process result.\n\n        :param teams_data: see ``CrmTeam._allocate_leads()``;\n        :param members_data: see ``CrmTeamMember._assign_and_convert_leads()``;\n\n        :return list: list of formatted logs, ready to be formatted into a nice\n        plaintext or html message at caller's will\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='assigned', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=BinOp(
                                            left=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='teams_data', ctx=Load()),
                                                            slice=Name(id='team', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='assigned', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='teams_data', ctx=Load()),
                                                            slice=Name(id='team', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='merged', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='team', ctx=Store()),
                                                iter=Name(id='teams_data', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='duplicates', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='teams_data', ctx=Load()),
                                                        slice=Name(id='team', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='duplicates', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='team', ctx=Store()),
                                                iter=Name(id='teams_data', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='members', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='members_data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='members_assigned', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='member_data', ctx=Load()),
                                                    slice=Constant(value='assigned', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='member_data', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='members_data', ctx=Load()),
                                                        attr='values',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
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
                        Assign(
                            targets=[Name(id='message_parts', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='duplicates', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='message_parts', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='%(duplicates)s duplicates leads have been merged.', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='duplicates',
                                                        value=Name(id='duplicates', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='assigned', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='members_assigned', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assignment_max',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='message_parts', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='No allocated leads to %(team_name)s team because it has no capacity. Add capacity to its salespersons.', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='team_name',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
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
                                                            value=Name(id='message_parts', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='No allocated leads to %(team_name)s team and its salespersons because no unassigned lead matches its domain.', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='team_name',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
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
                                                    value=Name(id='message_parts', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='No allocated leads to any team or salesperson. Check your Sales Teams and Salespersons configuration as well as unassigned leads.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
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
                                        operand=Name(id='assigned', ctx=Load()),
                                    ),
                                    Name(id='members_assigned', ctx=Load()),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='message_parts', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='No new lead allocated to %(team_name)s team because no unassigned lead matches its domain.', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='team_name',
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
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
                                                    value=Name(id='message_parts', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='No new lead allocated to the teams because no lead match their domains.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='assigned', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='self', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='message_parts', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='%(assigned)s leads allocated to %(team_name)s team.', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='assigned',
                                                                        value=Name(id='assigned', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='team_name',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
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
                                                            value=Name(id='message_parts', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='%(assigned)s leads allocated among %(team_count)s teams.', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='assigned',
                                                                        value=Name(id='assigned', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='team_count',
                                                                        value=Call(
                                                                            func=Name(id='len', ctx=Load()),
                                                                            args=[Name(id='self', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='members_assigned', ctx=Load()),
                                    ),
                                    Name(id='assigned', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='message_parts', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='No lead assigned to salespersons because no unassigned lead matches their domains.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='members_assigned', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='message_parts', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='%(members_assigned)s leads assigned among %(member_count)s salespersons.', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='members_assigned',
                                                                value=Name(id='members_assigned', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='member_count',
                                                                value=Name(id='members', ctx=Load()),
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
                        ),
                        Return(
                            value=Name(id='message_parts', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_allocate_leads',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='work_days', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Allocate leads to teams given by self. This method sets ``team_id``\n        field on lead records that are unassigned (no team and no responsible).\n        No salesperson is assigned in this process. Its purpose is simply to\n        allocate leads within teams.\n\n        This process allocates all available leads on teams weighted by their\n        maximum assignment by month that indicates their relative workload.\n\n        Heuristic of this method is the following:\n          * find unassigned leads for each team, aka leads being\n            * without team, without user -> not assigned;\n            * not in a won stage, and not having False/0 (lost) or 100 (won)\n              probability) -> live leads;\n            * if set, a delay after creation can be applied (see BUNDLE_HOURS_DELAY)\n              parameter explanations here below;\n            * matching the team's assignment domain (empty means\n              everything);\n\n          * assign a weight to each team based on their assignment_max that\n            indicates their relative workload;\n\n          * pick a random team using a weighted random choice and find a lead\n            to assign:\n\n            * remove already assigned leads from the available leads. If there\n              is not any lead spare to assign, remove team from active teams;\n            * pick the first lead and set the current team;\n            * when setting a team on leads, leads are also merged with their\n              duplicates. Purpose is to clean database and avoid assigning\n              duplicates to same or different teams;\n            * add lead and its duplicates to already assigned leads;\n\n          * pick another random team until their is no more leads to assign\n            to any team;\n\n        This process ensure that teams having overlapping domains will all\n        receive leads as lead allocation is done one lead at a time. This\n        allocation will be proportional to their size (assignment of their\n        members).\n\n        :config int crm.assignment.bundle: deprecated\n        :config int crm.assignment.commit.bundle: optional config parameter allowing\n          to set size of lead batch to be committed together. By default 100\n          which is a good trade-off between transaction time and speed\n        :config int crm.assignment.delay: optional config parameter giving a\n          delay before taking a lead into assignment process (BUNDLE_HOURS_DELAY)\n          given in hours. Purpose if to allow other crons or automated actions\n          to make their job. This option is mainly historic as its purpose was\n          to let automated actions prepare leads and score before PLS was added\n          into CRM. This is now not required anymore but still supported;\n\n        :param float work_days: see ``CrmTeam.action_assign_leads()``;\n\n        :return teams_data: dict() with each team assignment result:\n          team: {\n            'assigned': set of lead IDs directly assigned to the team (no\n              duplicate or merged found);\n            'merged': set of lead IDs merged and assigned to the team (main\n              leads being results of merge process);\n            'duplicates': set of lead IDs found as duplicates and merged into\n              other leads. Those leads are unlinked during assign process and\n              are already removed at return of this method;\n          }, ...\n        ", kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='work_days', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0.2, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='work_days', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=30, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Leads team allocation should be done for at least 0.2 or maximum 30 work days, not %.2f.', kind=None),
                                                    Name(id='work_days', ctx=Load()),
                                                ],
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
                        Assign(
                            targets=[Name(id='BUNDLE_HOURS_DELAY', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
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
                                        args=[Constant(value='crm.assignment.delay', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='default',
                                                value=Constant(value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='BUNDLE_COMMIT_SIZE', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
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
                                            Constant(value='crm.assignment.commit.bundle', kind=None),
                                            Constant(value=100, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                            targets=[Name(id='max_create_dt', ctx=Store())],
                            value=BinOp(
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
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='timedelta',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='hours',
                                            value=Name(id='BUNDLE_HOURS_DELAY', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='duplicates_lead_cache', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='teams_data', ctx=Store()),
                                        Name(id='population', ctx=Store()),
                                        Name(id='weights', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='team', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='assignment_max',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='lead_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='literal_eval', ctx=Load()),
                                                        args=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='team', ctx=Load()),
                                                                        attr='assignment_domain',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='[]', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='create_date', kind=None),
                                                                    Constant(value='<', kind=None),
                                                                    Name(id='max_create_dt', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='team_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='stage_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='stage_id.is_won', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
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
                                Assign(
                                    targets=[Name(id='leads', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='crm.lead', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='lead_domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='lead', ctx=Store()),
                                    iter=Name(id='leads', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='lead', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='duplicates_lead_cache', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='duplicates_lead_cache', ctx=Load()),
                                                            slice=Name(id='lead', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lead', ctx=Load()),
                                                            attr='_get_lead_duplicates',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='email',
                                                                value=Attribute(
                                                                    value=Name(id='lead', ctx=Load()),
                                                                    attr='email_from',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
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
                                    targets=[
                                        Subscript(
                                            value=Name(id='teams_data', ctx=Load()),
                                            slice=Name(id='team', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='team', kind=None),
                                            Constant(value='leads', kind=None),
                                            Constant(value='assigned', kind=None),
                                            Constant(value='merged', kind=None),
                                            Constant(value='duplicates', kind=None),
                                        ],
                                        values=[
                                            Name(id='team', ctx=Load()),
                                            Name(id='leads', ctx=Load()),
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='population', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='team', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='weights', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
                                                attr='assignment_max',
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
                        If(
                            test=Name(id='auto_commit', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='global_data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='assigned',
                                        value=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='merged',
                                        value=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='duplicates',
                                        value=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='leads_done_ids', ctx=Store()),
                                        Name(id='lead_unlink_ids', ctx=Store()),
                                        Name(id='counter', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='population', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='counter', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='team', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='choices',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='population', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='weights',
                                                    value=Name(id='weights', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='k',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='teams_data', ctx=Load()),
                                                slice=Name(id='team', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='leads', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='teams_data', ctx=Load()),
                                                            slice=Name(id='team', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='leads', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='l', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='l', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotIn()],
                                                            comparators=[Name(id='leads_done_ids', ctx=Load())],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Subscript(
                                                value=Name(id='teams_data', ctx=Load()),
                                                slice=Name(id='team', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='leads', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='population_index', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='population', ctx=Load()),
                                                    attr='index',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='team', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='population', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='population_index', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='weights', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='population_index', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='candidate_lead', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='teams_data', ctx=Load()),
                                                slice=Name(id='team', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='leads', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='assign_res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='team', ctx=Load()),
                                            attr='_allocate_leads_deduplicate',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='candidate_lead', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='duplicates_cache',
                                                value=Name(id='duplicates_lead_cache', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='key', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Constant(value='assigned', kind=None),
                                            Constant(value='merged', kind=None),
                                            Constant(value='duplicates', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='teams_data', ctx=Load()),
                                                            slice=Name(id='team', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='key', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='assign_res', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='leads_done_ids', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='assign_res', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
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
                                                        value=Name(id='global_data', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='assign_res', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lead_unlink_ids', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='assign_res', ctx=Load()),
                                                slice=Constant(value='duplicates', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='auto_commit', ctx=Load()),
                                            Compare(
                                                left=BinOp(
                                                    left=Name(id='counter', ctx=Load()),
                                                    op=Mod(),
                                                    right=Name(id='BUNDLE_COMMIT_SIZE', ctx=Load()),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
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
                                                                slice=Constant(value='crm.lead', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='lead_unlink_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='lead_unlink_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
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
                        ),
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
                                                slice=Constant(value='crm.lead', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='lead_unlink_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='auto_commit', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='## Assigned %s leads', kind=None),
                                    BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='global_data', ctx=Load()),
                                                    slice=Constant(value='assigned', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='global_data', ctx=Load()),
                                                    slice=Constant(value='merged', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='team', ctx=Store()),
                                    Name(id='team_data', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='teams_data', ctx=Load()),
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='## Assigned %s leads to team %s', kind=None),
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='team_data', ctx=Load()),
                                                            slice=Constant(value='assigned', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='team_data', ctx=Load()),
                                                            slice=Constant(value='merged', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='team', ctx=Load()),
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
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\tLeads: direct assign %s / merge result %s / duplicates merged: %s', kind=None),
                                            Subscript(
                                                value=Name(id='team_data', ctx=Load()),
                                                slice=Constant(value='assigned', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='team_data', ctx=Load()),
                                                slice=Constant(value='merged', kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='team_data', ctx=Load()),
                                                slice=Constant(value='duplicates', kind=None),
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
                        Return(
                            value=Name(id='teams_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_allocate_leads_deduplicate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='leads', annotation=None, type_comment=None),
                            arg(arg='duplicates_cache', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Assign leads to sales team given by self by calling lead tool\n        method _handle_salesmen_assignment. In this method we deduplicate leads\n        allowing to reduce number of resulting leads before assigning them\n        to salesmen.\n\n        :param leads: recordset of leads to assign to current team;\n        :param duplicates_cache: if given, avoid to perform a duplicate search\n          and fetch information in it instead;\n        ', kind=None),
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
                            targets=[Name(id='duplicates_cache', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='duplicates_cache', ctx=Load()),
                                    ops=[IsNot()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Name(id='duplicates_cache', ctx=Load()),
                                orelse=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_assigned', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='crm.lead', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='leads_done_ids', ctx=Store()),
                                        Name(id='leads_merged_ids', ctx=Store()),
                                        Name(id='leads_dup_ids', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_dups_dict', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='lead', ctx=Store()),
                            iter=Name(id='leads', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='lead', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='leads_done_ids', ctx=Load())],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='lead', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='duplicates_cache', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='duplicates_cache', ctx=Load()),
                                                            slice=Name(id='lead', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lead', ctx=Load()),
                                                            attr='_get_lead_duplicates',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='email',
                                                                value=Attribute(
                                                                    value=Name(id='lead', ctx=Load()),
                                                                    attr='email_from',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='lead_duplicates', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='duplicates_cache', ctx=Load()),
                                                        slice=Name(id='lead', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='lead_duplicates', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='leads_dups_dict', ctx=Load()),
                                                            slice=Name(id='lead', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='lead_duplicates', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='leads_done_ids', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=BinOp(
                                                                    left=Name(id='lead', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Name(id='lead_duplicates', ctx=Load()),
                                                                ),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                AugAssign(
                                                    target=Name(id='leads_assigned', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='lead', ctx=Load()),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='leads_done_ids', ctx=Load()),
                                                            attr='add',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='lead', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
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
                        Assign(
                            targets=[Name(id='dups_to_assign', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='lead', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='lead', ctx=Store()),
                                        iter=Name(id='leads_dups_dict', ctx=Load()),
                                        ifs=[],
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
                                            value=Name(id='leads_assigned', ctx=Load()),
                                            attr='union',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='dups_to_assign', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_handle_salesmen_assignment',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='user_ids',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='team_id',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        For(
                            target=Name(id='lead', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='leads', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='lead', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Name(id='lead', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='leads_dups_dict', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lead_duplicates', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='leads_dups_dict', ctx=Load()),
                                        slice=Name(id='lead', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='merged', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lead_duplicates', ctx=Load()),
                                            attr='_merge_opportunity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='user_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='team_id',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='auto_unlink',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='max_length',
                                                value=Constant(value=0, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='leads_dup_ids', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=Name(id='lead_duplicates', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='merged', ctx=Load()),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='leads_merged_ids', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='merged', ctx=Load()),
                                                attr='id',
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='assigned', kind=None),
                                    Constant(value='merged', kind=None),
                                    Constant(value='duplicates', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='leads_assigned', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='leads_merged_ids', ctx=Load()),
                                    Name(id='leads_dup_ids', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_your_pipeline',
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
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='crm.crm_lead_action_pipeline', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_update_to_pipeline',
                                    ctx=Load(),
                                ),
                                args=[Name(id='action', ctx=Load())],
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
                    name='action_opportunity_forecast',
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
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='crm.crm_lead_action_forecast', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_action_update_to_pipeline',
                                    ctx=Load(),
                                ),
                                args=[Name(id='action', ctx=Load())],
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
                    name='_action_update_to_pipeline',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_team_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='sale_team_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='user_team_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='user_team_id', ctx=Store())],
                                    value=Attribute(
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
                                                                Constant(value='id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='user_team_id', ctx=Load()),
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
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='user_team_id', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            args=[List(elts=[], ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='limit',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='help', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value="<p class='o_view_nocontent_smiling_face'>Add new opportunities</p><p>\n    Looks like you are not a member of a Sales Team. You should add yourself\n    as a member of one of the Sales Team.\n</p>", kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='user_team_id', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='help', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="<p>As you don't belong to any Sales Team, Odoo opens the first one by default.</p>", kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='action_context', ctx=Store())],
                            value=Call(
                                func=Name(id='safe_eval', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='action', ctx=Load()),
                                        slice=Constant(value='context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='uid', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='user_team_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action_context', ctx=Load()),
                                            slice=Constant(value='default_team_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='user_team_id', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='context', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='action_context', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
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
                    name='_compute_dashboard_button_name',
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
                                        args=[
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_dashboard_button_name',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='team_with_pipelines', ctx=Store())],
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
                                            args=[arg(arg='el', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='use_opportunities',
                                            ctx=Load(),
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
                                    value=Name(id='team_with_pipelines', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='dashboard_button_name', kind=None)],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Pipeline', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                    name='action_primary_channel_button',
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='use_opportunities',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.actions.actions', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_for_xml_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='crm.crm_case_form_view_salesteams_opportunity', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='rcontext', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='team', kind=None)],
                                        values=[Name(id='self', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='help', kind=None),
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
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render_template',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='crm.crm_action_helper', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Name(id='rcontext', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='action', ctx=Load()),
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
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='action_primary_channel_button',
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
                    name='_graph_get_model',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='use_opportunities',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='crm.lead', kind=None),
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
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_graph_get_model',
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
                    name='_graph_date_column',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='use_opportunities',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='create_date', kind=None),
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
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_graph_date_column',
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
                    name='_graph_y_query',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='use_opportunities',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Constant(value='count(*)', kind=None),
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
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_graph_y_query',
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
                    name='_extra_sql_conditions',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='use_opportunities',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Constant(value="AND type LIKE 'opportunity'", kind=None),
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
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_extra_sql_conditions',
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
                    name='_graph_title_and_key',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='use_opportunities',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Constant(value='', kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='New Opportunities', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
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
                                            Name(id='Team', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_graph_title_and_key',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
