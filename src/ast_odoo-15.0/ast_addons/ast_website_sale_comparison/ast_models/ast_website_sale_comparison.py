Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ProductAttributeCategory',
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
                    value=Constant(value='product.attribute.category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Product Attribute Category', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Category Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='attribute_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='product.attribute', kind=None),
                            Constant(value='category_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Related Attributes', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('category_id', '=', False)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
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
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='category_id, sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='category_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.attribute.category', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Category', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Set a category to regroup similar attributes under the same section in the Comparison page of eCommerce', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ProductTemplateAttributeLine',
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
                    value=Constant(value='product.template.attribute.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_categories_for_display',
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
                            value=Constant(value='On the product page group together the attribute lines that concern\n        attributes that are in the same category.\n\n        The returned categories are ordered following their default order.\n\n        :return: OrderedDict [{\n            product.attribute.category: [product.template.attribute.line]\n        }]\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attributes', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='attribute_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='categories', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='cat', ctx=Load()),
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='product.template.attribute.line', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='cat', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='attributes', ctx=Load()),
                                                            attr='category_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sorted',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
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
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='pa', ctx=Load()),
                                                attr='category_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='pa', ctx=Store()),
                                                iter=Name(id='attributes', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='categories', ctx=Load()),
                                            slice=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.attribute.category', kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='ptal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='categories', ctx=Load()),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='ptal', ctx=Load()),
                                                attr='attribute_id',
                                                ctx=Load(),
                                            ),
                                            attr='category_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Name(id='ptal', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='categories', ctx=Load()),
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
            name='ProductProduct',
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
                    value=Constant(value='product.product', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_categories_for_display',
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
                            value=Constant(value='On the comparison page group on the same line the values of each\n        product that concern the same attributes, and then group those\n        attributes per category.\n\n        The returned categories are ordered following their default order.\n\n        :return: OrderedDict [{\n            product.attribute.category: OrderedDict [{\n                product.attribute: OrderedDict [{\n                    product: [product.template.attribute.value]\n                }]\n            }]\n        }]\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='attributes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_tmpl_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='valid_product_template_attribute_line_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='_without_no_variant_attributes',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='attribute_id',
                                        ctx=Load(),
                                    ),
                                    attr='sorted',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='categories', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='cat', ctx=Load()),
                                                Call(
                                                    func=Name(id='OrderedDict', ctx=Load()),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='cat', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='attributes', ctx=Load()),
                                                            attr='category_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sorted',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
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
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Name(id='pa', ctx=Load()),
                                                attr='category_id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='pa', ctx=Store()),
                                                iter=Name(id='attributes', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='categories', ctx=Load()),
                                            slice=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.attribute.category', kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='OrderedDict', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='pa', ctx=Store()),
                            iter=Name(id='attributes', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='categories', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='pa', ctx=Load()),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='pa', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='OrderedDict', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='product', ctx=Load()),
                                                        Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='product_template_attribute_value_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='filtered',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Lambda(
                                                                    args=arguments(
                                                                        posonlyargs=[],
                                                                        args=[arg(arg='ptav', annotation=None, type_comment=None)],
                                                                        vararg=None,
                                                                        kwonlyargs=[],
                                                                        kw_defaults=[],
                                                                        kwarg=None,
                                                                        defaults=[],
                                                                    ),
                                                                    body=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='ptav', ctx=Load()),
                                                                            attr='attribute_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='pa', ctx=Load())],
                                                                    ),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='product', ctx=Store()),
                                                        iter=Name(id='self', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='categories', ctx=Load()),
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
