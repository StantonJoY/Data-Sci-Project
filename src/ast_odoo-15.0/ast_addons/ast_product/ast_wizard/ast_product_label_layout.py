Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ProductLabelLayout',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='product.label.layout', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Choose the sheet layout to print the labels', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='print_format', ctx=Store())],
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
                                            Constant(value='dymo', kind=None),
                                            Constant(value='Dymo', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='2x7xprice', kind=None),
                                            Constant(value='2 x 7 with price', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='4x7xprice', kind=None),
                                            Constant(value='4 x 7 with price', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='4x12', kind=None),
                                            Constant(value='4 x 12', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='4x12xprice', kind=None),
                                            Constant(value='4 x 12 with price', kind=None),
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
                                value=Constant(value='Format', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='2x7xprice', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='custom_quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_tmpl_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.template', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='extra_html', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Extra Content', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rows', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_dimensions', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='columns', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_dimensions', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_dimensions',
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
                        For(
                            target=Name(id='wizard', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='x', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='wizard', ctx=Load()),
                                                attr='print_format',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='columns', ctx=Store()),
                                                        Name(id='rows', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='print_format',
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='x', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=2, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='columns',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='columns', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='wizard', ctx=Load()),
                                                    attr='rows',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='rows', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='columns',
                                                            ctx=Store(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='wizard', ctx=Load()),
                                                            attr='rows',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
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
                            args=[Constant(value='print_format', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_report_data',
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='custom_quantity',
                                    ctx=Load(),
                                ),
                                ops=[LtE()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You need to set a positive quantity.', kind=None)],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='print_format',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='dymo', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='xml_id', ctx=Store())],
                                    value=Constant(value='product.report_product_template_label_dymo', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='x', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='print_format',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='xml_id', ctx=Store())],
                                            value=Constant(value='product.report_product_template_label', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='xml_id', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='active_model', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_tmpl_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='products', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_tmpl_ids',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='active_model', ctx=Store())],
                                    value=Constant(value='product.template', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='products', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='active_model', ctx=Store())],
                                            value=Constant(value='product.product', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='picking_quantity', kind=None),
                                    Constant(value='active_model', kind=None),
                                    Constant(value='quantity_by_product', kind=None),
                                    Constant(value='layout_wizard', kind=None),
                                    Constant(value='price_included', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_quantity',
                                        ctx=Load(),
                                    ),
                                    Name(id='active_model', ctx=Load()),
                                    DictComp(
                                        key=Name(id='p', ctx=Load()),
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='custom_quantity',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='p', ctx=Store()),
                                                iter=Name(id='products', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Constant(value='xprice', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='print_format',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='xml_id', ctx=Load()),
                                    Name(id='data', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
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
                                        Name(id='xml_id', ctx=Store()),
                                        Name(id='data', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_report_data',
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
                                operand=Name(id='xml_id', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Unable to find report template for %s format', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='print_format',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                        args=[Name(id='xml_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='report_action',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=None, kind=None)],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Name(id='data', ctx=Load()),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
