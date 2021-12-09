Module(
    body=[
        ImportFrom(
            module='odoo.addons.crm.tests.common',
            names=[alias(name='TestCrmCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.event.tests.common',
            names=[alias(name='TestEventCommon', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestEventCrmCommon',
            bases=[
                Name(id='TestCrmCommon', ctx=Load()),
                Name(id='TestEventCommon', ctx=Load()),
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
                                            Name(id='TestEventCrmCommon', ctx=Load()),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='event.lead.rule', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_lead_tag',
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
                                        slice=Constant(value='crm.tag', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='TagTest', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_rule_attendee',
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
                                        slice=Constant(value='event.lead.rule', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='lead_creation_basis', kind=None),
                                            Constant(value='lead_creation_trigger', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='event_registration_filter', kind=None),
                                            Constant(value='lead_type', kind=None),
                                            Constant(value='lead_user_id', kind=None),
                                            Constant(value='lead_tag_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Rule Attendee', kind=None),
                                            Constant(value='attendee', kind=None),
                                            Constant(value='create', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='ilike', kind=None),
                                                            Constant(value='@test.example.com', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='lead', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='user_sales_salesman',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='test_lead_tag',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_rule_order',
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
                                        slice=Constant(value='event.lead.rule', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='lead_creation_basis', kind=None),
                                            Constant(value='lead_creation_trigger', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='event_registration_filter', kind=None),
                                            Constant(value='lead_type', kind=None),
                                            Constant(value='lead_user_id', kind=None),
                                            Constant(value='lead_sales_team_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Rule Order', kind=None),
                                            Constant(value='order', kind=None),
                                            Constant(value='create', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='email', kind=None),
                                                            Constant(value='ilike', kind=None),
                                                            Constant(value='@test.example.com', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='opportunity', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='user_sales_leads',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='sales_team_1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_rule_order_done',
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
                                        slice=Constant(value='event.lead.rule', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='lead_creation_basis', kind=None),
                                            Constant(value='lead_creation_trigger', kind=None),
                                            Constant(value='event_registration_filter', kind=None),
                                            Constant(value='lead_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Rule Order: confirmed partner only', kind=None),
                                            Constant(value='order', kind=None),
                                            Constant(value='done', kind=None),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='partner_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='opportunity', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='batch_customer_data',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=BinOp(
                                    left=List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='partner_id', kind=None)],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='event_customer',
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
                                    op=Add(),
                                    right=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='phone', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='My Customer 00', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='event_customer2',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='email.00@test.example.com', kind=None),
                                                    Constant(value='0456000000', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=ListComp(
                                    elt=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Constant(value='My Customer %02d', kind=None),
                                                op=Mod(),
                                                right=Name(id='x', ctx=Load()),
                                            ),
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='x', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                                body=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='cls', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ref',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='base.public_partner', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            BinOp(
                                                left=Constant(value='email.%02d@test.example.com', kind=None),
                                                op=Mod(),
                                                right=Name(id='x', ctx=Load()),
                                            ),
                                            BinOp(
                                                left=Constant(value='04560000%02d', kind=None),
                                                op=Mod(),
                                                right=Name(id='x', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='x', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertLeadConvertion',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                            arg(arg='registrations', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='expected', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Tool method hiding details of lead value generation and check\n\n        :param lead: lead created through automated rule;\n        :param rule: event.lead.rule that created the lead;\n        :param event: original event;\n        :param registrations: source registrations (singleton or record set if done in batch);\n        :param partner: partner on lead;\n        ', kind=None),
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
                            targets=[Name(id='lead', ctx=Store())],
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
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='rule', ctx=Load()),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='lead', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    BinOp(
                                        left=Constant(value='Invalid registrations -> lead creation, found %s leads where only 1 is expected.', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='lead', ctx=Load())],
                                            keywords=[],
                                        ),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                    Name(id='registrations', ctx=Load()),
                                    Constant(value='Invalid registrations -> lead creation, too much registrations on it.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Attribute(
                                value=Name(id='registrations', ctx=Load()),
                                attr='event_id',
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='event', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Invalid registrations -> event assertion, all registrations should belong to same event', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='partner', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partner', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='expected_reg_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='_find_first_notnull',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='_find_first_notnull',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partner', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='expected_contact_name', ctx=Store())],
                                    value=IfExp(
                                        test=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='is_company',
                                                ctx=Load(),
                                            ),
                                        ),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expected_partner_name', ctx=Store())],
                                    value=IfExp(
                                        test=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='is_company',
                                            ctx=Load(),
                                        ),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='expected_contact_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='_find_first_notnull',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expected_partner_name', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='event_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='event', ctx=Load()),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='referred',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='name',
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='partner', ctx=Load()),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s - %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Name(id='expected_reg_name', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='False', kind=None),
                                    Attribute(
                                        value=Name(id='lead', ctx=Load()),
                                        attr='name',
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='contact_name',
                                        ctx=Load(),
                                    ),
                                    Name(id='expected_contact_name', ctx=Load()),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='partner_name',
                                        ctx=Load(),
                                    ),
                                    Name(id='expected_partner_name', ctx=Load()),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='email_from',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Name(id='partner', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='email',
                                            ctx=Load(),
                                        ),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='registrations', ctx=Load()),
                                                attr='_find_first_notnull',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='email', kind=None)],
                                            keywords=[],
                                        ),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='phone',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=Name(id='partner', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='phone',
                                            ctx=Load(),
                                        ),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='registrations', ctx=Load()),
                                                attr='_find_first_notnull',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='phone', kind=None)],
                                            keywords=[],
                                        ),
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='mobile',
                                        ctx=Load(),
                                    ),
                                    IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='partner', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='mobile',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='mobile',
                                            ctx=Load(),
                                        ),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='registrations', ctx=Load()),
                                                attr='_find_first_notnull',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='mobile', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='False', kind=None),
                                    Attribute(
                                        value=Name(id='lead', ctx=Load()),
                                        attr='description',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='registrations', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='registration', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='registration', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='lead', ctx=Load()),
                                                        attr='description',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertIn',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='registration', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='lead', ctx=Load()),
                                                                attr='description',
                                                                ctx=Load(),
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
                                If(
                                    test=Attribute(
                                        value=Name(id='registration', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='registration', ctx=Load()),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='lead', ctx=Load()),
                                                        attr='description',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='registration', ctx=Load()),
                                        attr='phone',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='registration', ctx=Load()),
                                                        attr='phone',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='lead', ctx=Load()),
                                                        attr='description',
                                                        ctx=Load(),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='lead', ctx=Load()),
                                        attr='type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='lead_type',
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='lead_user_id',
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='team_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='lead_sales_team_id',
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
                                        value=Name(id='lead', ctx=Load()),
                                        attr='tag_ids',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='lead_tag_ids',
                                        ctx=Load(),
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
