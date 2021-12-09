Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='SaleOrder',
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
                    value=Constant(value='sale.order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mrp_production_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Count of MO generated', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_mrp_production_count', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='mrp.group_mrp_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_mrp_production_count',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='procurement.group', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='sale_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='ids:array_agg(id)', kind=None)],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Constant(value='sale_id', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mrp_count', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Name(id='data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='procurement_groups', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='procurement.group', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='item', ctx=Load()),
                                                slice=Constant(value='ids', kind=None),
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
                                            value=Name(id='mrp_count', ctx=Load()),
                                            slice=Subscript(
                                                value=Subscript(
                                                    value=Name(id='item', ctx=Load()),
                                                    slice=Constant(value='sale_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='procurement_groups', ctx=Load()),
                                                                    attr='stock_move_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='created_production_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=BitOr(),
                                                right=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='procurement_groups', ctx=Load()),
                                                                attr='mrp_production_ids',
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sale', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='sale', ctx=Load()),
                                            attr='mrp_production_count',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mrp_count', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='sale', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='procurement_group_id.stock_move_ids.created_production_id.procurement_group_id.mrp_production_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_mrp_production',
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
                            targets=[Name(id='procurement_groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='procurement.group', kind=None),
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
                                                    Constant(value='sale_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mrp_production_ids', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='procurement_groups', ctx=Load()),
                                                    attr='stock_move_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='created_production_id',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='procurement_groups', ctx=Load()),
                                                attr='mrp_production_ids',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                ],
                                values=[
                                    Constant(value='mrp.production', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='mrp_production_ids', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='form', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='mrp_production_ids', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='domain', kind=None),
                                                    Constant(value='view_mode', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Manufacturing Orders Generated by %s', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Call(
                                                                        func=Name(id='list', ctx=Load()),
                                                                        args=[Name(id='mrp_production_ids', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='tree,form', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
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
            name='SaleOrderLine',
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
                    value=Constant(value='sale.order.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_to_deliver',
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
                            value=Constant(value='The inventory widget should now be visible in more cases if the product is consumable.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SaleOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_qty_to_deliver',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='boms', ctx=Store())],
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
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='sale', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='boms', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='move_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='bom_line_id.bom_id', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='draft', kind=None),
                                                                    Constant(value='sent', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='boms', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='boms', ctx=Load()),
                                                                attr='_bom_find',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='company_id',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                keyword(
                                                                    arg='bom_type',
                                                                    value=Constant(value='phantom', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='relevant_bom', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='boms', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='b', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='b', ctx=Load()),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='phantom', kind=None)],
                                                        ),
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='b', ctx=Load()),
                                                                                attr='product_tmpl_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[
                                                                                Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='product_tmpl_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='b', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='relevant_bom', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='display_qty_widget',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='draft', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='consu', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='components', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get_components',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='components', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='components', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='display_qty_widget',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
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
                                Constant(value='product_uom_qty', kind=None),
                                Constant(value='qty_delivered', kind=None),
                                Constant(value='product_id', kind=None),
                                Constant(value='state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_qty_delivered',
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
                                            Name(id='SaleOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_compute_qty_delivered',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='order_line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='order_line', ctx=Load()),
                                            attr='qty_delivered_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='stock_move', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='boms', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='move_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotEq()],
                                                                    comparators=[Constant(value='cancel', kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='bom_line_id.bom_id', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='dropship', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='boms', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Name(id='any', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='_is_dropshipped',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='m', ctx=Store()),
                                                                        iter=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='move_ids',
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
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='boms', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='boms', ctx=Load()),
                                                                attr='_bom_find',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='order_line', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='company_id',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                keyword(
                                                                    arg='bom_type',
                                                                    value=Constant(value='phantom', kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='order_line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='dropship', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='relevant_bom', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='boms', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='b', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='b', ctx=Load()),
                                                                        attr='type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='phantom', kind=None)],
                                                                ),
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='b', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[
                                                                                Attribute(
                                                                                    value=Name(id='order_line', ctx=Load()),
                                                                                    attr='product_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        BoolOp(
                                                                            op=And(),
                                                                            values=[
                                                                                Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='b', ctx=Load()),
                                                                                        attr='product_tmpl_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[
                                                                                        Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='order_line', ctx=Load()),
                                                                                                attr='product_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='product_tmpl_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                UnaryOp(
                                                                                    op=Not(),
                                                                                    operand=Attribute(
                                                                                        value=Name(id='b', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='relevant_bom', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Name(id='dropship', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='moves', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='move_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                            vararg=None,
                                                                            kwonlyargs=[],
                                                                            kw_defaults=[],
                                                                            kwarg=None,
                                                                            defaults=[],
                                                                        ),
                                                                        body=Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='m', ctx=Load()),
                                                                                attr='state',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[NotEq()],
                                                                            comparators=[Constant(value='cancel', kind=None)],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='moves', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='all', ctx=Load()),
                                                                        args=[
                                                                            GeneratorExp(
                                                                                elt=Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='m', ctx=Load()),
                                                                                        attr='state',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='done', kind=None)],
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='m', ctx=Store()),
                                                                                        iter=Name(id='moves', ctx=Load()),
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
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='qty_delivered',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='qty_delivered',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=0.0, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                        Continue(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='moves', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='move_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='m', ctx=Load()),
                                                                                attr='state',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value='done', kind=None)],
                                                                        ),
                                                                        UnaryOp(
                                                                            op=Not(),
                                                                            operand=Attribute(
                                                                                value=Name(id='m', ctx=Load()),
                                                                                attr='scrapped',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='filters', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='incoming_moves', kind=None),
                                                            Constant(value='outgoing_moves', kind=None),
                                                        ],
                                                        values=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='m', ctx=Load()),
                                                                                    attr='location_dest_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='usage',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value='customer', kind=None)],
                                                                        ),
                                                                        BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                UnaryOp(
                                                                                    op=Not(),
                                                                                    operand=Attribute(
                                                                                        value=Name(id='m', ctx=Load()),
                                                                                        attr='origin_returned_move_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                                BoolOp(
                                                                                    op=And(),
                                                                                    values=[
                                                                                        Attribute(
                                                                                            value=Name(id='m', ctx=Load()),
                                                                                            attr='origin_returned_move_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        Attribute(
                                                                                            value=Name(id='m', ctx=Load()),
                                                                                            attr='to_refund',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Compare(
                                                                            left=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='m', ctx=Load()),
                                                                                    attr='location_dest_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='usage',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[NotEq()],
                                                                            comparators=[Constant(value='customer', kind=None)],
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='m', ctx=Load()),
                                                                            attr='to_refund',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='order_qty', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='product_uom',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='product_uom_qty',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='relevant_bom', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='qty_delivered', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='moves', ctx=Load()),
                                                            attr='_compute_kit_quantities',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='order_qty', ctx=Load()),
                                                            Name(id='relevant_bom', ctx=Load()),
                                                            Name(id='filters', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='order_line', ctx=Load()),
                                                            attr='qty_delivered',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='relevant_bom', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='qty_delivered', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='order_line', ctx=Load()),
                                                                attr='product_uom',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='boms', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Call(
                                                                func=Name(id='all', ctx=Load()),
                                                                args=[
                                                                    GeneratorExp(
                                                                        elt=BoolOp(
                                                                            op=And(),
                                                                            values=[
                                                                                Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='m', ctx=Load()),
                                                                                        attr='state',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='done', kind=None)],
                                                                                ),
                                                                                Compare(
                                                                                    left=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='m', ctx=Load()),
                                                                                            attr='location_dest_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='usage',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[Constant(value='customer', kind=None)],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='m', ctx=Store()),
                                                                                iter=Attribute(
                                                                                    value=Name(id='order_line', ctx=Load()),
                                                                                    attr='move_ids',
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
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='qty_delivered',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Attribute(
                                                                        value=Name(id='order_line', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='order_line', ctx=Load()),
                                                                            attr='qty_delivered',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=0.0, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_get_bom_component_qty',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='bom_quantity', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_uom',
                                        ctx=Load(),
                                    ),
                                    attr='_compute_quantity',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=1, kind=None),
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
                                    value=Name(id='bom', ctx=Load()),
                                    attr='explode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='bom_quantity', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='components', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='line', ctx=Store()),
                                    Name(id='line_data', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='lines', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='uom', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='product_uom_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qty', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='line_data', ctx=Load()),
                                        slice=Constant(value='qty', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='components', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product', ctx=Load()),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='uom', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Name(id='components', ctx=Load()),
                                                            slice=Name(id='product', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='uom', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='from_uom', ctx=Store())],
                                                    value=Name(id='uom', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='to_uom', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='uom.uom', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='components', ctx=Load()),
                                                                    slice=Name(id='product', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='uom', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='qty', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='from_uom', ctx=Load()),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='qty', ctx=Load()),
                                                            Name(id='to_uom', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='components', ctx=Load()),
                                                    slice=Name(id='product', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='qty', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='qty', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='to_uom', ctx=Store())],
                                            value=Attribute(
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
                                                    args=[Name(id='product', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='uom', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='to_uom', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='from_uom', ctx=Store())],
                                                    value=Name(id='uom', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='qty', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='from_uom', ctx=Load()),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='qty', ctx=Load()),
                                                            Name(id='to_uom', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='components', ctx=Load()),
                                                    slice=Name(id='product', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='qty', kind=None),
                                                    Constant(value='uom', kind=None),
                                                ],
                                                values=[
                                                    Name(id='qty', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='to_uom', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='components', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_qty_procurement',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='previous_product_uom_qty', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
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
                            targets=[Name(id='bom', ctx=Store())],
                            value=Subscript(
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
                                        attr='_bom_find',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='bom_type',
                                            value=Constant(value='phantom', kind=None),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='previous_product_uom_qty', ctx=Load()),
                                ],
                            ),
                            body=[
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='previous_product_uom_qty', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='previous_product_uom_qty', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SaleOrderLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_qty_procurement',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='previous_product_uom_qty',
                                        value=Name(id='previous_product_uom_qty', ctx=Load()),
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
