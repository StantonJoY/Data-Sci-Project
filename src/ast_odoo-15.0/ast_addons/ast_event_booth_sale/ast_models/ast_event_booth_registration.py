Module(
    body=[
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
        ClassDef(
            name='EventBoothRegistration',
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
                    value=Constant(value='event.booth.registrations are used to allow multiple partners to book the same booth.\n    Whenever a partner has paid his registration all the others linked to the booth will be deleted.', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='event.booth.registration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Event Booth Registration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sale_order_line_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sale.order.line', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sale Order Line', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='event_booth_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.booth', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Booth', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='sale_order_line_id.order_partner_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Contact Name', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_contact_name', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_email', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Contact Email', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_contact_email', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_phone', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Contact Phone', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_contact_phone', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='contact_mobile', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Contact Mobile', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_contact_mobile', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='unique_registration', kind=None),
                                    Constant(value='unique(sale_order_line_id, event_booth_id)', kind=None),
                                    Constant(value='There can be only one registration for a booth by sale order line', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_contact_name',
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
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='registration', ctx=Load()),
                                            attr='contact_name',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='contact_name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='registration', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='partner_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_contact_email',
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
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='registration', ctx=Load()),
                                            attr='contact_email',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='contact_email',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='registration', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='partner_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_contact_phone',
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
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='registration', ctx=Load()),
                                            attr='contact_phone',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='contact_phone',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='registration', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='phone',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='partner_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_contact_mobile',
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
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='registration', ctx=Load()),
                                            attr='contact_mobile',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='contact_mobile',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='registration', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='mobile',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='partner_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_fields_for_booth_confirmation',
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
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='sale_order_line_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='contact_name', kind=None),
                                    Constant(value='contact_email', kind=None),
                                    Constant(value='contact_phone', kind=None),
                                    Constant(value='contact_mobile', kind=None),
                                ],
                                ctx=Load(),
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
                    name='action_confirm',
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
                            target=Name(id='registration', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=DictComp(
                                        key=Name(id='field', ctx=Load()),
                                        value=IfExp(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='registration', ctx=Load()),
                                                        slice=Name(id='field', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='models', ctx=Load()),
                                                        attr='BaseModel',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=Attribute(
                                                value=Subscript(
                                                    value=Name(id='registration', ctx=Load()),
                                                    slice=Name(id='field', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            orelse=Subscript(
                                                value=Name(id='registration', ctx=Load()),
                                                slice=Name(id='field', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_get_fields_for_booth_confirmation',
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
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='registration', ctx=Load()),
                                                attr='event_booth_id',
                                                ctx=Load(),
                                            ),
                                            attr='action_confirm',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
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
                                    attr='_cancel_pending_registrations',
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
                    name='_cancel_pending_registrations',
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
                            targets=[Name(id='body', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='<p>%(message)s: <ul>%(booth_names)s</ul></p>', kind=None),
                                op=Mod(),
                                right=Dict(
                                    keys=[
                                        Constant(value='message', kind=None),
                                        Constant(value='booth_names', kind=None),
                                    ],
                                    values=[
                                        Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Your order has been cancelled because the following booths have been reserved', kind=None)],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Constant(value='', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                GeneratorExp(
                                                    elt=BinOp(
                                                        left=Constant(value='<li>%s</li>', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='booth', ctx=Load()),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='booth', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='event_booth_id',
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
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='other_registrations', ctx=Store())],
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
                                                    Constant(value='event_booth_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='event_booth_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='not in', kind=None),
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
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Attribute(
                                value=Attribute(
                                    value=Name(id='other_registrations', ctx=Load()),
                                    attr='sale_order_line_id',
                                    ctx=Load(),
                                ),
                                attr='order_id',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Name(id='body', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='partner_ids',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='user_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='action_cancel',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                    value=Name(id='other_registrations', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
