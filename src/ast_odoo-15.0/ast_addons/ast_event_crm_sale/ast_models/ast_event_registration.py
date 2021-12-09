Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='EventRegistration',
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
                    value=Constant(value='event.registration', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_lead_grouping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rules', annotation=None, type_comment=None),
                            arg(arg='rule_to_new_regs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override to support sale-order based grouping and update.\n\n        When checking for groups for rules, we search for existing leads linked\n        to same group (based on sale_order_id) and rule. Each rule can therefore\n        update an existing lead or create a new one, for each sale order that\n        makes the group. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='so_registrations', ctx=Store())],
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
                                            args=[arg(arg='reg', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='reg', ctx=Load()),
                                            attr='sale_order_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouping_res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='EventRegistration', ctx=Load()),
                                            BinOp(
                                                left=Name(id='self', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='so_registrations', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_lead_grouping',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rules', ctx=Load()),
                                    Name(id='rule_to_new_regs', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='so_registrations', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='related_registrations', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='sale_order_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='so_registrations', ctx=Load()),
                                                                    attr='sale_order_id',
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='related_leads', ctx=Store())],
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
                                                            Constant(value='event_lead_rule_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='rules', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='registration_ids', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='related_registrations', ctx=Load()),
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
                                For(
                                    target=Name(id='rule', ctx=Store()),
                                    iter=Name(id='rules', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='rule_new_regs', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='rule_to_new_regs', ctx=Load()),
                                                slice=Name(id='rule', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='so_to_regs', ctx=Store())],
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
                                            target=Name(id='registration', ctx=Store()),
                                            iter=BinOp(
                                                left=Name(id='rule_new_regs', ctx=Load()),
                                                op=BitAnd(),
                                                right=Name(id='so_registrations', ctx=Load()),
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='so_to_regs', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='registration', ctx=Load()),
                                                            attr='sale_order_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Store(),
                                                    ),
                                                    op=BitOr(),
                                                    value=Name(id='registration', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='so_res', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='sale_order', ctx=Store()),
                                                    Name(id='registrations', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='so_to_regs', ctx=Load()),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
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
                                                    targets=[Name(id='leads', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='related_leads', ctx=Load()),
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
                                                                body=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='lead', ctx=Load()),
                                                                                attr='event_lead_rule_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='rule', ctx=Load())],
                                                                        ),
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='lead', ctx=Load()),
                                                                                    attr='registration_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='sale_order_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='sale_order', ctx=Load())],
                                                                        ),
                                                                    ],
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
                                                            value=Name(id='so_res', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='leads', ctx=Load()),
                                                                    Name(id='sale_order', ctx=Load()),
                                                                    Name(id='registrations', ctx=Load()),
                                                                ],
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
                                            test=Name(id='so_res', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='grouping_res', ctx=Load()),
                                                            slice=Name(id='rule', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='grouping_res', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='rule', ctx=Load()),
                                                                Call(
                                                                    func=Name(id='list', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='so_res', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='grouping_res', ctx=Load()),
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
