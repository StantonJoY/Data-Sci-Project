Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ProductWishlist',
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
                    value=Constant(value='product.wishlist', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_notification', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_to_wishlist',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pricelist_id', annotation=None, type_comment=None),
                            arg(arg='currency_id', annotation=None, type_comment=None),
                            arg(arg='website_id', annotation=None, type_comment=None),
                            arg(arg='price', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='partner_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='wish', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_add_to_wishlist',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='pricelist_id',
                                        value=Name(id='pricelist_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='currency_id',
                                        value=Name(id='currency_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='website_id',
                                        value=Name(id='website_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='price',
                                        value=Name(id='price', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='product_id',
                                        value=Name(id='product_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='partner_id',
                                        value=Name(id='partner_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='wish', ctx=Load()),
                                    slice=Constant(value='stock_notification', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='wish', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='_is_sold_out',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='wish', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_send_availability_email',
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
                            targets=[Name(id='to_notify', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.wishlist', kind=None),
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
                                                    Constant(value='stock_notification', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='to_notify', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='notified', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.wishlist', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tmpl', ctx=Store())],
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
                                args=[Constant(value='website_sale_stock_wishlist.availability_email_body', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='wishlist', ctx=Store()),
                            iter=Name(id='to_notify', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='wishlist', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='website_id',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wishlist', ctx=Load()),
                                                            attr='website_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='_is_sold_out',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='body_html', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tmpl', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='wishlist', kind=None)],
                                                        values=[Name(id='wishlist', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
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
                                                                slice=Constant(value='mail.message', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Name(id='body_html', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='record_name',
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='full_mail', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mail.render.mixin', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_render_encapsulate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='mail.mail_notification_light', kind=None),
                                                    Name(id='body_html', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='add_context',
                                                        value=Call(
                                                            func=Name(id='dict', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='message',
                                                                    value=Name(id='msg', ctx=Load()),
                                                                ),
                                                                keyword(
                                                                    arg='model_description',
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Wishlist', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mail_values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='subject', kind=None),
                                                    Constant(value='email_from', kind=None),
                                                    Constant(value='email_to', kind=None),
                                                    Constant(value='body_html', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value="The product '%(product_name)s' is now available", kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Dict(
                                                            keys=[Constant(value='product_name', kind=None)],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='company_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='user',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='email_formatted',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wishlist', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='email_formatted',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='full_mail', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='mail', ctx=Store())],
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
                                                                slice=Constant(value='mail.mail', kind=None),
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
                                                args=[Name(id='mail_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='send',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='raise_exception',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='notified', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='wishlist', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='notified', ctx=Load()),
                                    attr='stock_notification',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
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
    ],
    type_ignores=[],
)
