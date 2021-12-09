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
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='CouponReward',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='coupon.reward', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Coupon Reward', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='reward_description', kind=None),
                    type_comment=None,
                ),
                Expr(
                    value=Constant(value='Rewards are not restricted to a company...\n    You could have a reward_product_id limited to a specific company A.\n    But still use this reward as reward of a program of company B...\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='reward_description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reward Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='discount', kind=None),
                                            Constant(value='Discount', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product', kind=None),
                                            Constant(value='Free Product', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Reward Type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='discount', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=BinOp(
                                    left=BinOp(
                                        left=Constant(value='Discount - Reward will be provided as discount.\n', kind=None),
                                        op=Add(),
                                        right=Constant(value='Free Product - Free product will be provide as reward \n', kind=None),
                                    ),
                                    op=Add(),
                                    right=Constant(value='Free Shipping - Free shipping will be provided as reward (Need delivery module)', kind=None),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Free Product', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Reward Product', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_product_quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Quantity', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Reward product quantity', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='percentage', kind=None),
                                            Constant(value='Percentage', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fixed_amount', kind=None),
                                            Constant(value='Fixed Amount', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='percentage', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=BinOp(
                                    left=Constant(value='Percentage - Entered percentage discount will be provided\n', kind=None),
                                    op=Add(),
                                    right=Constant(value='Amount - Entered fixed amount discount will be provided', kind=None),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_percentage', ctx=Store())],
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
                                value=Constant(value='Discount', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The discount in percentage, between 1 and 100', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_apply_on', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='on_order', kind=None),
                                            Constant(value='On Order', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cheapest_product', kind=None),
                                            Constant(value='On Cheapest Product', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='specific_products', kind=None),
                                            Constant(value='On Specific Products', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='on_order', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=BinOp(
                                    left=BinOp(
                                        left=Constant(value='On Order - Discount on whole order\n', kind=None),
                                        op=Add(),
                                        right=Constant(value='Cheapest product - Discount on cheapest product of the order\n', kind=None),
                                    ),
                                    op=Add(),
                                    right=Constant(value='Specific products - Discount on selected specific products', kind=None),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_specific_product_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Products', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Products that will be discounted if the discount is applied on specific products', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_max_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Maximum amount of discount that can be provided', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_fixed_amount', ctx=Store())],
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
                                value=Constant(value='Fixed Amount', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The discount in fixed amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_product_uom_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='reward_product_id.product_tmpl_id.uom_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='discount_line_product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Reward Line Product', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Product used in the sales order to apply the discount. Each coupon program has its own reward product for reporting purpose', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_discount_percentage',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='reward', annotation=None, type_comment=None)],
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
                                                        value=Name(id='reward', ctx=Load()),
                                                        attr='discount_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='percentage', kind=None)],
                                                ),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='reward', ctx=Load()),
                                                                attr='discount_percentage',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Lt()],
                                                            comparators=[Constant(value=0, kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='reward', ctx=Load()),
                                                                attr='discount_percentage',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Gt()],
                                                            comparators=[Constant(value=100, kind=None)],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Discount percentage should be between 1-100', kind=None)],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='discount_percentage', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='name_get',
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
                            value=Constant(value='\n        Returns a complete description of the reward\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='reward', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='reward_string', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='reward', ctx=Load()),
                                            attr='reward_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='reward_string', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Free Product - %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='reward', ctx=Load()),
                                                            attr='reward_product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='reward', ctx=Load()),
                                                    attr='reward_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='discount', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='reward', ctx=Load()),
                                                            attr='discount_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='percentage', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='reward_percentage', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='reward', ctx=Load()),
                                                                        attr='discount_percentage',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='reward', ctx=Load()),
                                                                    attr='discount_apply_on',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='on_order', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='reward_string', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='%s%% discount on total amount', kind=None),
                                                                            Name(id='reward_percentage', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='reward', ctx=Load()),
                                                                            attr='discount_apply_on',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='specific_products', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Call(
                                                                                    func=Name(id='len', ctx=Load()),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='reward', ctx=Load()),
                                                                                            attr='discount_specific_product_ids',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=1, kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='reward_string', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[
                                                                                            Constant(value='%s%% discount on products', kind=None),
                                                                                            Name(id='reward_percentage', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='reward_string', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[Constant(value='%(percentage)s%% discount on %(product_name)s', kind=None)],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='percentage',
                                                                                                value=Name(id='reward_percentage', ctx=Load()),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='product_name',
                                                                                                value=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='reward', ctx=Load()),
                                                                                                        attr='discount_specific_product_ids',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='name',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='reward', ctx=Load()),
                                                                                    attr='discount_apply_on',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='cheapest_product', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='reward_string', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='_', ctx=Load()),
                                                                                        args=[
                                                                                            Constant(value='%s%% discount on cheapest product', kind=None),
                                                                                            Name(id='reward_percentage', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
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
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='reward', ctx=Load()),
                                                                    attr='discount_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='fixed_amount', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='program', ctx=Store())],
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
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='reward_id', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Name(id='reward', ctx=Load()),
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
                                                                Assign(
                                                                    targets=[Name(id='reward_string', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='%(amount)s %(currency)s discount on total amount', kind=None)],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='amount',
                                                                                value=Attribute(
                                                                                    value=Name(id='reward', ctx=Load()),
                                                                                    attr='discount_fixed_amount',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='currency',
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='program', ctx=Load()),
                                                                                        attr='currency_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='name',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='reward', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='reward_string', ctx=Load()),
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
