Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ProductPricelistReport',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.product.report_pricelist', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Pricelist Report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Constant(value='pdf', kind=None),
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
                    name='get_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='render_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Constant(value='html', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='product.report_pricelist_page', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='render_values', ctx=Load())],
                                keywords=[],
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
                    name='_get_report_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='report_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='html', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='quantities', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='quantities', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value=1, kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pricelist_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='pricelist_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='pricelist_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pricelist', ctx=Store())],
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
                                                slice=Constant(value='product.pricelist', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pricelist_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='pricelist', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pricelist', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='active_model', ctx=Store())],
                            value=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='active_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='active_ids', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='active_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_product_tmpl', ctx=Store())],
                            value=Compare(
                                left=Name(id='active_model', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='product.template', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ProductClass', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Name(id='active_model', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products', ctx=Store())],
                            value=IfExp(
                                test=Name(id='active_ids', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='ProductClass', ctx=Load()),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='active_ids', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Attribute(
                                        value=Name(id='ProductClass', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='sale_ok', kind=None),
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
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products_data', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_product_data',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='is_product_tmpl', ctx=Load()),
                                        Name(id='product', ctx=Load()),
                                        Name(id='pricelist', ctx=Load()),
                                        Name(id='quantities', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='product', ctx=Store()),
                                        iter=Name(id='products', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='is_html_type', kind=None),
                                    Constant(value='is_product_tmpl', kind=None),
                                    Constant(value='is_visible_title', kind=None),
                                    Constant(value='pricelist', kind=None),
                                    Constant(value='products', kind=None),
                                    Constant(value='quantities', kind=None),
                                ],
                                values=[
                                    Compare(
                                        left=Name(id='report_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='html', kind=None)],
                                    ),
                                    Name(id='is_product_tmpl', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='bool', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='is_visible_title', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Name(id='pricelist', ctx=Load()),
                                    Name(id='products_data', ctx=Load()),
                                    Name(id='quantities', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_product_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='is_product_tmpl', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='pricelist', annotation=None, type_comment=None),
                            arg(arg='quantities', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='price', kind=None),
                                    Constant(value='uom', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='product', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='is_product_tmpl', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='dict', ctx=Load()),
                                            attr='fromkeys',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='quantities', ctx=Load()),
                                            Constant(value=0.0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='qty', ctx=Store()),
                            iter=Name(id='quantities', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='price', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='qty', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='pricelist', ctx=Load()),
                                            attr='get_product_price',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product', ctx=Load()),
                                            Name(id='qty', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='is_product_tmpl', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='product_variant_count',
                                            ctx=Load(),
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='variants', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_product_data',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value=False, kind=None),
                                                Name(id='variant', ctx=Load()),
                                                Name(id='pricelist', ctx=Load()),
                                                Name(id='quantities', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='variant', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='product_variant_ids',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='data', ctx=Load()),
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
