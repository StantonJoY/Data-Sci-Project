Module(
    body=[
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        ClassDef(
            name='TestWebsiteSequence',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
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
                                        args=[
                                            Name(id='TestWebsiteSequence', ctx=Load()),
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
                        ),
                        Assign(
                            targets=[Name(id='ProductTemplate', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.template', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_templates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductTemplate', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='orderpoint_ids', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='product_templates', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='product_variant_ids.orderpoint_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='active', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='loyalty.rule', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rules', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='loyalty.rule', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rules', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='loyalty.reward', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rewards', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='loyalty.reward', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rewards', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='product_templates', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p1',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p2',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p3',
                                            ctx=Store(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p4',
                                            ctx=Store(),
                                        ),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductTemplate', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='website_sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='First Product', kind=None),
                                                    Constant(value=100, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='website_sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Second Product', kind=None),
                                                    Constant(value=180, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='website_sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Third Product', kind=None),
                                                    Constant(value=225, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='website_sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Last Product', kind=None),
                                                    Constant(value=250, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_correct_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p1',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p2',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='p3',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p4',
                                            ctx=Load(),
                                        ),
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
                    name='_search_website_sequence_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='ASC', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Helper method to limit the search only to the setUp products', kind=None),
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
                                        slice=Constant(value='product.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=BinOp(
                                            left=Constant(value='website_sequence %s', kind=None),
                                            op=Mod(),
                                            right=Name(id='order', ctx=Load()),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_correct_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='products', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='product_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_search_website_sequence_order',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='ids',
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
                                    Name(id='product_ids', ctx=Load()),
                                    Attribute(
                                        value=Name(id='products', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Wrong sequence order', kind=None),
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
                    name='test_01_website_sequence',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='p2',
                                        ctx=Load(),
                                    ),
                                    attr='set_sequence_down',
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
                                    attr='_check_correct_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p1',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='p2',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p4',
                                            ctx=Load(),
                                        ),
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
                                        attr='p4',
                                        ctx=Load(),
                                    ),
                                    attr='set_sequence_up',
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
                                    attr='_check_correct_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p1',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='p4',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p2',
                                            ctx=Load(),
                                        ),
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
                                        attr='p2',
                                        ctx=Load(),
                                    ),
                                    attr='set_sequence_top',
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
                                    attr='_check_correct_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p2',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p1',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='p3',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p4',
                                            ctx=Load(),
                                        ),
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
                                        attr='p1',
                                        ctx=Load(),
                                    ),
                                    attr='set_sequence_bottom',
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
                                    attr='_check_correct_order',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p2',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='p3',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='p4',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p1',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='current_sequences', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_website_sequence_order',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_sequence', kind=None)],
                                keywords=[],
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
                                    Name(id='current_sequences', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value=95, kind=None),
                                            Constant(value=180, kind=None),
                                            Constant(value=225, kind=None),
                                            Constant(value=230, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Wrong sequence order (2)', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='p2',
                                        ctx=Load(),
                                    ),
                                    attr='website_sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='p3',
                                        ctx=Load(),
                                    ),
                                    attr='set_sequence_top',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='p3',
                                            ctx=Load(),
                                        ),
                                        attr='website_sequence',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=4, kind=None),
                                    ),
                                    Constant(value='`website_sequence` should go below 0', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Last Newly Created Product', kind=None)],
                                    ),
                                ],
                                keywords=[],
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
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_search_website_sequence_order',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='new_product', ctx=Load()),
                                    Constant(value='new product should be last', kind=None),
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
                    func=Attribute(
                        value=Attribute(
                            value=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='tests',
                                ctx=Load(),
                            ),
                            attr='common',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
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
