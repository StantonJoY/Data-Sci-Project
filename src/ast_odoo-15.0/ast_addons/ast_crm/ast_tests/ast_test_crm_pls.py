Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mail.tests.common',
            names=[alias(name='mail_new_test_user', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Date', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='Form', asname=None),
                alias(name='tagged', asname=None),
                alias(name='users', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestCRMPLS',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                            value=Constant(value=' Keep a limited setup to ensure tests are not impacted by other\n        records created in CRM common. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestCRMPLS', ctx=Load()),
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
                                    attr='company_main',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='user',
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='user_sales_manager',
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
                                        value=Constant(value='user_sales_manager', kind=None),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Constant(value='Martin PLS Sales Manager', kind=None),
                                    ),
                                    keyword(
                                        arg='email',
                                        value=Constant(value='crm_manager@test.example.com', kind=None),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='company_main',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='notification_type',
                                        value=Constant(value='inbox', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='sales_team.group_sale_manager,base.group_partner_manager', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='pls_team',
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
                                        slice=Constant(value='crm.team', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='PLS Team', kind=None)],
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
                    name='_get_lead_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='team_id', annotation=None, type_comment=None),
                            arg(arg='name_suffix', annotation=None, type_comment=None),
                            arg(arg='country_id', annotation=None, type_comment=None),
                            arg(arg='state_id', annotation=None, type_comment=None),
                            arg(arg='email_state', annotation=None, type_comment=None),
                            arg(arg='phone_state', annotation=None, type_comment=None),
                            arg(arg='source_id', annotation=None, type_comment=None),
                            arg(arg='stage_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='state_id', kind=None),
                                    Constant(value='email_state', kind=None),
                                    Constant(value='phone_state', kind=None),
                                    Constant(value='source_id', kind=None),
                                    Constant(value='stage_id', kind=None),
                                    Constant(value='country_id', kind=None),
                                    Constant(value='team_id', kind=None),
                                ],
                                values=[
                                    BinOp(
                                        left=Constant(value='lead_', kind=None),
                                        op=Add(),
                                        right=Name(id='name_suffix', ctx=Load()),
                                    ),
                                    Constant(value='opportunity', kind=None),
                                    Name(id='state_id', ctx=Load()),
                                    Name(id='email_state', ctx=Load()),
                                    Name(id='phone_state', ctx=Load()),
                                    Name(id='source_id', ctx=Load()),
                                    Name(id='stage_id', ctx=Load()),
                                    Name(id='country_id', ctx=Load()),
                                    Name(id='team_id', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_leads_with_tags',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tag_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Lead', ctx=Store())],
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
                            targets=[Name(id='team_id', ctx=Store())],
                            value=Attribute(
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
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[Constant(value='name', kind=None)],
                                            values=[Constant(value='blup', kind=None)],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_to_create', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=150, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='i', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=50, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='leads_to_create', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='tag_ids', kind=None),
                                                            Constant(value='team_id', kind=None),
                                                        ],
                                                        values=[
                                                            BinOp(
                                                                left=Constant(value='lead_tag_%s', kind=None),
                                                                op=Mod(),
                                                                right=Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[Name(id='i', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=4, kind=None),
                                                                            Subscript(
                                                                                value=Name(id='tag_ids', ctx=Load()),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='team_id', ctx=Load()),
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
                                                left=Name(id='i', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Constant(value=100, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='leads_to_create', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='tag_ids', kind=None),
                                                                    Constant(value='team_id', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='lead_tag_%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[Name(id='i', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=4, kind=None),
                                                                                    Subscript(
                                                                                        value=Name(id='tag_ids', ctx=Load()),
                                                                                        slice=Constant(value=1, kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='team_id', ctx=Load()),
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
                                                            value=Name(id='leads_to_create', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='tag_ids', kind=None),
                                                                    Constant(value='team_id', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='lead_tag_%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Call(
                                                                            func=Name(id='str', ctx=Load()),
                                                                            args=[Name(id='i', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Name(id='tag_ids', ctx=Load()),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='team_id', ctx=Load()),
                                                                ],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_with_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='leads_to_create', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='leads_with_tags', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_crm_lead_pls_update',
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
                            value=Constant(value=' We test here that the wizard for updating probabilities from settings\n            is getting correct value from config params and after updating values\n            from the wizard, the config params are correctly updated\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='frequency_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead.scoring.frequency.field', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pls_fields_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='frequency_fields', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='field_id.name', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pls_start_date_str', ctx=Store())],
                            value=Constant(value='2021-01-01', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrConfigSudo', ctx=Store())],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrConfigSudo', ctx=Load()),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.pls_start_date', kind=None),
                                    Name(id='pls_start_date_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrConfigSudo', ctx=Load()),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.pls_fields', kind=None),
                                    Name(id='pls_fields_str', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='date_to_update', ctx=Store())],
                            value=Constant(value='2021-02-02', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fields_to_remove', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='frequency_fields', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='f', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Name(id='f', ctx=Load()),
                                                    attr='field_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                List(
                                                    elts=[
                                                        Constant(value='source_id', kind=None),
                                                        Constant(value='lang_id', kind=None),
                                                    ],
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
                            targets=[Name(id='fields_after_updation_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=',', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=Name(id='frequency_fields', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='fields_to_remove', ctx=Load()),
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='field_id.name', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pls_update_wizard', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead.pls.update', kind=None),
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
                                    context_expr=Name(id='pls_update_wizard', ctx=Load()),
                                    optional_vars=None,
                                ),
                            ],
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
                                                func=Attribute(
                                                    value=Name(id='Date', ctx=Load()),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='pls_update_wizard', ctx=Load()),
                                                        attr='pls_start_date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='pls_start_date_str', ctx=Load()),
                                            Constant(value='Correct date is taken from config', kind=None),
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
                                                    value=Constant(value=',', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='f', ctx=Load()),
                                                                attr='field_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='f', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='pls_update_wizard', ctx=Load()),
                                                                    attr='pls_fields',
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
                                            Name(id='pls_fields_str', ctx=Load()),
                                            Constant(value='Correct fields are taken from config', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='pls_update_wizard', ctx=Load()),
                                            attr='pls_start_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='date_to_update', ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='field', ctx=Store()),
                                    iter=Name(id='fields_to_remove', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='pls_update_wizard', ctx=Load()),
                                                        attr='pls_fields',
                                                        ctx=Load(),
                                                    ),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='field', ctx=Load()),
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
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pls_update_wizard0', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pls_update_wizard', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='pls_update_wizard0', ctx=Load()),
                                    attr='action_update_crm_lead_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            value=Name(id='IrConfigSudo', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='crm.pls_start_date', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='date_to_update', ctx=Load()),
                                    Constant(value='Correct date is updated in config', kind=None),
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
                                            value=Name(id='IrConfigSudo', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='crm.pls_fields', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='fields_after_updation_str', ctx=Load()),
                                    Constant(value='Correct fields are updated in config', kind=None),
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
                    name='test_predictive_lead_scoring',
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
                            value=Constant(value=" We test here computation of lead probability based on PLS Bayes.\n                We will use 3 different values for each possible variables:\n                country_id : 1,2,3\n                state_id: 1,2,3\n                email_state: correct, incorrect, None\n                phone_state: correct, incorrect, None\n                source_id: 1,2,3\n                stage_id: 1,2,3 + the won stage\n                And we will compute all of this for 2 different team_id\n            Note : We assume here that original bayes computation is correct\n            as we don't compute manually the probabilities.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Lead', ctx=Store())],
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
                            targets=[Name(id='LeadScoringFrequency', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='crm.lead.scoring.frequency', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state_values', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='correct', kind=None),
                                    Constant(value='incorrect', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='utm.source', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='limit',
                                            value=Constant(value=3, kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='state_ids', ctx=Store())],
                            value=Attribute(
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
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='limit',
                                            value=Constant(value=3, kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_ids', ctx=Store())],
                            value=Attribute(
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
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='limit',
                                            value=Constant(value=3, kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stage_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='crm.stage', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[List(elts=[], ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='limit',
                                            value=Constant(value=3, kind=None),
                                        ),
                                    ],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='won_stage_id', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='crm.stage', kind=None),
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
                                                        Constant(value='is_won', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value=True, kind=None),
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
                        Assign(
                            targets=[Name(id='team_ids', ctx=Store())],
                            value=Attribute(
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
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Dict(
                                                    keys=[Constant(value='name', kind=None)],
                                                    values=[Constant(value='Team Test 1', kind=None)],
                                                ),
                                                Dict(
                                                    keys=[Constant(value='name', kind=None)],
                                                    values=[Constant(value='Team Test 2', kind=None)],
                                                ),
                                                Dict(
                                                    keys=[Constant(value='name', kind=None)],
                                                    values=[Constant(value='Team Test 3', kind=None)],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_to_create', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=3, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='leads_to_create', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_lead_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='team_ids', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='team_1_%s', kind=None),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='i', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='country_ids', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='state_ids', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='state_values', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='state_values', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='source_ids', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='stage_ids', ctx=Load()),
                                                        slice=Name(id='i', ctx=Load()),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_1_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=3, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_1_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=4, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_2_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=5, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_2_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=6, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_2_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=7, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_2_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=8, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='team_2_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=9, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=False, kind=None),
                                            BinOp(
                                                left=Constant(value='no_team_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=10, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=False, kind=None),
                                            BinOp(
                                                left=Constant(value='no_team_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=11, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=False, kind=None),
                                            BinOp(
                                                left=Constant(value='no_team_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=12, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                                    value=Name(id='leads_to_create', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_lead_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=False, kind=None),
                                            BinOp(
                                                left=Constant(value='no_team_%s', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='str', ctx=Load()),
                                                    args=[Constant(value=13, kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='country_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='state_values', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='source_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stage_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='leads', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='leads_to_create', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_with_no_team', ctx=Store())],
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
                                    value=Name(id='leads_with_no_team', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='team_id', kind=None)],
                                        values=[
                                            Subscript(
                                                value=Name(id='team_ids', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
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
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.pls_start_date', kind=None),
                                    Constant(value='2000-01-01', kind=None),
                                ],
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
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.pls_fields', kind=None),
                                    Constant(value='country_id,state_id,email_state,phone_state,source_id,tag_ids', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=5, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=6, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=7, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=10, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=11, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=12, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=33.49, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=7.74, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lead_13_team_3_proba', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Name(id='leads', ctx=Load()),
                                    slice=Constant(value=13, kind=None),
                                    ctx=Load(),
                                ),
                                attr='automated_probability',
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='lead_13_team_3_proba', ctx=Load()),
                                            Constant(value=35.09, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads_with_no_team', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='team_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lead_13_no_team_proba', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Name(id='leads', ctx=Load()),
                                    slice=Constant(value=13, kind=None),
                                    ctx=Load(),
                                ),
                                attr='automated_probability',
                                ctx=Load(),
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
                                    Compare(
                                        left=Name(id='lead_13_team_3_proba', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=13, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='Probability for leads with no team should be different than if they where in their own team.', kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='lead_13_no_team_proba', ctx=Load()),
                                            Constant(value=36.65, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lead_4_stage_0_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=4, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='stage_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Subscript(
                                                        value=Name(id='stage_ids', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
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
                            targets=[Name(id='lead_4_stage_won_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=4, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='stage_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='won_stage_id', ctx=Load()),
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
                            targets=[Name(id='lead_4_country_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=4, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=4, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_4_email_state_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=4, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='email_state', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='leads', ctx=Load()),
                                                                    slice=Constant(value=4, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='email_state',
                                                                ctx=Load(),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_9_stage_0_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='stage_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Subscript(
                                                        value=Name(id='stage_ids', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
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
                            targets=[Name(id='lead_9_stage_won_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='stage_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='won_stage_id', ctx=Load()),
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
                            targets=[Name(id='lead_9_country_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_9_email_state_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='email_state', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='leads', ctx=Load()),
                                                                    slice=Constant(value=9, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='email_state',
                                                                ctx=Load(),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=9, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lead_9_country_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
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
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='team_id',
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
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='country_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='leads', ctx=Load()),
                                                                slice=Constant(value=9, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='country_id',
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=33.49, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=7.74, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='leads', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='is_automated_probability',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='leads', ctx=Load()),
                                            slice=Constant(value=8, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='is_automated_probability',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='toggle_active',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='stage_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='won_stage_id', ctx=Load()),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='toggle_active',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='stage_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='stage_ids', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='toggle_active',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=3, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='stage_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='stage_ids', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=8, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='stage_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='stage_ids', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_4_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_4_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.1, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='won_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_0_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
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
                                        value=Name(id='lead_9_stage_won_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_country_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.1, kind=None),
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
                                        value=Name(id='lead_9_email_state_freq', ctx=Load()),
                                        attr='lost_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=3, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='probability',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=40, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='leads', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='is_automated_probability',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                        value=Subscript(
                                            value=Name(id='leads', ctx=Load()),
                                            slice=Constant(value=8, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='is_automated_probability',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=20.87, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2.43, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=40, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2.43, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=8, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='country_ids', ctx=Load()),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=34.38, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=34.38, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='leads', ctx=Load()),
                                        slice=Constant(value=8, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='country_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='country_ids', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2.43, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2.43, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tag_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='crm.tag', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Dict(
                                                    keys=[Constant(value='name', kind=None)],
                                                    values=[Constant(value='Tag_test_1', kind=None)],
                                                ),
                                                Dict(
                                                    keys=[Constant(value='name', kind=None)],
                                                    values=[Constant(value='Tag_test_2', kind=None)],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leads_with_tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='generate_leads_with_tags',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tag_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads_with_tags', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=30, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads_with_tags', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=31, kind=None),
                                            upper=Constant(value=50, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads_with_tags', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=50, kind=None),
                                            upper=Constant(value=90, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads_with_tags', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=91, kind=None),
                                            upper=Constant(value=100, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads_with_tags', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=100, kind=None),
                                            upper=Constant(value=135, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_lost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='leads_with_tags', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=136, kind=None),
                                            upper=Constant(value=150, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='action_set_won',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tag_1_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='tag_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Subscript(
                                                        value=Name(id='tag_ids', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
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
                            targets=[Name(id='tag_2_freq', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='LeadScoringFrequency', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='variable', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='tag_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='value', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Subscript(
                                                        value=Name(id='tag_ids', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tag_1_freq', ctx=Load()),
                                                attr='won_count',
                                                ctx=Load(),
                                            ),
                                            Constant(value=33.1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tag_1_freq', ctx=Load()),
                                                attr='lost_count',
                                                ctx=Load(),
                                            ),
                                            Constant(value=65.1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tag_2_freq', ctx=Load()),
                                                attr='won_count',
                                                ctx=Load(),
                                            ),
                                            Constant(value=23.1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='tag_2_freq', ctx=Load()),
                                                attr='lost_count',
                                                ctx=Load(),
                                            ),
                                            Constant(value=75.1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads_with_tags', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lead_tag_1', ctx=Store())],
                            value=Subscript(
                                value=Name(id='leads_with_tags', ctx=Load()),
                                slice=Constant(value=30, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_tag_2', ctx=Store())],
                            value=Subscript(
                                value=Name(id='leads_with_tags', ctx=Load()),
                                slice=Constant(value=90, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lead_tag_1_2', ctx=Store())],
                            value=Subscript(
                                value=Name(id='leads_with_tags', ctx=Load()),
                                slice=Constant(value=135, kind=None),
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=33.69, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=23.51, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.05, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=5, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=23.51, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=33.69, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=23.51, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.05, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=23.51, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=33.69, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=23.51, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.05, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
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
                                                    left=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='lead', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        op=Mod(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='email_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='correct', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
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
                                                    left=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='lead', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        op=Mod(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=1, kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='email_state',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='incorrect', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads_with_tags', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4.21, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0.23, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
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
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.pls_fields', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads_with_tags', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=34.38, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=50.0, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
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
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='crm.pls_fields', kind=None),
                                    Constant(value='country_id,state_id,email_state,phone_state,source_id', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='leads_with_tags', ctx=Load()),
                                    attr='invalidate_cache',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4.21, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='leads', ctx=Load()),
                                                    slice=Constant(value=8, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0.23, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=5, kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=4, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='lead_tag_1_2', ctx=Load()),
                                    attr='tag_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Subscript(
                                                value=Name(id='tag_ids', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead_tag_1_2', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=28.6, kind=None),
                                            Constant(value=2, kind=None),
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
                    name='test_settings_pls_start_date',
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
                            targets=[Name(id='set_param', ctx=Store())],
                            value=Attribute(
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
                                attr='set_param',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='str_date_8_days_ago', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Date', ctx=Load()),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='Date', ctx=Load()),
                                                attr='today',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=8, kind=None),
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
                            targets=[Name(id='resConfig', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.config.settings', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_param', ctx=Load()),
                                args=[
                                    Constant(value='crm.pls_start_date', kind=None),
                                    Constant(value='2021-10-10', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_config_new', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resConfig', ctx=Load()),
                                    attr='new',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Date', ctx=Load()),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='res_config_new', ctx=Load()),
                                                attr='predictive_lead_scoring_start_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='2021-10-10', kind=None),
                                    Constant(value='If config param is a valid date, date in settings should match with config param', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_param', ctx=Load()),
                                args=[
                                    Constant(value='crm.pls_start_date', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_config_new', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resConfig', ctx=Load()),
                                    attr='new',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Date', ctx=Load()),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='res_config_new', ctx=Load()),
                                                attr='predictive_lead_scoring_start_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='str_date_8_days_ago', ctx=Load()),
                                    Constant(value='If config param is empty, date in settings should be set to 8 days before today', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='set_param', ctx=Load()),
                                args=[
                                    Constant(value='crm.pls_start_date', kind=None),
                                    Constant(value='One does not simply walk into system parameters to corrupt them', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_config_new', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='resConfig', ctx=Load()),
                                    attr='new',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='Date', ctx=Load()),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='res_config_new', ctx=Load()),
                                                attr='predictive_lead_scoring_start_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='str_date_8_days_ago', ctx=Load()),
                                    Constant(value='If config param is not a valid date, date in settings should be set to 8 days before today', kind=None),
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
                    name='test_pls_no_share_stage',
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
                            value=Constant(value=' We test here the situation where all stages are team specific, as there is\n            a current limitation (can be seen in _pls_get_won_lost_total_count) regarding \n            the first stage (used to know how many lost and won there is) that requires \n            to have no team assigned to it.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Lead', ctx=Store())],
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
                            targets=[Name(id='team_id', ctx=Store())],
                            value=Attribute(
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
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Dict(
                                                    keys=[Constant(value='name', kind=None)],
                                                    values=[Constant(value='Team Test', kind=None)],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
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
                                                slice=Constant(value='crm.stage', kind=None),
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='team_id', kind=None)],
                                        values=[Name(id='team_id', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lead', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='team_id', kind=None),
                                            Constant(value='probability', kind=None),
                                        ],
                                        values=[
                                            Constant(value='team', kind=None),
                                            Name(id='team_id', ctx=Load()),
                                            Constant(value=41.23, kind=None),
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
                                    value=Name(id='Lead', ctx=Load()),
                                    attr='_cron_update_automated_probabilities',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead', ctx=Load()),
                                                attr='probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=41.23, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                                            value=Name(id='tools', ctx=Load()),
                                            attr='float_compare',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='lead', ctx=Load()),
                                                attr='automated_probability',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                            Constant(value=2, kind=None),
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
                    name='test_team_unlink',
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
                            value=Constant(value=' Test that frequencies are sent to "no team" when unlinking a team\n        in order to avoid loosing too much informations. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='pls_team', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pls_team',
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
                                                ],
                                                ctx=Load(),
                                            ),
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
                        Assign(
                            targets=[Name(id='no_team', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='2', kind=None),
                                            Constant(value=0.1, kind=None),
                                            Constant(value=0.1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='3', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0.1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='variable', kind=None),
                                                Constant(value='value', kind=None),
                                                Constant(value='won_count', kind=None),
                                                Constant(value='lost_count', kind=None),
                                                Constant(value='team_id', kind=None),
                                            ],
                                            values=[
                                                Name(id='variable', ctx=Load()),
                                                Name(id='value', ctx=Load()),
                                                Name(id='won_count', ctx=Load()),
                                                Name(id='lost_count', ctx=Load()),
                                                Constant(value=False, kind=None),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='variable', ctx=Store()),
                                                        Name(id='value', ctx=Store()),
                                                        Name(id='won_count', ctx=Store()),
                                                        Name(id='lost_count', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='no_team', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='team', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value=0.1, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='2', kind=None),
                                            Constant(value=0.1, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='3', kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='existing_plsteam', ctx=Store())],
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
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='variable', kind=None),
                                                Constant(value='value', kind=None),
                                                Constant(value='won_count', kind=None),
                                                Constant(value='lost_count', kind=None),
                                                Constant(value='team_id', kind=None),
                                            ],
                                            values=[
                                                Name(id='variable', ctx=Load()),
                                                Name(id='value', ctx=Load()),
                                                Name(id='won_count', ctx=Load()),
                                                Name(id='lost_count', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='pls_team', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='variable', ctx=Store()),
                                                        Name(id='value', ctx=Store()),
                                                        Name(id='won_count', ctx=Store()),
                                                        Name(id='lost_count', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='team', ctx=Load()),
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
                                    value=Name(id='pls_team', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='final_noteam', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value=40, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='2', kind=None),
                                            Constant(value=0.1, kind=None),
                                            Constant(value=0.1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='3', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='1', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='country_id', kind=None),
                                            Constant(value='3', kind=None),
                                            Constant(value=30, kind=None),
                                            Constant(value=30, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                                        func=Attribute(
                                            value=Name(id='existing_plsteam', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='crm.lead.scoring.frequency', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Frequencies of unlinked teams should be unlinked (cascade)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                                    List(
                                                        elts=[
                                                            Constant(value='stage_id', kind=None),
                                                            Constant(value='country_id', kind=None),
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
                        For(
                            target=Name(id='frequency', ctx=Store()),
                            iter=Name(id='existing_noteam', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='stat', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='item', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='item', ctx=Store()),
                                                        iter=Name(id='final_noteam', ctx=Load()),
                                                        ifs=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='item', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
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
                                                                        left=Subscript(
                                                                            value=Name(id='item', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='frequency', ctx=Load()),
                                                attr='won_count',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stat', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
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
                                                value=Name(id='frequency', ctx=Load()),
                                                attr='lost_count',
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='stat', ctx=Load()),
                                                slice=Constant(value=3, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='existing_noteam', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='final_noteam', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_sales_manager', kind=None)],
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
                    args=[Constant(value='crm_lead_pls', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
