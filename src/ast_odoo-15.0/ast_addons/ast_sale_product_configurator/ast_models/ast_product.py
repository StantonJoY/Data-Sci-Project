Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
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
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='optional_product_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='product.template', kind=None),
                            Constant(value='product_optional_rel', kind=None),
                            Constant(value='src_id', kind=None),
                            Constant(value='dest_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Optional Products', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Optional Products are suggested whenever the customer hits *Add to Cart* (cross-sell strategy, e.g. for computers: warranty, software, etc.).', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_has_configurable_attributes',
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
                            value=Constant(value=' A product is considered configurable if:\n        - It has dynamic attributes\n        - It has any attribute line with at least 2 attribute values configured\n        - It has at least one custom attribute value ', kind=None),
                        ),
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='has_configurable_attributes',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Attribute(
                                                                value=Name(id='attribute', ctx=Load()),
                                                                attr='create_variant',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='dynamic', kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='attribute', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='mapped',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='attribute_line_ids.attribute_id', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='attribute_line_id', ctx=Load()),
                                                                        attr='value_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[GtE()],
                                                            comparators=[Constant(value=2, kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='attribute_line_id', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='attribute_line_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Attribute(
                                                            value=Name(id='attribute_value', ctx=Load()),
                                                            attr='is_custom',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='attribute_value', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='product', ctx=Load()),
                                                                        attr='mapped',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='attribute_line_ids.value_ids', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                            args=[
                                Constant(value='attribute_line_ids.value_ids.is_custom', kind=None),
                                Constant(value='attribute_line_ids.attribute_id.create_variant', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_single_product_variant',
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
                            value=Constant(value=' Method used by the product configurator to check if the product is configurable or not.\n\n        We need to open the product configurator if the product:\n        - is configurable (see has_configurable_attributes)\n        - has optional products ', kind=None),
                        ),
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProductTemplate', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_single_product_variant',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_id', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='has_optional_products', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='optional_product', ctx=Store()),
                                    iter=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_variant_id',
                                            ctx=Load(),
                                        ),
                                        attr='optional_product_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='optional_product', ctx=Load()),
                                                            attr='has_dynamic_attributes',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='optional_product', ctx=Load()),
                                                            attr='_get_possible_variants',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_variant_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='product_template_attribute_value_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='has_optional_products', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Break(),
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
                                            value=Name(id='res', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='has_optional_products', kind=None)],
                                                values=[Name(id='has_optional_products', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
