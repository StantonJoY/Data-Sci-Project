Module(
    body=[
        ImportFrom(
            module='odoo.addons.point_of_sale.tests.test_frontend',
            names=[alias(name='TestPointOfSaleHttpCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='Form', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestUi',
            bases=[Name(id='TestPointOfSaleHttpCommon', ctx=Load())],
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
                                        args=[],
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
                                    attr='promo_programs',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='coupon.program', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code_promo_program',
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
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='program_type', kind=None),
                                            Constant(value='promo_code_usage', kind=None),
                                            Constant(value='promo_code', kind=None),
                                            Constant(value='discount_apply_on', kind=None),
                                            Constant(value='discount_percentage', kind=None),
                                            Constant(value='discount_specific_product_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Promo Code Program - Discount on Specific Products', kind=None),
                                            Constant(value='promotion_program', kind=None),
                                            Constant(value='code_needed', kind=None),
                                            Constant(value='promocode', kind=None),
                                            Constant(value='specific_products', kind=None),
                                            Constant(value=50, kind=None),
                                            Attribute(
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='whiteboard_pen',
                                                            ctx=Load(),
                                                        ),
                                                        op=BitOr(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='magnetic_board',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='desk_organizer',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='promo_programs',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='code_promo_program',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='auto_promo_program_current',
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
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='program_type', kind=None),
                                            Constant(value='promo_code_usage', kind=None),
                                            Constant(value='discount_apply_on', kind=None),
                                            Constant(value='discount_percentage', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Auto Promo Program - Cheapest Product', kind=None),
                                            Constant(value='promotion_program', kind=None),
                                            Constant(value='no_code_needed', kind=None),
                                            Constant(value='cheapest_product', kind=None),
                                            Constant(value=90, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='promo_programs',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='auto_promo_program_current',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='auto_promo_program_next',
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
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='program_type', kind=None),
                                            Constant(value='promo_code_usage', kind=None),
                                            Constant(value='promo_applicability', kind=None),
                                            Constant(value='discount_apply_on', kind=None),
                                            Constant(value='discount_percentage', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Auto Promo Program - Global Discount', kind=None),
                                            Constant(value='promotion_program', kind=None),
                                            Constant(value='no_code_needed', kind=None),
                                            Constant(value='on_next_order', kind=None),
                                            Constant(value='on_order', kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='promo_programs',
                                ctx=Store(),
                            ),
                            op=BitOr(),
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='auto_promo_program_next',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='coupon_program',
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
                                        slice=Constant(value='coupon.program', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='program_type', kind=None),
                                            Constant(value='rule_products_domain', kind=None),
                                            Constant(value='reward_type', kind=None),
                                            Constant(value='rule_min_quantity', kind=None),
                                            Constant(value='reward_product_id', kind=None),
                                            Constant(value='reward_product_quantity', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Coupon Program - Buy 3 Take 2 Free Product', kind=None),
                                            Constant(value='coupon_program', kind=None),
                                            Constant(value="[('name', 'ilike', 'Desk Organizer')]", kind=None),
                                            Constant(value='product', kind=None),
                                            Constant(value=3, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='desk_organizer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='coupon.generate.wizard', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='active_id', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='coupon_program',
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
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='nbr_coupons', kind=None)],
                                                values=[Constant(value=4, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='generate_coupon',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon1',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon2',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon3',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon4',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='coupon_program',
                                    ctx=Load(),
                                ),
                                attr='coupon_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='coupon1',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='1234', kind=None)],
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
                                        attr='coupon2',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='5678', kind=None)],
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
                                        attr='coupon3',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='1357', kind=None)],
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
                                        attr='coupon4',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='2468', kind=None)],
                                    ),
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
                    name='test_pos_coupon_tour_basic',
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
                            value=Constant(value='PoS Coupon Basic Tour', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='main_pos_config',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='pos_config', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='pos_config', ctx=Load()),
                                            attr='tax_regime_selection',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='pos_config', ctx=Load()),
                                            attr='use_pricelist',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='pos_config', ctx=Load()),
                                            attr='pricelist_id',
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
                                                slice=Constant(value='product.pricelist', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='PoS Default Pricelist', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='pos_config', ctx=Load()),
                                            attr='use_coupon_programs',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='pos_config', ctx=Load()),
                                                attr='coupon_program_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='coupon_program',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='promo_program', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='promo_programs',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='pos_config', ctx=Load()),
                                                        attr='promo_program_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='promo_program', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='main_pos_config',
                                        ctx=Load(),
                                    ),
                                    attr='open_session_cb',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='check_coa',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                    BinOp(
                                        left=Constant(value='/pos/web?config_id=%d', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='main_pos_config',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='PosCouponTour1', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='accountman', kind=None),
                                    ),
                                ],
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
                                            attr='coupon1',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='used', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='`1234` coupon should have been used.', kind=None),
                                    ),
                                ],
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
                                            attr='coupon2',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='`5678` coupon code is used but was eventually freed.', kind=None),
                                    ),
                                ],
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
                                            attr='auto_promo_program_current',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
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
                                            attr='auto_promo_program_next',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
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
                                            attr='code_promo_program',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
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
                                            attr='coupon_program',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='auto_promo_program_next',
                                                    ctx=Load(),
                                                ),
                                                attr='coupon_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pos_session', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='main_pos_config',
                                    ctx=Load(),
                                ),
                                attr='current_session_id',
                                ctx=Load(),
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
                                        args=[
                                            Attribute(
                                                value=Name(id='pos_session', ctx=Load()),
                                                attr='order_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=5, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg',
                                        value=Constant(value='5 orders were made in tour part1.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='promo_coupon1', ctx=Store()),
                                        Name(id='promo_coupon2', ctx=Store()),
                                        Name(id='promo_coupon3', ctx=Store()),
                                        Name(id='promo_coupon4', ctx=Store()),
                                        Starred(
                                            value=Name(id='_', ctx=Store()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='auto_promo_program_next',
                                    ctx=Load(),
                                ),
                                attr='coupon_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='promo_coupon1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='123456', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='promo_coupon2', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='345678', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='promo_coupon3', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='567890', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='promo_coupon4', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='code', kind=None)],
                                        values=[Constant(value='098765', kind=None)],
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
                                    BinOp(
                                        left=Constant(value='/pos/web?config_id=%d', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='main_pos_config',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='PosCouponTour2', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='accountman', kind=None),
                                    ),
                                ],
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
                                            attr='coupon4',
                                            ctx=Load(),
                                        ),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
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
                                        value=Name(id='promo_coupon4', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
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
                                            attr='auto_promo_program_current',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=5, kind=None),
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
                                            attr='auto_promo_program_next',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='code_promo_program',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='coupon_program',
                                            ctx=Load(),
                                        ),
                                        attr='pos_order_count',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
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
