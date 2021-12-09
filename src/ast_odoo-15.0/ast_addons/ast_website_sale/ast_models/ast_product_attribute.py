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
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
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
                    targets=[Name(id='visibility', ctx=Store())],
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
                                            Constant(value='visible', kind=None),
                                            Constant(value='Visible', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='hidden', kind=None),
                                            Constant(value='Hidden', kind=None),
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
                                value=Constant(value='visible', kind=None),
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
                    name='_prepare_single_value_for_display',
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
                            value=Constant(value='On the product page group together the attribute lines that concern\n        the same attribute and that have only one value each.\n\n        Indeed those are considered informative values, they do not generate\n        choice for the user, so they are displayed below the configurator.\n\n        The returned attributes are ordered as they appear in `self`, so based\n        on the order of the attribute lines.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='single_value_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='ptal', annotation=None, type_comment=None)],
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
                                                        value=Name(id='ptal', ctx=Load()),
                                                        attr='value_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value=1, kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='single_value_attributes', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Name(id='pa', ctx=Load()),
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
                                                target=Name(id='pa', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='single_value_lines', ctx=Load()),
                                                    attr='attribute_id',
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
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ptal', ctx=Store()),
                            iter=Name(id='single_value_lines', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='single_value_attributes', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='ptal', ctx=Load()),
                                            attr='attribute_id',
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
                            value=Name(id='single_value_attributes', ctx=Load()),
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
