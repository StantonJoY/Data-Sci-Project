Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Event',
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
                    value=Constant(value='event.event', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_order_lines_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='sale.order.line', kind=None),
                            Constant(value='event_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='groups',
                                value=Constant(value='sales_team.group_sale_salesman', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='All sale order lines pointing to this event', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_price_subtotal', ctx=Store())],
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
                                value=Constant(value='Sales (Tax Excluded)', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_sale_price_subtotal', kind=None),
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
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.currency', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Currency', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sale_price_subtotal',
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
                            value=Constant(value=" Takes all the sale.order.lines related to this event and converts amounts\n        from the currency of the sale order to the currency of the event company.\n\n        To avoid extra overhead, we use conversion rates as of 'today'.\n        Meaning we have a number that can change over time, but using the conversion rates\n        at the time of the related sale.order would mean thousands of extra requests as we would\n        have to do one conversion per sale.order (and a sale.order is created every time\n        we sell a single event ticket). ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='date_now', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_price_by_event', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='event_subtotals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sale.order.line', kind=None),
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
                                                            Constant(value='event_id', kind=None),
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
                                                            Constant(value='price_subtotal', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='event_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                    Constant(value='price_subtotal:sum', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='event_id', kind=None),
                                                    Constant(value='currency_id', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lazy',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company_by_event', ctx=Store())],
                                    value=DictComp(
                                        key=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='_origin',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        value=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='event', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='currency_by_event', ctx=Store())],
                                    value=DictComp(
                                        key=BoolOp(
                                            op=Or(),
                                            values=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='_origin',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        value=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='event', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='currency_by_id', ctx=Store())],
                                    value=DictComp(
                                        key=Attribute(
                                            value=Name(id='currency', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        value=Name(id='currency', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='currency', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.currency', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        ListComp(
                                                            elt=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='event_subtotal', ctx=Load()),
                                                                    slice=Constant(value='currency_id', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='event_subtotal', ctx=Store()),
                                                                    iter=Name(id='event_subtotals', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
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
                                For(
                                    target=Name(id='event_subtotal', ctx=Store()),
                                    iter=Name(id='event_subtotals', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='price_subtotal', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='event_subtotal', ctx=Load()),
                                                slice=Constant(value='price_subtotal', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='event_id', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='event_subtotal', ctx=Load()),
                                                    slice=Constant(value='event_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='currency_id', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='event_subtotal', ctx=Load()),
                                                    slice=Constant(value='currency_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sale_price', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='currency_by_event', ctx=Load()),
                                                        slice=Name(id='event_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_convert',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='price_subtotal', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='currency_by_id', ctx=Load()),
                                                        slice=Name(id='currency_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='company_by_event', ctx=Load()),
                                                        slice=Name(id='event_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='date_now', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='event_id', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='sale_price_by_event', ctx=Load())],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='sale_price_by_event', ctx=Load()),
                                                        slice=Name(id='event_id', ctx=Load()),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='sale_price', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='sale_price_by_event', ctx=Load()),
                                                            slice=Name(id='event_id', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='sale_price', ctx=Load()),
                                                    type_comment=None,
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
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='sale_price_subtotal',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sale_price_by_event', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='company_id.currency_id', kind=None),
                                Constant(value='sale_order_lines_ids.price_subtotal', kind=None),
                                Constant(value='sale_order_lines_ids.currency_id', kind=None),
                                Constant(value='sale_order_lines_ids.company_id', kind=None),
                                Constant(value='sale_order_lines_ids.order_id.date_order', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_linked_orders',
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
                            value=Constant(value=' Redirects to the orders linked to the current events ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sale_order_action', ctx=Store())],
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
                                args=[Constant(value='sale.action_orders', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sale_order_action', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='domain', kind=None),
                                            Constant(value='context', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value='cancel', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='order_line.event_id', kind=None),
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
                                            Dict(
                                                keys=[Constant(value='create', kind=None)],
                                                values=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='sale_order_action', ctx=Load()),
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
