Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='tagged', asname=None),
                alias(name='common', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestMatrixCommon',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='HttpCase',
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
                                            Name(id='TestMatrixCommon', ctx=Load()),
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
                            targets=[Name(id='product_attributes', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='create_variant', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='PA1', kind=None),
                                                    Constant(value='always', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='create_variant', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='PA2', kind=None),
                                                    Constant(value='always', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='create_variant', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='PA3', kind=None),
                                                    Constant(value='dynamic', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='create_variant', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='PA4', kind=None),
                                                    Constant(value='no_variant', kind=None),
                                                    Constant(value=4, kind=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='attribute_id', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=BinOp(
                                                        left=Constant(value='PAV', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='product_attribute', ctx=Load()),
                                                                    attr='sequence',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='i', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='product_attribute', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[
                                                        Constant(value=1, kind=None),
                                                        Constant(value=3, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                            comprehension(
                                                target=Name(id='product_attribute', ctx=Store()),
                                                iter=Name(id='product_attributes', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='matrix_template',
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
                                        slice=Constant(value='product.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                            Constant(value='attribute_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Matrix', kind=None),
                                            Constant(value='consu', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                                keywords=[],
                                            ),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='attribute_id', kind=None),
                                                                Constant(value='value_ids', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='attribute', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                List(
                                                                    elts=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value=6, kind=None),
                                                                                Constant(value=0, kind=None),
                                                                                Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='attribute', ctx=Load()),
                                                                                        attr='value_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='ids',
                                                                                    ctx=Load(),
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
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='attribute', ctx=Store()),
                                                        iter=Name(id='product_attributes', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_ptav',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='pav_name', annotation=None, type_comment=None)],
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
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.template.attribute.value', kind=None),
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
                                                            Constant(value='product_attribute_value_id.name', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='pav_name', ctx=Load()),
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
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Name(id='get_ptav', ctx=Load()),
                                        args=[Constant(value='PAV12', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=50, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Name(id='get_ptav', ctx=Load()),
                                        args=[Constant(value='PAV31', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=25, kind=None),
                            ),
                            type_comment=None,
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
