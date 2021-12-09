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
            name='GiftCard',
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
                    value=Constant(value='gift.card', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='buy_line_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sale.order.line', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sale Order line where this gift card has been bought.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='redeem_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='sale.order.line', kind=None),
                            Constant(value='gift_card_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Redeems', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_balance',
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_balance',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='confirmed_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='redeem_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='l', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='sale', kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='balance', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='balance',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='confirmed_line', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='balance', ctx=Store()),
                                            op=Sub(),
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='confirmed_line', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='line', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BinOp(
                                                                    left=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='_convert',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='price_unit',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                attr='currency_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='record', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='company',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='create_date',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    op=Mult(),
                                                                    right=UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=1, kind=None),
                                                                    ),
                                                                ),
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
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='balance',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='balance', ctx=Load()),
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
                            args=[Constant(value='redeem_line_ids', kind=None)],
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
