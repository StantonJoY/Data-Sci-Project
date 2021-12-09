Module(
    body=[
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='EventLeadRule',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=" Rule model for creating / updating leads from event registrations.\n\n    SPECIFICATIONS: CREATION TYPE\n\n    There are two types of lead creation:\n\n      * per attendee: create a lead for each registration;\n      * per order: create a lead for a group of registrations;\n\n    The last one is only available through interface if it is possible to register\n    a group of attendees in one action (when event_sale or website_event are\n    installed). Behavior itself is implemented directly in event_crm.\n\n    Basically a group is either a list of registrations belonging to the same\n    event and created in batch (website_event flow). With event_sale this\n    definition will be improved to be based on sale_order.\n\n    SPECIFICATIONS: CREATION TRIGGERS\n\n    There are three options to trigger lead creation. We consider basically that\n    lead quality increases if attendees confirmed or went to the event. Triggers\n    allow therefore to run rules:\n\n      * at attendee creation;\n      * at attendee confirmation;\n      * at attendee venue;\n\n    This trigger defines when the rule will run.\n\n    SPECIFICATIONS: FILTERING REGISTRATIONS\n\n    When a batch of registrations matches the rule trigger we filter them based\n    on conditions and rules defines on event_lead_rule model. Heuristic is the\n    following:\n\n      * the rule is active;\n      * if a filter is set: filter registrations based on this filter. This is\n        done like a search, and filter is a domain;\n      * if a company is set on the rule, it must match event's company. Note\n        that multi-company rules apply on event_lead_rule;\n      * if an event category it set, it must match;\n      * if an event is set, it must match;\n      * if both event and category are set, one of them must match (OR). If none\n        of those are set, it is considered as OK;\n\n    If conditions are met, leads are created with pre-filled informations defined\n    on the rule (type, user_id, team_id). Contact information coming from the\n    registrations are computed (customer, name, email, phone, mobile, contact_name).\n\n    SPECIFICATIONS: OTHER POINTS\n\n    Note that all rules matching their conditions are applied. This means more\n    than one lead can be created depending on the configuration. This is\n    intended in order to give more freedom to the user using the automatic\n    lead generation.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='event.lead.rule', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Event Lead Rules', kind=None),
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
                        args=[Constant(value='Rule Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='crm.lead', kind=None),
                            Constant(value='event_lead_rule_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Created Leads', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='sales_team.group_sale_salesman', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_creation_basis', ctx=Store())],
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
                                            Constant(value='attendee', kind=None),
                                            Constant(value='Per Attendee', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='order', kind=None),
                                            Constant(value='Per Order', kind=None),
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
                                value=Constant(value='Create', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='attendee', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Per Attendee : A Lead is created for each Attendee (B2C).\nPer Order : A single Lead is created per Ticket Batch/Sale Order (B2B)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_creation_trigger', ctx=Store())],
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
                                            Constant(value='create', kind=None),
                                            Constant(value='Attendees are created', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='confirm', kind=None),
                                            Constant(value='Attendees are confirmed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='done', kind=None),
                                            Constant(value='Attendees attended', kind=None),
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
                                value=Constant(value='When', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='create', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Creation: at attendee creation;\nConfirmation: when attendee is confirmed, manually or automatically;\nAttended: when attendance is confirmed and registration set to done;', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='event_type_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.type', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Event Categories', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Filter the attendees to include those of this specific event category. If not set, no event category restriction will be applied.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='event_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.event', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Event', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('company_id', 'in', [company_id or current_company_id, False])]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Filter the attendees to include those of this specific event. If not set, no event restriction will be applied.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Restrict the trigger of this rule to events belonging to a specific company.\nIf not set, no company restriction will be applied.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='event_registration_filter', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Registrations Domain', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Filter the attendees that will or not generate leads.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_type', ctx=Store())],
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
                                            Constant(value='lead', kind=None),
                                            Constant(value='Lead', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='opportunity', kind=None),
                                            Constant(value='Opportunity', kind=None),
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
                                value=Constant(value='Lead Type', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
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
                                    body=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.users', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='has_group',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='crm.group_use_lead', kind=None)],
                                            keywords=[],
                                        ),
                                        body=Constant(value='lead', kind=None),
                                        orelse=Constant(value='opportunity', kind=None),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default lead type when this rule is applied.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_sales_team_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='crm.team', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sales Team', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='set null', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Automatically assign the created leads to this Sales Team.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Salesperson', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Automatically assign the created leads to this Salesperson.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lead_tag_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='crm.tag', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Tags', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Automatically add these tags to the created leads.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_on_registrations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='registrations', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create or update leads based on rule configuration. Two main lead\n        management type exists\n\n          * per attendee: each registration creates a lead;\n          * per order: registrations are grouped per group and one lead is created\n            or updated with the batch (used mainly with sale order configuration\n            in event_sale);\n\n        Heuristic\n\n          * first, check existing lead linked to registrations to ensure no\n            duplication. Indeed for example attendee status change may trigger\n            the same rule several times;\n          * then for each rule, get the subset of registrations matching its\n            filters;\n          * then for each order-based rule, get the grouping information. This\n            give a list of registrations by group (event, sale_order), with maybe\n            an already-existing lead to update instead of creating a new one;\n          * finally apply rules. Attendee-based rules create a lead for each\n            attendee, group-based rules use the grouping information to create\n            or update leads;\n\n        :param registrations: event.registration recordset on which rules given by\n          self have to run. Triggers should already be checked, only filters are\n          applied here.\n\n        :return leads: newly-created leads. Updated leads are not returned.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='registrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registrations', ctx=Load()),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='existing_leads', ctx=Store())],
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
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='registration_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='registrations', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='event_lead_rule_id', kind=None),
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
                        Assign(
                            targets=[Name(id='rule_to_existing_regs', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='event.registration', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='lead', ctx=Store()),
                            iter=Name(id='existing_leads', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='rule_to_existing_regs', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='lead', ctx=Load()),
                                            attr='event_lead_rule_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='lead', ctx=Load()),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_registrations', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='event.registration', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rule_to_new_regs', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new_for_rule', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='reg', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Name(id='reg', ctx=Load()),
                                                    ops=[NotIn()],
                                                    comparators=[
                                                        Subscript(
                                                            value=Name(id='rule_to_existing_regs', ctx=Load()),
                                                            slice=Name(id='rule', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='rule_registrations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='_filter_registrations',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='new_for_rule', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='new_registrations', ctx=Store()),
                                    op=BitOr(),
                                    value=Name(id='rule_registrations', ctx=Load()),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rule_to_new_regs', ctx=Load()),
                                            slice=Name(id='rule', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='rule_registrations', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='new_registrations', ctx=Load()),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='id', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='order_based_rules', ctx=Store())],
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
                                            args=[arg(arg='rule', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='rule', ctx=Load()),
                                                attr='lead_creation_basis',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='order', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rule_group_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='new_registrations', ctx=Load()),
                                    attr='_get_lead_grouping',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='order_based_rules', ctx=Load()),
                                    Name(id='rule_to_new_regs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='lead_creation_basis',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='attendee', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='matching_registrations', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='rule_to_new_regs', ctx=Load()),
                                                        slice=Name(id='rule', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sorted',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='id', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='registration', ctx=Store()),
                                            iter=Name(id='matching_registrations', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lead_vals_list', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='registration', ctx=Load()),
                                                                    attr='_get_lead_values',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='rule', ctx=Load())],
                                                                keywords=[],
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
                                    orelse=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='toupdate_leads', ctx=Store()),
                                                    Name(id='group_key', ctx=Store()),
                                                    Name(id='group_registrations', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Subscript(
                                                value=Name(id='rule_group_info', ctx=Load()),
                                                slice=Name(id='rule', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='toupdate_leads', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='additionnal_description', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='group_registrations', ctx=Load()),
                                                                    attr='_get_lead_description',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='New registrations', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='line_counter',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        For(
                                                            target=Name(id='lead', ctx=Store()),
                                                            iter=Name(id='toupdate_leads', ctx=Load()),
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
                                                                                keys=[
                                                                                    Constant(value='description', kind=None),
                                                                                    Constant(value='registration_ids', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    BinOp(
                                                                                        left=Constant(value='%s<br/>%s', kind=None),
                                                                                        op=Mod(),
                                                                                        right=Tuple(
                                                                                            elts=[
                                                                                                Attribute(
                                                                                                    value=Name(id='lead', ctx=Load()),
                                                                                                    attr='description',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                Name(id='additionnal_description', ctx=Load()),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    ListComp(
                                                                                        elt=Tuple(
                                                                                            elts=[
                                                                                                Constant(value=4, kind=None),
                                                                                                Attribute(
                                                                                                    value=Name(id='reg', ctx=Load()),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ],
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        generators=[
                                                                                            comprehension(
                                                                                                target=Name(id='reg', ctx=Store()),
                                                                                                iter=Name(id='group_registrations', ctx=Load()),
                                                                                                ifs=[],
                                                                                                is_async=0,
                                                                                            ),
                                                                                        ],
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
                                                    orelse=[
                                                        If(
                                                            test=Name(id='group_registrations', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='lead_vals_list', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='group_registrations', ctx=Load()),
                                                                                    attr='_get_lead_values',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='rule', ctx=Load())],
                                                                                keywords=[],
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
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
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
                                        slice=Constant(value='crm.lead', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='lead_vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_filter_registrations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='registrations', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Keep registrations matching rule conditions. Those are\n\n          * if a filter is set: filter registrations based on this filter. This is\n            done like a search, and filter is a domain;\n          * if a company is set on the rule, it must match event's company. Note\n            that multi-company rules apply on event_lead_rule;\n          * if an event category it set, it must match;\n          * if an event is set, it must match;\n          * if both event and category are set, one of them must match (OR). If none\n            of those are set, it is considered as OK;\n\n        :param registrations: event.registration recordset on which rule filters\n          will be evaluated;\n        :return: subset of registrations matching rules\n        ", kind=None),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='event_registration_filter',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_registration_filter',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='[]', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='registrations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='filtered_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='literal_eval', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='event_registration_filter',
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
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='company_ok', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='registration', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=IfExp(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    body=Compare(
                                        left=Attribute(
                                            value=Name(id='registration', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    orelse=Constant(value=True, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event_or_event_type_ok', ctx=Store())],
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='registration', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=IfExp(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='event_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='event_type_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='event_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='event_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='registration', ctx=Load()),
                                                        attr='event_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='event_type_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='event_type_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    orelse=Constant(value=True, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='registrations', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Call(
                                                    func=Name(id='company_ok', ctx=Load()),
                                                    args=[Name(id='r', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='event_or_event_type_ok', ctx=Load()),
                                                    args=[Name(id='r', ctx=Load())],
                                                    keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
