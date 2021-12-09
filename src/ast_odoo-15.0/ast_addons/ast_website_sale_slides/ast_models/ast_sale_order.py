Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SaleOrder',
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
                    value=Constant(value='sale.order', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_action_confirm',
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
                            value=Constant(value=" If the product of an order line is a 'course', we add the client of the sale_order\n        as a member of the channel(s) on which this product is configured (see slide.channel.product_id). ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SaleOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='so_lines', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='order_id', kind=None),
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
                            targets=[Name(id='products', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='so_lines', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='related_channels', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='slide.channel', kind=None),
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
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='products', ctx=Load()),
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
                            targets=[Name(id='channel_products', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='related_channels', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='channels_per_so', ctx=Store())],
                            value=DictComp(
                                key=Name(id='sale_order', ctx=Load()),
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='slide.channel', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='sale_order', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='so_line', ctx=Store()),
                            iter=Name(id='so_lines', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='so_line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='channel_products', ctx=Load())],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='related_channel', ctx=Store()),
                                            iter=Name(id='related_channels', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='related_channel', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='so_line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='channels_per_so', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='so_line', ctx=Load()),
                                                                        attr='order_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='channels_per_so', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='so_line', ctx=Load()),
                                                                        attr='order_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                op=BitOr(),
                                                                right=Name(id='related_channel', ctx=Load()),
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='sale_order', ctx=Store()),
                                    Name(id='channels', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='channels_per_so', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='channels', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_action_add_members',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='sale_order', ctx=Load()),
                                                attr='partner_id',
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
                        Return(
                            value=Name(id='result', ctx=Load()),
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
