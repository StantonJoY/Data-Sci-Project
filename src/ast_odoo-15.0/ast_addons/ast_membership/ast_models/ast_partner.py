Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='date', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='membership', asname=None)],
            level=1,
        ),
        ClassDef(
            name='Partner',
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
                    value=Constant(value='res.partner', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='associate_member', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Associate Member', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='A member with whom you want to associate your membership.It will consider the membership state of the associated member.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='member_lines', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='membership.membership_line', kind=None),
                            Constant(value='partner', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Membership', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='free_member', ctx=Store())],
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
                                value=Constant(value='Free Member', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Select if you want to give free membership.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='membership_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Membership Amount', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The price negotiated by the partner', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='membership_state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='membership', ctx=Load()),
                                attr='STATE',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_membership_state', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Current Membership Status', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='It indicates the membership state.\n-Non Member: A partner who has not applied for any membership.\n-Cancelled Member: A member who has cancelled his membership.\n-Old Member: A member whose membership date has expired.\n-Waiting Member: A member who has applied for the membership and whose invoice is going to be created.\n-Invoiced Member: A member whose invoice has been created.\n-Paying member: A member who has paid the membership fee.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='membership_start', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_membership_state', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Membership Start Date', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Date from which membership becomes active.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='membership_stop', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_membership_state', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Membership End Date', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Date until which membership remains active.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='membership_cancel', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_membership_state', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Cancel Membership Date', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Date on which membership has been cancelled', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_membership_state',
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
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='state', ctx=Store())],
                                    value=Constant(value='none', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='membership_start',
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
                                                    slice=Constant(value='membership.membership_line', kind=None),
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
                                                                Constant(value='partner', kind=None),
                                                                Constant(value='=', kind=None),
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='partner', ctx=Load()),
                                                                                attr='associate_member',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='partner', ctx=Load()),
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
                                                                Constant(value='date_cancel', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value=False, kind=None),
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
                                                keyword(
                                                    arg='order',
                                                    value=Constant(value='date_from', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='date_from',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='membership_stop',
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
                                                    slice=Constant(value='membership.membership_line', kind=None),
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
                                                                Constant(value='partner', kind=None),
                                                                Constant(value='=', kind=None),
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='partner', ctx=Load()),
                                                                                attr='associate_member',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='partner', ctx=Load()),
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
                                                                Constant(value='date_cancel', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value=False, kind=None),
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
                                                keyword(
                                                    arg='order',
                                                    value=Constant(value='date_to desc', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='date_to',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='membership_cancel',
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
                                                    slice=Constant(value='membership.membership_line', kind=None),
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
                                                                Constant(value='partner', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
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
                                                keyword(
                                                    arg='order',
                                                    value=Constant(value='date_cancel', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='date_cancel',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='membership_cancel',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id='today', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='membership_cancel',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='membership_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='free_member',
                                                    ctx=Load(),
                                                ),
                                                body=Constant(value='free', kind=None),
                                                orelse=Constant(value='canceled', kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='membership_stop',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id='today', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='membership_stop',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='free_member',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='membership_state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='free', kind=None),
                                                    type_comment=None,
                                                ),
                                                Continue(),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='associate_member',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='associate_member',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_membership_state',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='membership_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='associate_member',
                                                    ctx=Load(),
                                                ),
                                                attr='membership_state',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='line_states', ctx=Store())],
                                    value=ListComp(
                                        elt=Attribute(
                                            value=Name(id='mline', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='mline', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='member_lines',
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='mline', ctx=Load()),
                                                                            attr='date_to',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='date', ctx=Load()),
                                                                            attr='min',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[GtE()],
                                                                comparators=[Name(id='today', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='mline', ctx=Load()),
                                                                            attr='date_from',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='date', ctx=Load()),
                                                                            attr='min',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[LtE()],
                                                                comparators=[Name(id='today', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='mline', ctx=Load()),
                                                                            attr='account_invoice_line',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='partner', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='paid', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='line_states', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='state', ctx=Store())],
                                            value=Constant(value='paid', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='invoiced', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='line_states', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='state', ctx=Store())],
                                                    value=Constant(value='invoiced', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Constant(value='waiting', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='line_states', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='state', ctx=Store())],
                                                            value=Constant(value='waiting', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Constant(value='canceled', kind=None),
                                                                ops=[In()],
                                                                comparators=[Name(id='line_states', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='state', ctx=Store())],
                                                                    value=Constant(value='canceled', kind=None),
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
                                If(
                                    test=Compare(
                                        left=Name(id='state', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='none', kind=None)],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='mline', ctx=Store()),
                                            iter=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='member_lines',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='mline', ctx=Load()),
                                                                            attr='date_from',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='date', ctx=Load()),
                                                                            attr='min',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='today', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='mline', ctx=Load()),
                                                                            attr='date_to',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='date', ctx=Load()),
                                                                            attr='min',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='today', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='mline', ctx=Load()),
                                                                            attr='date_from',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='date', ctx=Load()),
                                                                            attr='min',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                ops=[LtE()],
                                                                comparators=[
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='mline', ctx=Load()),
                                                                                attr='date_to',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='date', ctx=Load()),
                                                                                attr='min',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='mline', ctx=Load()),
                                                                attr='account_invoice_id',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='mline', ctx=Load()),
                                                                        attr='account_invoice_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='payment_state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='in_payment', kind=None),
                                                                            Constant(value='paid', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='state', ctx=Store())],
                                                            value=Constant(value='old', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Break(),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='free_member',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id='state', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='paid', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='state', ctx=Store())],
                                            value=Constant(value='free', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='membership_state',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='state', ctx=Load()),
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
                            args=[
                                Constant(value='member_lines.account_invoice_line', kind=None),
                                Constant(value='member_lines.account_invoice_line.move_id.state', kind=None),
                                Constant(value='member_lines.account_invoice_line.move_id.payment_state', kind=None),
                                Constant(value='member_lines.account_invoice_line.move_id.partner_id', kind=None),
                                Constant(value='free_member', kind=None),
                                Constant(value='member_lines.date_to', kind=None),
                                Constant(value='member_lines.date_from', kind=None),
                                Constant(value='associate_member', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_recursion_associate_member',
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
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='level', ctx=Store())],
                                    value=Constant(value=100, kind=None),
                                    type_comment=None,
                                ),
                                While(
                                    test=Name(id='partner', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='partner', ctx=Load()),
                                                attr='associate_member',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='level', ctx=Load()),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='You cannot create recursive associated members.', kind=None)],
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
                                        AugAssign(
                                            target=Name(id='level', ctx=Store()),
                                            op=Sub(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
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
                            args=[Constant(value='associate_member', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_cron_update_membership',
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
                            targets=[Name(id='partners', ctx=Store())],
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
                                                    Constant(value='membership_state', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='invoiced', kind=None),
                                                            Constant(value='paid', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='add_to_compute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='membership_state', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='partners', ctx=Load()),
                                ],
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
                    name='create_membership_invoice',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='amount', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create Customer Invoice of Membership for partners.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='invoice_vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='addr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='address_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='invoice', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='free_member',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Partner is a free Member.', kind=None)],
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='addr', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='invoice', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value="Partner doesn't have an address to make the invoice.", kind=None)],
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
                                            value=Name(id='invoice_vals_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=None, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                            Constant(value='tax_ids', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='product', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=1, kind=None),
                                                                            Name(id='amount', ctx=Load()),
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value=6, kind=None),
                                                                                            Constant(value=0, kind=None),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='product', ctx=Load()),
                                                                                                    attr='taxes_id',
                                                                                                    ctx=Load(),
                                                                                                ),
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
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='invoice_vals_list', ctx=Load())],
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
