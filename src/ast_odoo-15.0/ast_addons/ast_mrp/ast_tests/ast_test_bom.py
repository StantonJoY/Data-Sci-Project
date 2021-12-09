Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='exceptions', asname=None),
                alias(name='Command', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='Form', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.mrp.tests.common',
            names=[alias(name='TestMrpCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_round', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestBoM',
            bases=[Name(id='TestMrpCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_01_explode',
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='bom_1',
                                        ctx=Load(),
                                    ),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_4',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='bom', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='bom', ctx=Store()),
                                                        iter=Name(id='boms', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bom_1',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='line', ctx=Store()),
                                                        iter=Name(id='lines', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bom_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='bom_line_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='bom_3',
                                        ctx=Load(),
                                    ),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_6',
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='bom', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='bom', ctx=Store()),
                                                        iter=Name(id='boms', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bom_2',
                                                        ctx=Load(),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bom_3',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='line', ctx=Store()),
                                                        iter=Name(id='lines', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='bom_2',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=BitOr(),
                                                                    right=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='bom_3',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='bom_line_ids', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='filtered',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='line', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='child_bom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='child_bom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[Constant(value='phantom', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
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
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_10_variants',
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
                            targets=[Name(id='test_bom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='operation_ids', kind=None),
                                            Constant(value='byproduct_ids', kind=None),
                                            Constant(value='bom_line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_7_template',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uom_unit',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4.0, kind=None),
                                            Constant(value='normal', kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='workcenter_id', kind=None),
                                                                    Constant(value='time_cycle', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Cutting Machine', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='workcenter_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='workcenter_id', kind=None),
                                                                    Constant(value='time_cycle', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Weld Machine', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='workcenter_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=18, kind=None),
                                                                    Constant(value=2, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_7_attr1_v1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='workcenter_id', kind=None),
                                                                    Constant(value='time_cycle', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Taking a coffee', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='workcenter_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=5, kind=None),
                                                                    Constant(value=3, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_7_attr1_v2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_1',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='uom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_2',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='uom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_7_attr1_v1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_3',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_3',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='uom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_7_attr1_v2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_3',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_7_attr1_v1',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Command', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_4',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Command', ctx=Load()),
                                                                                    attr='link',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='product_7_attr1_v2',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='test_bom_l1', ctx=Store()),
                                        Name(id='test_bom_l2', ctx=Store()),
                                        Name(id='test_bom_l3', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='test_bom', ctx=Load()),
                                attr='bom_line_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_3',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='b', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='b', ctx=Store()),
                                                iter=Name(id='boms', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l1', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l2', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l3', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
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
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_1',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='b', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='b', ctx=Store()),
                                                iter=Name(id='boms', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l1', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l2', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l3', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
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
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_2',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='b', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='b', ctx=Store()),
                                                iter=Name(id='boms', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l1', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l2', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='test_bom_l3', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='l', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='l', ctx=Store()),
                                                iter=Name(id='lines', ctx=Load()),
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
                            targets=[Name(id='mrp_order_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.production', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_3',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mrp_order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='mrp_order', ctx=Load()),
                                        attr='bom_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='test_bom', ctx=Load()),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mrp_order', ctx=Load()),
                                                attr='workorder_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
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
                                            value=Name(id='mrp_order', ctx=Load()),
                                            attr='workorder_ids',
                                            ctx=Load(),
                                        ),
                                        attr='operation_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='test_bom', ctx=Load()),
                                            attr='operation_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mrp_order', ctx=Load()),
                                                attr='move_byproduct_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
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
                                            value=Name(id='mrp_order', ctx=Load()),
                                            attr='move_byproduct_ids',
                                            ctx=Load(),
                                        ),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mrp_order_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.production', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_1',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_1',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='bom_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='mrp.bom', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='bom_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='test_bom', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mrp_order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='mrp_order', ctx=Load()),
                                        attr='bom_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='test_bom', ctx=Load()),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mrp_order', ctx=Load()),
                                                attr='workorder_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
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
                                            value=Name(id='mrp_order', ctx=Load()),
                                            attr='workorder_ids',
                                            ctx=Load(),
                                        ),
                                        attr='operation_id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='test_bom', ctx=Load()),
                                            attr='operation_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=2, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mrp_order', ctx=Load()),
                                                attr='move_byproduct_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
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
                                            value=Name(id='mrp_order', ctx=Load()),
                                            attr='move_byproduct_ids',
                                            ctx=Load(),
                                        ),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_1',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_2',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mrp_order_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.production', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_2',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mrp_order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mrp_order_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
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
                                    Attribute(
                                        value=Name(id='mrp_order', ctx=Load()),
                                        attr='bom_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='test_bom', ctx=Load()),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mrp_order', ctx=Load()),
                                                attr='workorder_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
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
                                            value=Name(id='mrp_order', ctx=Load()),
                                            attr='workorder_ids',
                                            ctx=Load(),
                                        ),
                                        attr='operation_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='test_bom', ctx=Load()),
                                                attr='operation_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='test_bom', ctx=Load()),
                                                attr='operation_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='mrp_order', ctx=Load()),
                                                attr='move_byproduct_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
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
                                            value=Name(id='mrp_order', ctx=Load()),
                                            attr='move_byproduct_ids',
                                            ctx=Load(),
                                        ),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_1',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_3',
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
                    name='test_11_multi_level_variants',
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
                            targets=[Name(id='tmp_picking_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='code', kind=None),
                                            Constant(value='sequence_code', kind=None),
                                            Constant(value='sequence_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Manufacturing', kind=None),
                                            Constant(value='mrp_operation', kind=None),
                                            Constant(value='TMP', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.sequence', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Dict(
                                                            keys=[
                                                                Constant(value='code', kind=None),
                                                                Constant(value='name', kind=None),
                                                            ],
                                                            values=[
                                                                Constant(value='mrp.production', kind=None),
                                                                Constant(value='tmp_production_sequence', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_5',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_5',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                            Constant(value='phantom', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='operation_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='workcenter_id', kind=None),
                                                                    Constant(value='time_cycle', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Gift Wrap Maching', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='workcenter_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=15, kind=None),
                                                                    Constant(value=1, kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_bom_1_l1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_7_3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_7_template',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uom_unit',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4.0, kind=None),
                                            Constant(value='normal', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_2', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='operation_ids', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='workcenter_id', kind=None),
                                                                    Constant(value='time_cycle', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Cutting Machine', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='workcenter_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=12, kind=None),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='workcenter_id', kind=None),
                                                                    Constant(value='time_cycle', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Weld Machine', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='workcenter_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=18, kind=None),
                                                                    Constant(value=2, kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_bom_2_l1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_2_l2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_5',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_7_attr1_v1',
                                                                    ctx=Load(),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_2_l3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_5',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_7_attr1_v2',
                                                                    ctx=Load(),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_2_l4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_4',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_2', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_1',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=Name(id='test_bom_2', ctx=Load()),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bom_2',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='b', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='b', ctx=Store()),
                                                        iter=Name(id='boms', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='test_bom_2_l1', ctx=Load()),
                                                        op=BitOr(),
                                                        right=Name(id='test_bom_2_l4', ctx=Load()),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='bom_2',
                                                            ctx=Load(),
                                                        ),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='l', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='l', ctx=Store()),
                                                        iter=Name(id='lines', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='sequence', kind=None)],
                                        values=[Constant(value=1, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_2', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_1',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=Name(id='test_bom_2', ctx=Load()),
                                                    op=BitOr(),
                                                    right=Name(id='test_bom_1', ctx=Load()),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='b', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='b', ctx=Store()),
                                                        iter=Name(id='boms', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='test_bom_2_l1', ctx=Load()),
                                                        op=BitOr(),
                                                        right=Name(id='test_bom_2_l4', ctx=Load()),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='test_bom_1', ctx=Load()),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='l', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='l', ctx=Store()),
                                                        iter=Name(id='lines', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='picking_type_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse_1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='manu_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                        attr='bom_2',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='picking_type_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='tmp_picking_type', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_2', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='picking_type_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='tmp_picking_type', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='boms', ctx=Store()),
                                        Name(id='lines', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='test_bom_2', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_1',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=Name(id='test_bom_2', ctx=Load()),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bom_2',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='b', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='b', ctx=Store()),
                                                        iter=Name(id='boms', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='test_bom_2_l1', ctx=Load()),
                                                        op=BitOr(),
                                                        right=Name(id='test_bom_2_l4', ctx=Load()),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='bom_2',
                                                            ctx=Load(),
                                                        ),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='l', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='l', ctx=Store()),
                                                        iter=Name(id='lines', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='test_bom_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='consumption', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_9',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_9',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_9',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                            Constant(value='flexible', kind=None),
                                            Constant(value='normal', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='consumption', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_10',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_10',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_10',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                            Constant(value='flexible', kind=None),
                                            Constant(value='phantom', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_3_l1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_3', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_10',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='test_bom_4_l1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bom_id', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='test_bom_4', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_9',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='UserError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='test_bom_3', ctx=Load()),
                                            attr='explode',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_9',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_12_multi_level_variants2',
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
                            value=Constant(value='Test skip bom line with same attribute values in bom lines.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Product', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.product', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ProductAttribute', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.attribute', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ProductAttributeValue', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.attribute.value', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_color', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductAttribute', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Color', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_size', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductAttribute', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='size', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_color_red', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductAttributeValue', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='red', kind=None),
                                            Attribute(
                                                value=Name(id='att_color', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_color_blue', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductAttributeValue', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='blue', kind=None),
                                            Attribute(
                                                value=Name(id='att_color', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_size_big', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductAttributeValue', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='big', kind=None),
                                            Attribute(
                                                value=Name(id='att_size', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='att_size_medium', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ProductAttributeValue', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='medium', kind=None),
                                            Attribute(
                                                value=Name(id='att_size', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_template', ctx=Store())],
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
                                            Constant(value='attribute_line_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Sofa', kind=None),
                                            List(
                                                elts=[
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
                                                                    Attribute(
                                                                        value=Name(id='att_color', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Name(id='att_color_red', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='att_color_blue', ctx=Load()),
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
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
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
                                                                    Attribute(
                                                                        value=Name(id='att_size', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Name(id='att_size_big', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='att_size_medium', ctx=Load()),
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
                                                                ],
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sofa_red', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='attribute_line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sofa_blue', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='attribute_line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sofa_big', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='attribute_line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sofa_medium', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='attribute_line_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_A', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Product', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Wood', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_B', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Product', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Clothes', kind=None)],
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
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='bom_line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='product_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                            Constant(value='normal', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='product_A', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=4, kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='sofa_red', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=4, kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='sofa_blue', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=4, kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='sofa_big', ctx=Load()),
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
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='bom_product_template_attribute_value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='product_B', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=4, kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='sofa_red', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=4, kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='sofa_blue', ctx=Load()),
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='dict_consumed_products', ctx=Store())],
                            value=Dict(
                                keys=[
                                    BinOp(
                                        left=Name(id='sofa_red', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='sofa_big', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='sofa_red', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='sofa_medium', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='sofa_blue', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='sofa_big', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=Name(id='sofa_blue', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='sofa_medium', ctx=Load()),
                                    ),
                                ],
                                values=[
                                    BinOp(
                                        left=Name(id='product_A', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='product_B', ctx=Load()),
                                    ),
                                    Name(id='product_B', ctx=Load()),
                                    BinOp(
                                        left=Name(id='product_A', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='product_B', ctx=Load()),
                                    ),
                                    Name(id='product_B', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='combination', ctx=Store()),
                                    Name(id='consumed_products', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='dict_consumed_products', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='product_template', ctx=Load()),
                                                attr='product_variant_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='p', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='product_template_attribute_value_ids',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='combination', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mrp_order_form', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mrp.production', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='mrp_order_form', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='product', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mrp_order', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mrp_order_form', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='mrp_order', ctx=Load()),
                                                    attr='move_raw_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='consumed_products', ctx=Load()),
                                        ],
                                        keywords=[],
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
                    name='test_13_bom_kit_qty',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='bom_line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_7_3',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_7_template',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uom_unit',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=4.0, kind=None),
                                            Constant(value='phantom', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_3',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=2, kind=None),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='location', ctx=Store())],
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
                                args=[Constant(value='stock.stock_location_stock', kind=None)],
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
                                        slice=Constant(value='stock.quant', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_update_available_quantity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_2',
                                        ctx=Load(),
                                    ),
                                    Name(id='location', ctx=Load()),
                                    Constant(value=4.0, kind=None),
                                ],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='stock.quant', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_update_available_quantity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_3',
                                        ctx=Load(),
                                    ),
                                    Name(id='location', ctx=Load()),
                                    Constant(value=8.0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='kit_product_qty', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_7_3',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_2',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_3',
                                            ctx=Load(),
                                        ),
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='qty_available', kind=None)],
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
                                    Name(id='kit_product_qty', ctx=Load()),
                                    Constant(value=2, kind=None),
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
                    name='test_14_bom_kit_qty_multi_uom',
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
                            targets=[Name(id='uom_dozens', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_unit', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test units', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_dozens', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Test dozens', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_dozens', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='bom_line_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='product_unit', ctx=Load()),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uom_unit',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.0, kind=None),
                                            Constant(value='phantom', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='product_uom_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='product_dozens', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='uom_unit', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='location', ctx=Store())],
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
                                args=[Constant(value='stock.stock_location_stock', kind=None)],
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
                                        slice=Constant(value='stock.quant', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_update_available_quantity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_dozens', ctx=Load()),
                                    Name(id='location', ctx=Load()),
                                    Constant(value=1.0, kind=None),
                                ],
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
                                        value=Name(id='product_unit', ctx=Load()),
                                        attr='qty_available',
                                        ctx=Load(),
                                    ),
                                    Constant(value=12.0, kind=None),
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
                    name='test_20_bom_report',
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
                            value=Constant(value=' Simulate a crumble receipt with mrp and open the bom structure\n        report and check that data insde are correct.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_kg', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_kgm', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_litre', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_litre', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='crumble', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='Crumble', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='butter', ctx=Store())],
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
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Butter', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=7.01, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='biscuit', ctx=Store())],
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
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Biscuit', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1.5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_form_crumble', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_crumble', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='crumble', ctx=Load()),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_crumble', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=11, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_crumble', ctx=Load()),
                                    attr='product_uom_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='uom_kg', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_crumble', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_form_crumble', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='workcenter', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.workcenter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='costs_hour', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value='Deserts Table', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[Name(id='bom_crumble', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='bom', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='line', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='butter', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='uom_kg', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=5, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='line', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='biscuit', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='uom_kg', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=6, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='operation_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='operation', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='workcenter_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='workcenter', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Prepare biscuits', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='time_cycle_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=5, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='bom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='operation_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='operation', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='workcenter_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='workcenter', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Prepare butter', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='time_cycle_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=3, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='bom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='operation_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='operation', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='workcenter_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='workcenter', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Mix manually', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='time_cycle_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=5, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='bom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=11, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                        value=Subscript(
                                            value=Name(id='report_values', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_time', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=13.0, kind=None),
                                    Constant(value='Operation time should be the same for 1 unit or for the batch', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='operation_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=5, kind=None),
                                                    op=Div(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=10, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    op=Mult(),
                                    right=Constant(value=2, kind=None),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Constant(value=3, kind=None),
                                                op=Div(),
                                                right=Constant(value=60, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_digits',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='operations_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='operation_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='13 minute for 10$/hours -> 2.16', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='component_line', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='report_values', ctx=Load()),
                                    slice=Constant(value='lines', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='components', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='component_line', ctx=Load()),
                                            slice=Constant(value='prod_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='butter', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='component_line', ctx=Load()),
                                                                slice=Constant(value='total', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value=7.01, kind=None),
                                                                op=Mult(),
                                                                right=Constant(value=5, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='component_line', ctx=Load()),
                                            slice=Constant(value='prod_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='biscuit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='component_line', ctx=Load()),
                                                                slice=Constant(value='total', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value=1.5, kind=None),
                                                                op=Mult(),
                                                                right=Constant(value=6, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='total', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=46.21, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Product Bom Price is not correct', kind=None),
                                ],
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='report_values', ctx=Load()),
                                                        slice=Constant(value='lines', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='total', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=11.0, kind=None),
                                            ),
                                            Constant(value=4.2, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Product Unit Bom Price is not correct', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='report_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                        value=Subscript(
                                            value=Name(id='report_values', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_time', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=13.0, kind=None),
                                    Constant(value='Operation time should be the same for 1 unit or for the batch', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='operation_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=5, kind=None),
                                                    op=Div(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=10, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    op=Mult(),
                                    right=Constant(value=2, kind=None),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Constant(value=3, kind=None),
                                                op=Div(),
                                                right=Constant(value=60, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_digits',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='operations_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='operation_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='13 minute for 10$/hours -> 2.16', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='component_line', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='report_values', ctx=Load()),
                                    slice=Constant(value='lines', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='components', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='component_line', ctx=Load()),
                                            slice=Constant(value='prod_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='butter', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='component_line', ctx=Load()),
                                                                slice=Constant(value='total', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Constant(value=7.01, kind=None),
                                                                    op=Mult(),
                                                                    right=Constant(value=5, kind=None),
                                                                ),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=Constant(value=1, kind=None),
                                                                    op=Div(),
                                                                    right=Constant(value=11, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='component_line', ctx=Load()),
                                            slice=Constant(value='prod_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='biscuit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='component_line', ctx=Load()),
                                                                slice=Constant(value='total', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Constant(value=1.5, kind=None),
                                                                    op=Mult(),
                                                                    right=Constant(value=6, kind=None),
                                                                ),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=Constant(value=1, kind=None),
                                                                    op=Div(),
                                                                    right=Constant(value=11, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='total', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=6.17, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Product Unit Bom Price is not correct', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='report_values_12', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=12, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values_22', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=22, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='operation_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=10, kind=None),
                                                    op=Div(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=10, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    op=Mult(),
                                    right=Constant(value=2, kind=None),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Constant(value=6, kind=None),
                                                op=Div(),
                                                right=Constant(value=60, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_digits',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
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
                                        value=Subscript(
                                            value=Name(id='report_values_12', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_cost', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='report_values_22', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_cost', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='report_values_22', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_cost', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='operation_cost', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='report_values_23', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_crumble', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=23, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='operation_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value=15, kind=None),
                                                    op=Div(),
                                                    right=Constant(value=60, kind=None),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=10, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    op=Mult(),
                                    right=Constant(value=2, kind=None),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Constant(value=9, kind=None),
                                                op=Div(),
                                                right=Constant(value=60, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_digits',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
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
                                        value=Subscript(
                                            value=Name(id='report_values_23', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_cost', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='operation_cost', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cheese_cake', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Cheese Cake 300g', kind=None),
                                            Constant(value='product', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cream', ctx=Store())],
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
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='cream', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_litre', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_litre', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5.17, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_form_cheese_cake', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_cheese_cake', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='cheese_cake', ctx=Load()),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_cheese_cake', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=60, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_cheese_cake', ctx=Load()),
                                    attr='product_uom_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='uom_unit',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_cheese_cake', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_form_cheese_cake', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='workcenter_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.workcenter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='costs_hour', kind=None),
                                            Constant(value='time_start', kind=None),
                                            Constant(value='time_stop', kind=None),
                                        ],
                                        values=[
                                            Constant(value='cake mounting', kind=None),
                                            Constant(value=20, kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value=15, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[Name(id='bom_cheese_cake', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='bom', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='line', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='cream', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='uom_litre', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=3, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='bom_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='line', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='crumble', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='uom_kg', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=5.4, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='operation_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='operation', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='workcenter_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='workcenter', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Mix cheese and crumble', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='time_cycle_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=10, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='bom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='bom_cheese_cake', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='operation_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='new',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='operation', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='workcenter_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='workcenter_2', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='name',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='Cake mounting', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='time_cycle_manual',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=5, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='bom_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='bom_cheese_cake', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_cheese_cake', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=60, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
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
                                        value=Subscript(
                                            value=Name(id='report_values', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='operations_time', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=40.0, kind=None),
                                    Constant(value='Operation time should be the same for 1 unit or for the batch', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='operation_cost', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Constant(value=10, kind=None),
                                                op=Div(),
                                                right=Constant(value=60, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=10, kind=None),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_digits',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Name(id='float_round', ctx=Load()),
                                    args=[
                                        BinOp(
                                            left=BinOp(
                                                left=Constant(value=30, kind=None),
                                                op=Div(),
                                                right=Constant(value=60, kind=None),
                                            ),
                                            op=Mult(),
                                            right=Constant(value=20, kind=None),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_digits',
                                            value=Constant(value=2, kind=None),
                                        ),
                                    ],
                                ),
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
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='operations_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='operation_cost', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='component_line', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Name(id='report_values', ctx=Load()),
                                    slice=Constant(value='lines', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='components', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='component_line', ctx=Load()),
                                            slice=Constant(value='prod_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='cream', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='component_line', ctx=Load()),
                                                                slice=Constant(value='total', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value=3, kind=None),
                                                                op=Mult(),
                                                                right=Constant(value=5.17, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='component_line', ctx=Load()),
                                            slice=Constant(value='prod_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='crumble', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='crumble_cost', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_report_data',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='bom_id',
                                                                value=Attribute(
                                                                    value=Name(id='bom_crumble', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='searchQty',
                                                                value=Constant(value=5.4, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='searchVariant',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='total', kind=None),
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
                                                    Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='component_line', ctx=Load()),
                                                                slice=Constant(value='total', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='crumble_cost', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_digits',
                                                                value=Constant(value=2, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='total', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value=27.18, kind=None),
                                                op=Add(),
                                                right=Name(id='crumble_cost', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Product Bom Price is not correct', kind=None),
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
                    name='test_21_bom_report_variant',
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
                            value=Constant(value=' Test a sub BoM process with multiple variants.\n        BOM 1:\n        product template = car\n        quantity = 5 units\n        - red paint 50l -> red car (product.product)\n        - blue paint 50l -> blue car\n        - red dashboard with gps -> red car with GPS\n        - red dashboard w/h gps -> red w/h GPS\n        - blue dashboard with gps -> blue car with GPS\n        - blue dashboard w/h gps -> blue w/h GPS\n\n        BOM 2:\n        product_tmpl = dashboard\n        quantity = 2\n        - red paint 1l -> red dashboard (product.product)\n        - blue paint 1l -> blue dashboard\n        - gps -> dashboard with gps\n\n        Check the Price for a Blue Car with GPS -> 910$:\n        10l of blue paint -> 200$\n        1 blue dashboard GPS -> 710$:\n            - 0.5l of blue paint -> 10$\n            - GPS -> 700$\n\n        Check the price for a red car -> 10.5l of red paint -> 210$\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car',
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Car', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gps_attribute',
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
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='GPS', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gps_yes',
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
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Yes', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='gps_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gps_no',
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
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='No', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='gps_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car_gps_attribute_line',
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
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='car',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='gps_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='gps_yes',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='gps_no',
                                                                            ctx=Load(),
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car_gps_yes',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='car_gps_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car_gps_no',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='car_gps_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='color_attribute',
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
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Color', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='color_red',
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
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Red', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='color_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='color_blue',
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
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Blue', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='color_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car_color_attribute_line',
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
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='car',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='color_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='color_red',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='color_blue',
                                                                            ctx=Load(),
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car_color_red',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='car_color_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='car_color_blue',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='car_color_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_litre', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_litre', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='paint',
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
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='uom_po_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Paint', kind=None),
                                            Attribute(
                                                value=Name(id='uom_litre', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_litre', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='paint_color_attribute_line',
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
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='paint',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='color_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='color_red',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='color_blue',
                                                                            ctx=Load(),
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='paint_color_red',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paint_color_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='paint_color_blue',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paint_color_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='paint',
                                            ctx=Load(),
                                        ),
                                        attr='product_variant_ids',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='standard_price', kind=None)],
                                        values=[Constant(value=20, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard',
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
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Dashboard', kind=None),
                                            Constant(value=1000, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard_gps_attribute_line',
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
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='gps_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='gps_yes',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='gps_no',
                                                                            ctx=Load(),
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard_gps_yes',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dashboard_gps_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard_gps_no',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dashboard_gps_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard_color_attribute_line',
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
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='color_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='color_red',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='color_blue',
                                                                            ctx=Load(),
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
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard_color_red',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dashboard_color_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='dashboard_color_blue',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dashboard_color_attribute_line',
                                        ctx=Load(),
                                    ),
                                    attr='product_template_value_ids',
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='gps',
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='GPS', kind=None),
                                            Constant(value=700, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_form_car', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_car', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='car',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_form_car', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=5, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_form_car', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint_color_red',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_litre', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=50, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_color_red',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_form_car', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint_color_blue',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_litre', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=50, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_color_blue',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_form_car', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_gps_yes',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_color_red',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_gps_yes',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_color_red',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_form_car', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_gps_yes',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_color_blue',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_gps_yes',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_color_blue',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_form_car', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_gps_no',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_color_red',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_gps_no',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_color_red',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_form_car', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_gps_no',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='dashboard_color_blue',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_gps_no',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='car_color_blue',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_car', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_form_car', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_dashboard', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_dashboard', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='dashboard',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_dashboard', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_dashboard', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint_color_red',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_litre', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
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
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard_color_red',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_dashboard', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='paint_color_blue',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_litre', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
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
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard_color_blue',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_dashboard', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='gps',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=2, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='bom_product_template_attribute_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='dashboard_gps_yes',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_dashboard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_dashboard', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='blue_car_with_gps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='car',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='car_color_blue',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='car_gps_yes',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_car', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Attribute(
                                            value=Name(id='blue_car_with_gps', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='blue_paint', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paint',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='paint_color_blue',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='blue_paint', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='prod_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='prod_qty', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=10, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='blue_dashboard_gps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='dashboard',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dashboard_color_blue',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='dashboard_gps_yes',
                                            ctx=Load(),
                                        ),
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
                                    Attribute(
                                        value=Name(id='blue_dashboard_gps', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='prod_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='prod_qty', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='component', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Name(id='report_values', ctx=Load()),
                                        slice=Constant(value='lines', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='components', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values_dashboad', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_bom',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='component', ctx=Load()),
                                        slice=Constant(value='child_bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='component', ctx=Load()),
                                        slice=Constant(value='prod_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='component', ctx=Load()),
                                        slice=Constant(value='prod_qty', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='component', ctx=Load()),
                                        slice=Constant(value='line_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Subscript(
                                            value=Name(id='component', ctx=Load()),
                                            slice=Constant(value='level', kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='report_values_dashboad', ctx=Load()),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
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
                                        value=Name(id='blue_paint', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='report_values_dashboad', ctx=Load()),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='prod_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                            attr='gps',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='report_values_dashboad', ctx=Load()),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='prod_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='report_values_dashboad', ctx=Load()),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=10, kind=None),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='report_values_dashboad', ctx=Load()),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=700, kind=None),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=710, kind=None),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='report_values', ctx=Load()),
                                                    slice=Constant(value='lines', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='components', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=200, kind=None),
                                ],
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='report_values', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=910, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='red_car_without_gps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='car',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='car_color_red',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='car_gps_no',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_car', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=1, kind=None),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Attribute(
                                            value=Name(id='red_car_without_gps', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
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
                                        value=Subscript(
                                            value=Name(id='report_values', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=210, kind=None),
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
                    name='test_22_bom_report_recursive_bom',
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
                            value=Constant(value=' Test report with recursive BoM and different quantities.\n        BoM 1:\n        product = Finished (units)\n        quantity = 100 units\n        - Semi-Finished 5 kg\n\n        BoM 2:\n        product = Semi-Finished (kg)\n        quantity = 11 kg\n        - Assembly 2 dozens\n\n        BoM 3:\n        product = Assembly (dozens)\n        quantity = 5 dozens\n        - Raw Material 4 litres (product.product 5$/litre)\n\n        Check the Price for 80 units of Finished -> 2.92$:\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_kg', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_kgm', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_dozen', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_litre', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_litre', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='finished', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='Finished', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='semi_finished', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='Semi-Finished', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='assembly', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='Assembly', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_dozen', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_dozen', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='raw_material', ctx=Store())],
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
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Raw Material', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_litre', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_litre', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='finished', ctx=Load()),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_finished', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='semi_finished', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_kg', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_semi_finished', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_semi_finished', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='semi_finished', ctx=Load()),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_semi_finished', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=11, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_semi_finished', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='assembly', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_dozen', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=2, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_semi_finished', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_semi_finished', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_assembly', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_assembly', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='assembly', ctx=Load()),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_assembly', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=5, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_assembly', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='raw_material', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_litre', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=4, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_assembly', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_assembly', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.mrp.report_bom_structure', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom_finished', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Constant(value=80, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='report_values', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=2.92, kind=None),
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
                    name='test_validate_no_bom_line_with_same_product',
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
                            value=Constant(value='\n        Cannot set a BOM line on a BOM with the same product as the BOM itself\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='finished', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='Finished', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_unit', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='finished', ctx=Load()),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_finished', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='finished', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_unit', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='ValidationError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='bom_finished', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='bom_finished', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_validate_no_bom_line_with_same_product_variant',
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
                            value=Constant(value='\n        Cannot set a BOM line on a BOM with the same product variant as the BOM itself\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_template',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_3',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_finished', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_3',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_unit', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='ValidationError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='savepoint',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='bom_finished', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='bom_finished', ctx=Load()),
                                            attr='save',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_validate_bom_line_with_different_product_variant',
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
                            value=Constant(value='\n        Can set a BOM line on a BOM with a different product variant as the BOM itself (same product)\n        Usecase for example A black T-shirt made  from a white T-shirt and\n        black color.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_template',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='product_7_3',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_finished', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_2',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_unit', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_validate_bom_line_with_variant_of_bom_product',
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
                            value=Constant(value='\n        Can set a BOM line on a BOM with a product variant when the BOM has no variant selected\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_unit', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_tmpl_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_6',
                                    ctx=Load(),
                                ),
                                attr='product_tmpl_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='product_qty',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=100, kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom_finished', ctx=Load()),
                                                attr='bom_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_7_2',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='uom_unit', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=5, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_finished', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='bom_finished', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_replenishment',
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
                            value=Constant(value=' Tests the auto generation of manual orderpoints.\n            The multiple quantity of the orderpoint should be the\n            quantity of the BoM in the UoM of the product.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='uom_kg', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_kgm', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='uom_gram', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_gram', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_gram', ctx=Store())],
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
                                        ],
                                        values=[
                                            Constant(value='Product sold in grams', kind=None),
                                            Constant(value='product', kind=None),
                                            Attribute(
                                                value=Name(id='uom_gram', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_gram', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='product_qty', kind=None),
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='product_gram', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='product_gram', ctx=Load()),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='uom_kg', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2.0, kind=None),
                                            Constant(value='normal', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='picking_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='picking_form', ctx=Load()),
                                    attr='picking_type_id',
                                    ctx=Store(),
                                ),
                            ],
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
                                args=[Constant(value='stock.picking_type_out', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='picking_form', ctx=Load()),
                                                attr='move_ids_without_package',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='move', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='product_gram', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='product_uom_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=2300.0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer_picking', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_form', ctx=Load()),
                                    attr='save',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='customer_picking', ctx=Load()),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='stock.warehouse.orderpoint', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_orderpoint_action',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                        slice=Constant(value='stock.warehouse.orderpoint', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_orderpoint_action',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='orderpoint', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.warehouse.orderpoint', kind=None),
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
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='product_gram', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='orderpoint', ctx=Load()),
                                        attr='qty_multiple',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
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
                                        value=Name(id='orderpoint', ctx=Load()),
                                        attr='qty_to_order',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2300.0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='manufacturing_route_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mrp.route_warehouse0_manufacture', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='manufacturing_route', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.location.route', kind=None),
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
                                                    Constant(value='=', kind=None),
                                                    Name(id='manufacturing_route_id', ctx=Load()),
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
                            targets=[Name(id='orderpoint_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[Name(id='orderpoint', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='orderpoint_form', ctx=Load()),
                                    attr='route_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='manufacturing_route', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='orderpoint_form', ctx=Load()),
                                    attr='save',
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
                                        value=Name(id='orderpoint', ctx=Load()),
                                        attr='qty_multiple',
                                        ctx=Load(),
                                    ),
                                    Constant(value=2000.0, kind=None),
                                ],
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
                                        value=Name(id='orderpoint', ctx=Load()),
                                        attr='qty_to_order',
                                        ctx=Load(),
                                    ),
                                    Constant(value=4000.0, kind=None),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
