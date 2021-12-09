Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='reduce', asname=None)],
            level=0,
        ),
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
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ProductAttribute',
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
                    value=Constant(value='product.attribute', kind=None),
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
                            Constant(value=150, kind=None),
                            Constant(value=750, kind=None),
                        ],
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
                                                keys=[Constant(value='group_product_variant', kind=None)],
                                                values=[Constant(value=True, kind=None)],
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
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='PA_{counter}', kind=None)],
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
                                            Constant(value='create_variant', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='always', kind=None),
                                                            Constant(value='dynamic', kind=None),
                                                            Constant(value='no_variant', kind=None),
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
            name='ProductAttributeValue',
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
                    value=Constant(value='product.attribute.value', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='product.attribute', kind=None)],
                        ctx=Load(),
                    ),
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
                            Constant(value=100, kind=None),
                            Constant(value=1000, kind=None),
                            Constant(value=10000, kind=None),
                        ],
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
                            targets=[Name(id='attribute_ids', ctx=Store())],
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
                                slice=Constant(value='product.attribute', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='name', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='constant',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='PAV_{counter}', kind=None)],
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
                                            Constant(value='attribute_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attribute_ids', ctx=Load())],
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
            name='ProductTemplate',
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
                    value=Constant(value='product.template', kind=None),
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
                            Constant(value=150, kind=None),
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
                            Constant(value='product.attribute.value', kind=None),
                            Constant(value='product.category', kind=None),
                        ],
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
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
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='set_barcode_variant',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='sample_ratio', annotation=None, type_comment=None)],
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
                                        args=[Constant(value='barcode_product_template', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product_variants_ids', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='product_variant_ids',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product_variants_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='sample',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product_variants_ids', ctx=Load()),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='product_variants_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Mult(),
                                                        right=Name(id='sample_ratio', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product_variants', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product_variants_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Set barcode on product variants (%s)', kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='product_variants', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='product', ctx=Store()),
                                    iter=Name(id='product_variants', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='barcode',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='BARCODE-PT-%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
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
                        Expr(
                            value=Call(
                                func=Name(id='set_barcode_variant', ctx=Load()),
                                args=[Constant(value=0.85, kind=None)],
                                keywords=[],
                            ),
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
                            targets=[Name(id='attribute_ids', ctx=Store())],
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
                                slice=Constant(value='product.attribute', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attribute_ids_by_types', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attributes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='attribute_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attr', ctx=Store()),
                            iter=Name(id='attributes', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='attribute_ids_by_types', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='attr', ctx=Load()),
                                                    attr='create_variant',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='attr', ctx=Load()),
                                                attr='id',
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
                        FunctionDef(
                            name='get_attributes',
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
                                        ops=[Lt()],
                                        comparators=[Constant(value=0.2, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='attributes_qty', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='choices',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Constant(value=1, kind=None),
                                                        Constant(value=2, kind=None),
                                                        Constant(value=3, kind=None),
                                                        Constant(value=4, kind=None),
                                                        Constant(value=5, kind=None),
                                                        Constant(value=6, kind=None),
                                                        Constant(value=8, kind=None),
                                                        Constant(value=10, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Constant(value=10, kind=None),
                                                        Constant(value=9, kind=None),
                                                        Constant(value=8, kind=None),
                                                        Constant(value=7, kind=None),
                                                        Constant(value=6, kind=None),
                                                        Constant(value=4, kind=None),
                                                        Constant(value=1, kind=None),
                                                        Constant(value=0.5, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attr_line_vals', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attribute_used_ids', ctx=Store())],
                                    value=Name(id='attribute_ids', ctx=Load()),
                                    type_comment=None,
                                ),
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
                                        ops=[Lt()],
                                        comparators=[Constant(value=0.2, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attribute_used_ids', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='attribute_ids_by_types', ctx=Load()),
                                                slice=Constant(value='always', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='no_variant', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values_count', ctx=Store())],
                                    value=ListComp(
                                        elt=Constant(value=0, kind=None),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Name(id='attributes_qty', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='will_exceed',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='i', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Return(
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='no_variant', ctx=Load()),
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='reduce', ctx=Load()),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[
                                                                            arg(arg='x', annotation=None, type_comment=None),
                                                                            arg(arg='y', annotation=None, type_comment=None),
                                                                        ],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=BinOp(
                                                                        left=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Name(id='x', ctx=Load()),
                                                                                Constant(value=1, kind=None),
                                                                            ],
                                                                        ),
                                                                        op=Mult(),
                                                                        right=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Name(id='y', ctx=Load()),
                                                                                Constant(value=1, kind=None),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ),
                                                                BinOp(
                                                                    left=BinOp(
                                                                        left=Subscript(
                                                                            value=Name(id='values_count', ctx=Load()),
                                                                            slice=Slice(
                                                                                lower=Name(id='i', ctx=Load()),
                                                                                upper=None,
                                                                                step=None,
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=List(
                                                                            elts=[
                                                                                BinOp(
                                                                                    left=Subscript(
                                                                                        value=Name(id='values_count', ctx=Load()),
                                                                                        slice=Name(id='i', ctx=Load()),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    op=Add(),
                                                                                    right=Constant(value=1, kind=None),
                                                                                ),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Subscript(
                                                                        value=Name(id='values_count', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=None,
                                                                            upper=Name(id='i', ctx=Load()),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=1000, kind=None)],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Name(id='attributes_qty', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='will_exceed', ctx=Load()),
                                                args=[Name(id='i', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=Name(id='attr_line_vals', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='attr_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='random', ctx=Load()),
                                                    attr='choice',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attribute_used_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attr', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='product.attribute', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='attr_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='attr', ctx=Load()),
                                                    attr='create_variant',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='dynamic', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='no_variant', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='attr', ctx=Load()),
                                                    attr='value_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='nb_values', ctx=Store())],
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attr', ctx=Load()),
                                                        attr='value_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='vals_qty', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='random', ctx=Load()),
                                                        attr='randrange',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='nb_values', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='value_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='__', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[Name(id='vals_qty', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='will_exceed', ctx=Load()),
                                                        args=[Name(id='i', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='random_value_id', ctx=Store())],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='attr', ctx=Load()),
                                                                attr='value_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Call(
                                                                func=Attribute(
                                                                    value=Name(id='random', ctx=Load()),
                                                                    attr='randrange',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='nb_values', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='random_value_id', ctx=Load()),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='value_ids', ctx=Load())],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Subscript(
                                                                value=Name(id='values_count', ctx=Load()),
                                                                slice=Name(id='i', ctx=Load()),
                                                                ctx=Store(),
                                                            ),
                                                            op=Add(),
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='value_ids', ctx=Load()),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='random_value_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='attr_line_vals', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='attribute_id', kind=None),
                                                                    Constant(value='value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='attr_id', ctx=Load()),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    Call(
                                                                                        func=Name(id='list', ctx=Load()),
                                                                                        args=[Name(id='value_ids', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
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
                                    value=Name(id='attr_line_vals', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='name', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='populate', ctx=Load()),
                                                        attr='constant',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='product_template_name_{counter}', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='description', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='populate', ctx=Load()),
                                                        attr='constant',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='product_template_description_{counter}', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='default_code', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='populate', ctx=Load()),
                                                        attr='constant',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='PT-{counter}', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='attribute_line_ids', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='populate', ctx=Load()),
                                                        attr='compute',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='get_attributes', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
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
                                        attr='_populate_get_product_factories',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
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
            name='ProductTemplateAttributeExclusion',
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
                    value=Constant(value='product.template.attribute.exclusion', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='product.template', kind=None)],
                        ctx=Load(),
                    ),
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
                            Constant(value=200, kind=None),
                            Constant(value=1000, kind=None),
                            Constant(value=5000, kind=None),
                        ],
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
                            targets=[Name(id='configurable_templates', ctx=Store())],
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
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='p_tmpl_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='has_configurable_attributes', kind=None),
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
                        Assign(
                            targets=[Name(id='tmpl_ids_possible', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='multi_values_attribute_lines_by_tmpl', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='template', ctx=Store()),
                            iter=Name(id='configurable_templates', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='multi_values_attribute_lines', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='attribute_line_ids',
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
                                                    left=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='l', ctx=Load()),
                                                                attr='value_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[Gt()],
                                                    comparators=[Constant(value=1, kind=None)],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='multi_values_attribute_lines', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tmpl_ids_possible', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='multi_values_attribute_lines_by_tmpl', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='multi_values_attribute_lines', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_product_template_attribute_value_id',
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
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='choice',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='multi_values_attribute_lines_by_tmpl', ctx=Load()),
                                                        slice=Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='product_tmpl_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_template_value_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
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
                            name='get_value_ids',
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
                                Assign(
                                    targets=[Name(id='attr_val', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='product.template.attribute.value', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='product_template_attribute_value_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='attribute_line_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='remaining_lines', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Name(id='multi_values_attribute_lines_by_tmpl', ctx=Load()),
                                            slice=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Constant(value='product_tmpl_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='attr_val', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=6, kind=None),
                                                    Constant(value=0, kind=None),
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='random', ctx=Load()),
                                                                        attr='choice',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='remaining_lines', ctx=Load()),
                                                                            attr='product_template_value_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
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
                                        ctx=Load(),
                                    ),
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
                                            Constant(value='product_tmpl_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='randomize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tmpl_ids_possible', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_template_attribute_value_id', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_product_template_attribute_value_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='value_ids', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='populate', ctx=Load()),
                                                    attr='compute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='get_value_ids', ctx=Load())],
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
            name='ProductTemplateAttributeValue',
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
                    value=Constant(value='product.template.attribute.value', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_populate_dependencies', ctx=Store())],
                    value=List(
                        elts=[Constant(value='product.template', kind=None)],
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
                            targets=[Name(id='ptavs', ctx=Store())],
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
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Name(id='p_tmpl_ids', ctx=Load()),
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
                            targets=[Name(id='rand', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='populate', ctx=Load()),
                                    attr='Random',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ptav_extra_price_generator', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ptav', ctx=Store()),
                            iter=Name(id='ptavs', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='rand', ctx=Load()),
                                                attr='random',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0.5, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='ptav', ctx=Load()),
                                                    attr='price_extra',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='rand', ctx=Load()),
                                                        attr='randrange',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=500, kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mult(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='rand', ctx=Load()),
                                                        attr='random',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
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
                        Return(
                            value=Name(id='ptavs', ctx=Load()),
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
