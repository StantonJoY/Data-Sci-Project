Module(
    body=[
        ImportFrom(
            module='odoo.addons.test_event_full.tests.common',
            names=[alias(name='TestEventFullCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='users', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestEventCrm',
            bases=[Name(id='TestEventFullCommon', ctx=Load())],
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
                                            Name(id='TestEventCrm', ctx=Load()),
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
                                Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='TICKET1_COUNT',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='TICKET2_COUNT',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=3, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ticket1', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='event_0',
                                        ctx=Load(),
                                    ),
                                    attr='event_ticket_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ticket2', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='event_0',
                                        ctx=Load(),
                                    ),
                                    attr='event_ticket_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='customer_so',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='order_line', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='event_id', kind=None),
                                                                    Constant(value='event_ticket_id', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_qty', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='event_0',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ticket1', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='ticket1', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='TICKET1_COUNT',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='event_id', kind=None),
                                                                    Constant(value='event_ticket_id', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_qty', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='event_0',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ticket2', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='ticket2', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='TICKET2_COUNT',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=50, kind=None),
                                                                ],
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
                    name='test_event_crm_sale_customer',
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
                            value=Constant(value=' Test a SO with a real customer set on it, check partner propagation\n        as well as group-based lead update. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='customer_so', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='customer_so',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='t1_reg_vals', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[Name(id='customer_data', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='partner_id',
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='customer_so', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        keyword(
                                            arg='sale_order_line_id',
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='customer_so', ctx=Load()),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='customer_data', ctx=Store()),
                                        iter=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_customer_data',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='TICKET1_COUNT',
                                                    ctx=Load(),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='t1_registrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.registration', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='t1_reg_vals', ctx=Load())],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                    Name(id='t1_registrations', ctx=Load()),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_rule_order',
                                                    ctx=Load(),
                                                ),
                                                attr='lead_ids',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_rule_order_done',
                                            ctx=Load(),
                                        ),
                                        attr='lead_ids',
                                        ctx=Load(),
                                    ),
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
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Name(id='t1_registrations', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Name(id='customer_so', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='customer_so', ctx=Load()),
                                    attr='action_confirm',
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
                                        value=Name(id='customer_so', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='sale', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='registration_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='TICKET1_COUNT',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='TICKET2_COUNT',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='test_rule_order',
                                                    ctx=Load(),
                                                ),
                                                attr='lead_ids',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='test_rule_order_done',
                                            ctx=Load(),
                                        ),
                                        attr='lead_ids',
                                        ctx=Load(),
                                    ),
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
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Name(id='customer_so', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='done', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order_done',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Name(id='customer_so', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_sales_salesman', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_event_crm_sale_mixed_group',
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
                            value=Constant(value=' Test a mixed sale order line creation. This should not happen in a customer\n        use case but should be supported by the code. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='public_partner', ctx=Store())],
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
                                args=[Constant(value='base.public_partner', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='public_so', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='order_line', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='public_partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='event_id', kind=None),
                                                                    Constant(value='event_ticket_id', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_qty', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='event_0',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='event_0',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='event_ticket_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='event_0',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='event_ticket_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_so', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='customer_so',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mixed_reg_vals', ctx=Store())],
                            value=List(
                                elts=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website_customer_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='customer_so', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='sale_order_line_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='customer_so', ctx=Load()),
                                                            attr='order_line',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website_customer_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='customer_so', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='sale_order_line_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='customer_so', ctx=Load()),
                                                            attr='order_line',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website_customer_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='public_so', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='sale_order_line_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='public_so', ctx=Load()),
                                                            attr='order_line',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website_customer_data',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='public_so', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='sale_order_line_id',
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='public_so', ctx=Load()),
                                                            attr='order_line',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
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
                                        slice=Constant(value='event.registration', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='mixed_reg_vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='public_regs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
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
                                            left=Attribute(
                                                value=Name(id='reg', ctx=Load()),
                                                attr='sale_order_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='public_so', ctx=Load())],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='public_regs', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='customer_regs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
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
                                            left=Attribute(
                                                value=Name(id='reg', ctx=Load()),
                                                attr='sale_order_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='customer_so', ctx=Load())],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='customer_regs', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Name(id='public_regs', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Name(id='customer_regs', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Name(id='customer_so', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_sales_salesman', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_event_crm_sale_public',
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
                            value=Constant(value=' Test a SO with a public partner on it, then updated when SO is confirmed.\n        This somehow simulates a simplified website_event_sale flow. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='public_partner', ctx=Store())],
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
                                args=[Constant(value='base.public_partner', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_so', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sale.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='customer_so',
                                            ctx=Load(),
                                        ),
                                        attr='id',
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
                                    value=Name(id='customer_so', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='partner_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='public_partner', ctx=Load()),
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
                            targets=[Name(id='t1_reg_vals', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='dict', ctx=Load()),
                                    args=[Name(id='customer_data', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='partner_id',
                                            value=Attribute(
                                                value=Name(id='public_partner', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        keyword(
                                            arg='sale_order_line_id',
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='customer_so', ctx=Load()),
                                                        attr='order_line',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='customer_data', ctx=Store()),
                                        iter=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='website_customer_data',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='TICKET1_COUNT',
                                                    ctx=Load(),
                                                ),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='t1_registrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.registration', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='t1_reg_vals', ctx=Load())],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_0',
                                            ctx=Load(),
                                        ),
                                        attr='registration_ids',
                                        ctx=Load(),
                                    ),
                                    Name(id='t1_registrations', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Name(id='t1_registrations', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='customer_so', ctx=Load()),
                                    attr='action_confirm',
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
                                        value=Name(id='customer_so', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='sale', kind=None),
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
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='registration_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='TICKET1_COUNT',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='TICKET2_COUNT',
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
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Name(id='t1_registrations', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='customer_so', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='partner_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_customer',
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_rule_order',
                                        ctx=Load(),
                                    ),
                                    Name(id='t1_registrations', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='event_customer',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='users', ctx=Load()),
                            args=[Constant(value='user_sales_salesman', kind=None)],
                            keywords=[],
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
