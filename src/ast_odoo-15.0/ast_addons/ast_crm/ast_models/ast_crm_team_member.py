Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='crm.team.member', kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='crm_team_id.assignment_enabled', kind=None),
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
                        args=[Constant(value='Average Leads Capacity (on 30 days)', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=30, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_month_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Leads (30 days)', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_lead_month_count', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Lead assigned to this member those last 30 days', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_lead_month_count',
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
                            target=Name(id='member', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='member', ctx=Load()),
                                                    attr='user_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='member', ctx=Load()),
                                                    attr='crm_team_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='member', ctx=Load()),
                                                    attr='lead_month_count',
                                                    ctx=Store(),
                                                ),
                                            ],
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
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='active_test',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='member', ctx=Load()),
                                                            attr='_get_lead_month_domain',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
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
                                                Attribute(
                                                    value=Name(id='member', ctx=Load()),
                                                    attr='lead_month_count',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
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
                                Constant(value='user_id', kind=None),
                                Constant(value='crm_team_id', kind=None),
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
                            target=Name(id='member', ctx=Store()),
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
                                                                value=Name(id='member', ctx=Load()),
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
                                                                args=[Constant(value='Member assignment domain for user %(user)s and team %(team)s is incorrectly formatted', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='user',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='member', ctx=Load()),
                                                                                attr='user_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='team',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='member', ctx=Load()),
                                                                                attr='crm_team_id',
                                                                                ctx=Load(),
                                                                            ),
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
                    name='_get_lead_month_domain',
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
                            targets=[Name(id='limit_date', ctx=Store())],
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
                                            arg='days',
                                            value=Constant(value=30, kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='user_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='team_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='crm_team_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_open', kind=None),
                                            Constant(value='>=', kind=None),
                                            Name(id='limit_date', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='_assign_and_convert_leads',
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
                            value=Constant(value=" Main processing method to assign leads to sales team members. It also\n        converts them into opportunities. This method should be called after\n        ``_allocate_leads`` as this method assigns leads already allocated to\n        the member's team. Its main purpose is therefore to distribute team\n        workload on its members based on their capacity.\n\n        Preparation\n\n          * prepare lead domain for each member. It is done using a logical\n            AND with team's domain and member's domain. Member domains further\n            restricts team domain;\n          * prepare a set of available leads for each member by searching for\n            leads matching domain with a sufficient limit to ensure all members\n            will receive leads;\n          * prepare a weighted population sample. Population are members that\n            should received leads. Initial weight is the number of leads to\n            assign to that specific member. This is minimum value between\n            * remaining this month: assignment_max - number of lead already\n              assigned this month;\n            * days-based assignment: assignment_max with a ratio based on\n              ``work_days`` parameter (see ``CrmTeam.action_assign_leads()``)\n            * e.g. Michel Poilvache (max: 30 - currently assigned: 15) limit\n              for 2 work days: min(30-15, 30/15) -> 2 leads assigned\n            * e.g. Michel Tartopoil (max: 30 - currently assigned: 26) limit\n              for 10 work days: min(30-26, 30/3) -> 4 leads assigned\n\n        This method then follows the following heuristic\n\n          * take a weighted random choice in population;\n          * find first available (not yet assigned) lead in its lead set;\n          * if found:\n            * convert it into an opportunity and assign member as salesperson;\n            * lessen member's weight so that other members have an higher\n              probability of being picked up next;\n          * if not found: consider this member is out of assignment process,\n            remove it from population so that it is not picked up anymore;\n\n        Assignment is performed one lead at a time for fairness purpose. Indeed\n        members may have overlapping domains within a given team. To ensure\n        some fairness in process once a member receives a lead, a new choice is\n        performed with updated weights. This is not optimal from performance\n        point of view but increases probability leads are correctly distributed\n        within the team.\n\n        :param float work_days: see ``CrmTeam.action_assign_leads()``;\n\n        :return members_data: dict() with each member assignment result:\n          membership: {\n            'assigned': set of lead IDs directly assigned to the member;\n          }, ...\n\n        ", kind=None),
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='members_data', ctx=Store()),
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
                        Assign(
                            targets=[Name(id='members', ctx=Store())],
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
                                            args=[arg(arg='member', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='member', ctx=Load()),
                                                        attr='assignment_optout',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='member', ctx=Load()),
                                                        attr='assignment_max',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Gt()],
                                                    comparators=[Constant(value=0, kind=None)],
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='members', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='members_data', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lead_limit', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='member', ctx=Load()),
                                                attr='_get_assignment_quota',
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
                                        generators=[
                                            comprehension(
                                                target=Name(id='member', ctx=Store()),
                                                iter=Name(id='members', ctx=Load()),
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
                        For(
                            target=Name(id='member', ctx=Store()),
                            iter=Name(id='members', ctx=Load()),
                            body=[
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
                                                                        value=Name(id='member', ctx=Load()),
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
                                                            Constant(value='&', kind=None),
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='date_open', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='team_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='member', ctx=Load()),
                                                                            attr='crm_team_id',
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
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='probability DESC', kind=None),
                                            ),
                                            keyword(
                                                arg='limit',
                                                value=Name(id='lead_limit', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='to_assign', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='member', ctx=Load()),
                                            attr='_get_assignment_quota',
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
                                    targets=[
                                        Subscript(
                                            value=Name(id='members_data', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='member', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(
                                        keys=[
                                            Constant(value='team_member', kind=None),
                                            Constant(value='max', kind=None),
                                            Constant(value='to_assign', kind=None),
                                            Constant(value='leads', kind=None),
                                            Constant(value='assigned', kind=None),
                                        ],
                                        values=[
                                            Name(id='member', ctx=Load()),
                                            Attribute(
                                                value=Name(id='member', ctx=Load()),
                                                attr='assignment_max',
                                                ctx=Load(),
                                            ),
                                            Name(id='to_assign', ctx=Load()),
                                            Name(id='leads', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='crm.lead', kind=None),
                                                ctx=Load(),
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
                                        args=[
                                            Attribute(
                                                value=Name(id='member', ctx=Load()),
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
                                            value=Name(id='weights', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='to_assign', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_done_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='counter', ctx=Store())],
                            value=Constant(value=0, kind=None),
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
                            targets=[Name(id='commit_bundle_size', ctx=Store())],
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
                        While(
                            test=Name(id='population', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='counter', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='member_id', ctx=Store())],
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
                                    targets=[Name(id='member_index', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='population', ctx=Load()),
                                            attr='index',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='member_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='member_data', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='members_data', ctx=Load()),
                                        slice=Name(id='member_id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lead', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='lead', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='lead', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Name(id='member_data', ctx=Load()),
                                                            slice=Constant(value='leads', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='lead', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='leads_done_ids', ctx=Load())],
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
                                If(
                                    test=Name(id='lead', ctx=Load()),
                                    body=[
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
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='members_data', ctx=Load()),
                                                    slice=Name(id='member_id', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='assigned', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='lead', ctx=Load()),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='weights', ctx=Load()),
                                                    slice=Name(id='member_index', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='weights', ctx=Load()),
                                                    slice=Name(id='member_index', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lead', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='mail_auto_subscribe_no_notify',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='convert_opportunity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='lead', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='user_ids',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='member_data', ctx=Load()),
                                                                    slice=Constant(value='team_member', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                                                            right=Name(id='commit_bundle_size', ctx=Load()),
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
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='weights', ctx=Load()),
                                                    slice=Name(id='member_index', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='weights', ctx=Load()),
                                            slice=Name(id='member_index', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        ops=[LtE()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='population', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='member_index', ctx=Load())],
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
                                                args=[Name(id='member_index', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='counter', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=100000, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='population', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
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
                            targets=[Name(id='result_data', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Subscript(
                                                    value=Name(id='member_info', ctx=Load()),
                                                    slice=Constant(value='team_member', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Dict(
                                                    keys=[Constant(value='assigned', kind=None)],
                                                    values=[
                                                        Subscript(
                                                            value=Name(id='member_info', ctx=Load()),
                                                            slice=Constant(value='assigned', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='member_id', ctx=Store()),
                                                        Name(id='member_info', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='members_data', ctx=Load()),
                                                        attr='items',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Assigned %s leads to %s salesmen', kind=None),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='leads_done_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='members', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='member', ctx=Store()),
                                    Name(id='member_info', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='result_data', ctx=Load()),
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
                                            Constant(value='-> member %s: assigned %d leads (%s)', kind=None),
                                            Attribute(
                                                value=Name(id='member', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='member_info', ctx=Load()),
                                                        slice=Constant(value='assigned', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Name(id='member_info', ctx=Load()),
                                                slice=Constant(value='assigned', kind=None),
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
                            value=Name(id='result_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_assignment_quota',
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
                            value=Constant(value=' Compute assignment quota based on work_days. This quota includes\n        a compensation to speedup getting to the lead average (``assignment_max``).\n        As this field is a counter for "30 days" -> divide by requested work\n        days in order to have base assign number then add compensation.\n\n        :param float work_days: see ``CrmTeam.action_assign_leads()``;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='assign_ratio', ctx=Store())],
                            value=BinOp(
                                left=Name(id='work_days', ctx=Load()),
                                op=Div(),
                                right=Constant(value=30.0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_assign', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assignment_max',
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Name(id='assign_ratio', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compensation', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='max', ctx=Load()),
                                    args=[
                                        Constant(value=0, kind=None),
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='assignment_max',
                                                ctx=Load(),
                                            ),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='lead_month_count',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Name(id='to_assign', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Mult(),
                                right=Constant(value=0.2, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='to_assign', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='compensation', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
