Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='populate', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='timedelta', asname=None),
                alias(name='date', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Pricelist',
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
                    value=Constant(value='product.pricelist', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=20, kind=None),
                            Constant(value=100, kind=None),
                            Constant(value=1500, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='res.company', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='size', annotation=None, type_comment=None),
                        ],
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
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.config.settings', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='group_product_pricelist', kind=None),
                                                    Constant(value='group_sale_pricelist', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_populate',
                                    ctx=Load(),
                                ),
                                args=[Name(id='size', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.company', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='iterate',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='company_ids', ctx=Load()),
                                                        op=Add(),
                                                        right=ListComp(
                                                            elt=Constant(value=False, kind=None),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='i', ctx=Store()),
                                                                    iter=Call(
                                                                        func=Name(id='range', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[Name(id='company_ids', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='product_pricelist_{counter}', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='currency_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Call(
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
                                                                attr='search',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='active', kind=None),
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
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sequence', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=List(
                                                            elts=[Constant(value=False, kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=ListComp(
                                                            elt=Name(id='i', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='i', ctx=Store()),
                                                                    iter=Call(
                                                                        func=Name(id='range', ctx=Load()),
                                                                        args=[
                                                                            Constant(value=1, kind=None),
                                                                            Constant(value=101, kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='discount_policy', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='with_discount', kind=None),
                                                            Constant(value='without_discount', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='active', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=0.8, kind=None),
                                                            Constant(value=0.2, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
        ClassDef(
            name='PricelistItem',
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
                    value=Constant(value='product.pricelist.item', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_sizes', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='small', kind=None),
                            Constant(value='medium', kind=None),
                            Constant(value='large', kind=None),
                        ],
                        values=[
                            Constant(value=500, kind=None),
                            Constant(value=5000, kind=None),
                            Constant(value=50000, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='product.product', kind=None),
                            Constant(value='product.template', kind=None),
                            Constant(value='product.pricelist', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_populate_factories',
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
                            targets=[Name(id='pricelist_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.pricelist', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='p_tmpl_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.template', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='categ_ids', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='populated_models',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.category', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_target_info',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='iterator', annotation=None, type_comment=None),
                                    arg(arg='field_name', annotation=None, type_comment=None),
                                    arg(arg='model_name', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='random', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='populate', ctx=Load()),
                                            attr='Random',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='pricelist_target', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='values', ctx=Store()),
                                    iter=Name(id='iterator', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='applied_on', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='applied_on', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='applied_on', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='0_product_variant', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='product_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='random', ctx=Load()),
                                                            attr='choice',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='product_ids', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='applied_on', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='1_product', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='product_tmpl_id', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='choice',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='p_tmpl_ids', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='applied_on', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='2_product_category', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Constant(value='categ_id', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='random', ctx=Load()),
                                                                            attr='choice',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='categ_ids', ctx=Load())],
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
                                        Expr(
                                            value=Yield(
                                                value=Name(id='values', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_prices',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='iterator', annotation=None, type_comment=None),
                                    arg(arg='field_name', annotation=None, type_comment=None),
                                    arg(arg='model_name', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='random', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='populate', ctx=Load()),
                                            attr='Random',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='pricelist_prices', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='values', ctx=Store()),
                                    iter=Name(id='iterator', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='compute_price', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='compute_price', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='compute_price', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='fixed', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='fixed_price', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='random', ctx=Load()),
                                                            attr='randint',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value=1000, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='compute_price', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='percentage', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='percent_price', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=100, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='base', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='choice',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='list_price', kind=None),
                                                                            Constant(value='standard_price', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='price_discount', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=100, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Yield(
                                                value=Name(id='values', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='now', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='date', ctx=Load()),
                                    attr='today',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_date_start',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='values', annotation=None, type_comment=None),
                                    arg(arg='counter', annotation=None, type_comment=None),
                                    arg(arg='random', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='random',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0.5, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Name(id='now', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Constant(value=20, kind=None),
                                                                    ),
                                                                    Constant(value=20, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_date_end',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='values', annotation=None, type_comment=None),
                                    arg(arg='counter', annotation=None, type_comment=None),
                                    arg(arg='random', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='date_start', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='date_start', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randint',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value=100, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='pricelist_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='pricelist_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='applied_on', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='3_global', kind=None),
                                                            Constant(value='2_product_category', kind=None),
                                                            Constant(value='1_product', kind=None),
                                                            Constant(value='0_product_variant', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='compute_price', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='fixed', kind=None),
                                                            Constant(value='percentage', kind=None),
                                                            Constant(value='formula', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value=5, kind=None),
                                                            Constant(value=3, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='_price', kind=None),
                                            Name(id='get_prices', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='_target', kind=None),
                                            Name(id='get_target_info', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='min_quantity', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randint',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=50, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_start', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_date_start', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date_end', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_date_end', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
