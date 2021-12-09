Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[
                alias(name='HttpCaseWithUserDemo', asname=None),
                alias(name='HttpCaseWithUserPortal', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.event_crm.tests.common',
            names=[alias(name='TestEventCrmCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.sales_team.tests.common',
            names=[alias(name='TestSalesCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.tests.test_website_visitor',
            names=[alias(name='MockVisitor', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_event.tests.common',
            names=[alias(name='EventDtPatcher', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestEventFullCommon',
            bases=[
                Name(id='TestEventCrmCommon', ctx=Load()),
                Name(id='TestSalesCommon', ctx=Load()),
                Name(id='EventDtPatcher', ctx=Load()),
                Name(id='MockVisitor', ctx=Load()),
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
                                            Name(id='TestEventFullCommon', ctx=Load()),
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
                                    attr='event_product',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='description_sale', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='detailed_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Registration Product', kind=None),
                                            Constant(value='Mighty Description', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=30.0, kind=None),
                                            Constant(value='event', kind=None),
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
                                    attr='website',
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
                                        slice=Constant(value='website', kind=None),
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
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
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
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='event_0',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date_begin', kind=None),
                                            Constant(value='date_end', kind=None),
                                            Constant(value='event_ticket_ids', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='combine',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='reference_now',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Name(id='time', ctx=Load()),
                                                            args=[
                                                                Constant(value=7, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='combine',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='reference_now',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Name(id='time', ctx=Load()),
                                                            args=[
                                                                Constant(value=13, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='seats_max', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='First Ticket', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='event_product',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=30, kind=None),
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
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Second Ticket', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='event_product',
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
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='customer_so',
                                    ctx=Store(),
                                ),
                            ],
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
                                                slice=Constant(value='sale.order', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='user_sales_salesman',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='event_question_1',
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
                                        slice=Constant(value='event.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='once_per_order', kind=None),
                                            Constant(value='answer_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Question1', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Q1-Answer1', kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Q1-Answer2', kind=None)],
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='event_question_2',
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
                                        slice=Constant(value='event.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='once_per_order', kind=None),
                                            Constant(value='answer_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Question2', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Q2-Answer1', kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Q2-Answer2', kind=None)],
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='event_question_3',
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
                                        slice=Constant(value='event.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='once_per_order', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Question3', kind=None),
                                            Constant(value='text_box', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='event_0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
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
                                    attr='website_customer_data',
                                    ctx=Store(),
                                ),
                            ],
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='name', kind=None),
                                        Constant(value='partner_id', kind=None),
                                        Constant(value='email', kind=None),
                                        Constant(value='phone', kind=None),
                                        Constant(value='registration_answer_ids', kind=None),
                                    ],
                                    values=[
                                        BinOp(
                                            left=Constant(value='My Customer %02d', kind=None),
                                            op=Mod(),
                                            right=Name(id='x', ctx=Load()),
                                        ),
                                        Attribute(
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
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='question_id', kind=None),
                                                                Constant(value='value_answer_id', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='event_question_1',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='event_question_1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='answer_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=BinOp(
                                                                            left=Name(id='x', ctx=Load()),
                                                                            op=Mod(),
                                                                            right=Constant(value=2, kind=None),
                                                                        ),
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
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='question_id', kind=None),
                                                                Constant(value='value_answer_id', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='event_question_2',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='event_question_2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='answer_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=BinOp(
                                                                            left=Name(id='x', ctx=Load()),
                                                                            op=Mod(),
                                                                            right=Constant(value=2, kind=None),
                                                                        ),
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
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='question_id', kind=None),
                                                                Constant(value='value_text_box', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='event_question_3',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                BinOp(
                                                                    left=Constant(value='CustomerAnswer%s', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='x', ctx=Load()),
                                                                ),
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
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Constant(value=0, kind=None),
                                                Constant(value=4, kind=None),
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestEventFullCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='assertLeadConvertion',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rule', ctx=Load()),
                                    Name(id='registrations', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='partner',
                                        value=Name(id='partner', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='expected', ctx=Load()),
                                    ),
                                ],
                            ),
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
                        For(
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='registrations', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='registration', ctx=Load()),
                                            attr='registration_answer_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='answer', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='registration', ctx=Load()),
                                        attr='registration_answer_ids',
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
                                                            value=Name(id='answer', ctx=Load()),
                                                            attr='question_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='title',
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
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='answer', ctx=Load()),
                                                    attr='question_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='simple_choice', kind=None)],
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
                                                                    value=Name(id='answer', ctx=Load()),
                                                                    attr='value_answer_id',
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
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertIn',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='answer', ctx=Load()),
                                                                attr='value_text_box',
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
                                        ),
                                    ],
                                    orelse=[],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestWEventCommon',
            bases=[
                Name(id='HttpCaseWithUserDemo', ctx=Load()),
                Name(id='HttpCaseWithUserPortal', ctx=Load()),
                Name(id='EventDtPatcher', ctx=Load()),
                Name(id='MockVisitor', ctx=Load()),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                            Name(id='TestWEventCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_product',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='default_code', kind=None),
                                            Constant(value='description_sale', kind=None),
                                            Constant(value='list_price', kind=None),
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='detailed_type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test Event Registration', kind=None),
                                            Constant(value='EVENT_REG', kind=None),
                                            Constant(value='Mighty Description', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=30.0, kind=None),
                                            Constant(value='event', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_tag_category_1',
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
                                        slice=Constant(value='event.tag.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Type', kind=None),
                                            Constant(value=2, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_tag_category_1_tag_1',
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
                                        slice=Constant(value='event.tag', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                            Constant(value='category_id', kind=None),
                                            Constant(value='color', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Online', kind=None),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_tag_category_1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=8, kind=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='event.event', kind=None),
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
                                                            Constant(value='name', kind=None),
                                                            Constant(value='like', kind=None),
                                                            Constant(value='%Online Reveal%', kind=None),
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Do not click on me', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='event',
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
                                        slice=Constant(value='event.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='auto_confirm', kind=None),
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='address_id', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='tag_ids', kind=None),
                                            Constant(value='date_tz', kind=None),
                                            Constant(value='date_begin', kind=None),
                                            Constant(value='date_end', kind=None),
                                            Constant(value='event_ticket_ids', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='website_menu', kind=None),
                                            Constant(value='website_track', kind=None),
                                            Constant(value='website_track_proposal', kind=None),
                                            Constant(value='exhibitor_menu', kind=None),
                                            Constant(value='community_menu', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Online Reveal TestEvent', kind=None),
                                            Constant(value=True, kind=None),
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
                                                    args=[Constant(value='event.event_stage_booked', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_demo',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='event_tag_category_1_tag_1',
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
                                            Constant(value='Europe/Brussels', kind=None),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='combine',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='reference_now',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Name(id='time', ctx=Load()),
                                                            args=[
                                                                Constant(value=5, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='datetime', ctx=Load()),
                                                        attr='combine',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='reference_now',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Name(id='time', ctx=Load()),
                                                            args=[
                                                                Constant(value=15, kind=None),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='price', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Standard', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='event_product',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=0, kind=None),
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
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='seats_max', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='VIP', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='event_product',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=10, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_customer',
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
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='country_id', kind=None),
                                            Constant(value='phone', kind=None),
                                            Constant(value='mobile', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Constantin Customer', kind=None),
                                            Constant(value='constantin@test.example.com', kind=None),
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
                                                    args=[Constant(value='base.be', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='0485112233', kind=None),
                                            Constant(value=False, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_speaker',
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
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Brandon Freeman', kind=None),
                                            Constant(value='brandon.freeman55@example.com', kind=None),
                                            Constant(value='(355)-687-3262', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_question_1',
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
                                        slice=Constant(value='event.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='once_per_order', kind=None),
                                            Constant(value='answer_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Which field are you working in', kind=None),
                                            Constant(value='simple_choice', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Consumers', kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Sales', kind=None)],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='name', kind=None)],
                                                                values=[Constant(value='Research', kind=None)],
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='event_question_2',
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
                                        slice=Constant(value='event.question', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='question_type', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='once_per_order', kind=None),
                                        ],
                                        values=[
                                            Constant(value='How did you hear about us ?', kind=None),
                                            Constant(value='text_box', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='track_0',
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
                                        slice=Constant(value='event.track', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='duration', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='wishlisted_by_default', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='What This Event Is All About', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='website_event_track.event_track_stage3', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='reference_now',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='hours',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Constant(value=2, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_admin',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_speaker',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='track_1',
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
                                        slice=Constant(value='event.track', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='duration', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Live Testimonial', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='website_event_track.event_track_stage3', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='reference_now',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='minutes',
                                                            value=Constant(value=30, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Constant(value=0.75, kind=None),
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_admin',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_speaker',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='track_2',
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
                                        slice=Constant(value='event.track', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='stage_id', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='duration', kind=None),
                                            Constant(value='is_published', kind=None),
                                            Constant(value='user_id', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Our Last Day Together !', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='website_event_track.event_track_stage3', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='reference_now',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            Constant(value=0.75, kind=None),
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_admin',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event_speaker',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.meeting.room', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='summary', kind=None),
                                            Constant(value='target_audience', kind=None),
                                            Constant(value='is_pinned', kind=None),
                                            Constant(value='website_published', kind=None),
                                            Constant(value='event_id', kind=None),
                                            Constant(value='room_lang_id', kind=None),
                                            Constant(value='room_max_capacity', kind=None),
                                            Constant(value='room_participant_count', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Best wood for furniture', kind=None),
                                            Constant(value="Let's talk about wood types for furniture", kind=None),
                                            Constant(value='wood expert(s)', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='event',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
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
                                                    args=[Constant(value='base.lang_en', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='12', kind=None),
                                            Constant(value=9, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='event',
                                        ctx=Load(),
                                    ),
                                    attr='flush',
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
