Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='TransactionCase', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.tests.common',
            names=[alias(name='HttpCaseWithUserPortal', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestWebsiteSaleCartRecovery',
            bases=[Name(id='HttpCaseWithUserPortal', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_shop_cart_recovery_tour',
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
                            value=Constant(value='The goal of this test is to make sure cart recovery works.', kind=None),
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
                                            Constant(value='list_price', kind=None),
                                            Constant(value='website_published', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Acoustic Bloc Screens', kind=None),
                                            Constant(value=2950.0, kind=None),
                                            Constant(value=True, kind=None),
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
                                    attr='start_tour',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/', kind=None),
                                    Constant(value='shop_cart_recovery', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='portal', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestWebsiteSaleCartRecoveryServer',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestWebsiteSaleCartRecoveryServer', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer',
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
                                        ],
                                        values=[
                                            Constant(value='a', kind=None),
                                            Constant(value='a@example.com', kind=None),
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
                                    attr='recovery_template_default',
                                    ctx=Store(),
                                ),
                            ],
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
                                args=[Constant(value='website_sale.mail_template_sale_cart_recovery', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='recovery_template_custom1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='recovery_template_default',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='recovery_template_custom2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='recovery_template_default',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='website0',
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
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='cart_recovery_mail_template_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='web0', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='recovery_template_default',
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
                                    attr='website1',
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
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='cart_recovery_mail_template_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='web1', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='recovery_template_custom1',
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
                                    attr='website2',
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
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='cart_recovery_mail_template_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='web2', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='recovery_template_custom2',
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
                                    attr='so0',
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
                                            Constant(value='website_id', kind=None),
                                            Constant(value='is_abandoned_cart', kind=None),
                                            Constant(value='cart_recovery_email_sent', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website0',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
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
                                    attr='so1',
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
                                            Constant(value='website_id', kind=None),
                                            Constant(value='is_abandoned_cart', kind=None),
                                            Constant(value='cart_recovery_email_sent', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
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
                                    attr='so2',
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
                                            Constant(value='website_id', kind=None),
                                            Constant(value='is_abandoned_cart', kind=None),
                                            Constant(value='cart_recovery_email_sent', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='website2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cart_recovery_mail_template',
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
                            value=Constant(value='Make sure that we get the correct cart recovery templates to send.', kind=None),
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='so1',
                                                ctx=Load(),
                                            ),
                                            attr='_get_cart_recovery_template',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='recovery_template_custom1',
                                        ctx=Load(),
                                    ),
                                    Constant(value='We do not return the correct mail template', kind=None),
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='so2',
                                                ctx=Load(),
                                            ),
                                            attr='_get_cart_recovery_template',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='recovery_template_custom2',
                                        ctx=Load(),
                                    ),
                                    Constant(value='We do not return the correct mail template', kind=None),
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
                                        func=Attribute(
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='so1',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='so2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            attr='_get_cart_recovery_template',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='recovery_template_default',
                                        ctx=Load(),
                                    ),
                                    Constant(value='We do not return the correct mail template', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cart_recovery_mail_template_send',
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
                            value=Constant(value='The goal of this test is to make sure cart recovery works.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='orders', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so0',
                                        ctx=Load(),
                                    ),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='so1',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='so2',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='orders', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='cart_recovery_email_sent', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='The recovery mail should not have been sent yet.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='orders', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='access_token', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='There should not be an access token yet.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='orders', ctx=Load()),
                                    attr='_cart_recovery_email_send',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='orders', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='cart_recovery_email_sent', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='The recovery mail should have been sent.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='orders', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='access_token', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='All tokens should have been generated.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sent_mail', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='orders', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='mail', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='record_name', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Subscript(
                                                                value=Name(id='order', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
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
                                            value=Name(id='sent_mail', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Name(id='order', ctx=Load())],
                                                values=[Name(id='mail', ctx=Load())],
                                            ),
                                        ],
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='sent_mail', ctx=Load()),
                                                                slice=Name(id='order', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value=1, kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order', ctx=Store()),
                                                        iter=Name(id='orders', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Each cart recovery mail has been sent exactly once.', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='all', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='access_token',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='sent_mail', ctx=Load()),
                                                                slice=Name(id='order', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            attr='body',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='order', ctx=Store()),
                                                        iter=Name(id='orders', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Each mail should contain the access token of the corresponding SO.', kind=None),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
