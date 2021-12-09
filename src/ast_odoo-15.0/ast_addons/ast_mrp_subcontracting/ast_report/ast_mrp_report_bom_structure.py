Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ReportBomStructure',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='report.mrp.report_bom_structure', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_subcontracting_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='seller', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                            arg(arg='bom_quantity', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ratio_uom_seller', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='seller', ctx=Load()),
                                        attr='product_uom',
                                        ctx=Load(),
                                    ),
                                    attr='ratio',
                                    ctx=Load(),
                                ),
                                op=Div(),
                                right=Attribute(
                                    value=Attribute(
                                        value=Name(id='bom', ctx=Load()),
                                        attr='product_uom_id',
                                        ctx=Load(),
                                    ),
                                    attr='ratio',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='quantity', kind=None),
                                    Constant(value='uom', kind=None),
                                    Constant(value='prod_cost', kind=None),
                                    Constant(value='bom_cost', kind=None),
                                    Constant(value='level', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='seller', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='seller', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='bom_quantity', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='seller', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        op=Div(),
                                        right=Name(id='ratio_uom_seller', ctx=Load()),
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='seller', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            op=Div(),
                                            right=Name(id='ratio_uom_seller', ctx=Load()),
                                        ),
                                        op=Mult(),
                                        right=Name(id='bom_quantity', ctx=Load()),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='level', ctx=Load()),
                                            Constant(value=0, kind=None),
                                        ],
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
                    name='_get_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='factor', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='price', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_get_price',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='factor', ctx=Load()),
                                    Name(id='product', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='bom', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='subcontract', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='bom_quantity', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Name(id='factor', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='seller', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='quantity',
                                                value=Name(id='bom_quantity', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='uom_id',
                                                value=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='params',
                                                value=Dict(
                                                    keys=[Constant(value='subcontractor_ids', kind=None)],
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='bom', ctx=Load()),
                                                            attr='subcontractor_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='seller', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='price', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_price',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='seller', ctx=Load()),
                                                        attr='price',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='price', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_bom',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='line_qty', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ReportBomStructure', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_bom',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom_id', ctx=Load()),
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='line_qty', ctx=Load()),
                                    Name(id='line_id', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom', ctx=Store())],
                            value=Subscript(
                                value=Name(id='res', ctx=Load()),
                                slice=Constant(value='bom', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='bom', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='subcontract', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='bom_quantity', ctx=Store())],
                                    value=Name(id='line_qty', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='line_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='current_line', ctx=Store())],
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
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='line_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='bom_quantity', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='current_line', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='line_qty', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='seller', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='product', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='quantity',
                                                value=Name(id='bom_quantity', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='uom_id',
                                                value=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='params',
                                                value=Dict(
                                                    keys=[Constant(value='subcontractor_ids', kind=None)],
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='bom', ctx=Load()),
                                                            attr='subcontractor_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='seller', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='subcontracting', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_subcontracting_line',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='bom', ctx=Load()),
                                                    Name(id='seller', ctx=Load()),
                                                    Name(id='level', ctx=Load()),
                                                    Name(id='bom_quantity', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='total', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='subcontracting', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='bom_cost', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                FunctionDef(
                    name='_get_sub_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='line_qty', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                            arg(arg='child_bom_ids', annotation=None, type_comment=None),
                            arg(arg='unfolded', annotation=None, type_comment=None),
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
                                    attr='_get_sub_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='line_qty', ctx=Load()),
                                    Name(id='line_id', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                    Name(id='child_bom_ids', ctx=Load()),
                                    Name(id='unfolded', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='bom', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='subcontract', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
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
                                        args=[Name(id='product_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bom_quantity', ctx=Store())],
                                    value=Name(id='line_qty', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='line_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='current_line', ctx=Store())],
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
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='line_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='bom_quantity', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='current_line', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='line_qty', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='seller', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='quantity',
                                                value=Name(id='bom_quantity', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='uom_id',
                                                value=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='params',
                                                value=Dict(
                                                    keys=[Constant(value='subcontractor_ids', kind=None)],
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='bom', ctx=Load()),
                                                            attr='subcontractor_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='seller', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values_sub', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_subcontracting_line',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='bom', ctx=Load()),
                                                    Name(id='seller', ctx=Load()),
                                                    Name(id='level', ctx=Load()),
                                                    Name(id='bom_quantity', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values_sub', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='bom', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values_sub', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='Subcontracting: ', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='values_sub', ctx=Load()),
                                                    slice=Constant(value='name', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values_sub', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
