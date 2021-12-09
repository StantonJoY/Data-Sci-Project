Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ReportStockRule',
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
                    value=Constant(value='report.stock.report_stock_rule', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock rule report', kind=None),
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
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='product_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='product_id', kind=None),
                                    Name(id='docids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='warehouse_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='warehouse_ids', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='product_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='warehouses', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.warehouse', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='warehouse_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='routes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_routes',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='relevant_rules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='routes', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='rule_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
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
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[Name(id='warehouses', ctx=Load())],
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
                            targets=[Name(id='rules_and_loc', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Name(id='relevant_rules', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rules_and_loc', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_rule_loc',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='rule', ctx=Load()),
                                                    Name(id='product', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='locations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sort_locations',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rules_and_loc', ctx=Load()),
                                    Name(id='warehouses', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reordering_rules', ctx=Store())],
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
                                                        value=Name(id='product', ctx=Load()),
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
                        AugAssign(
                            target=Name(id='locations', ctx=Store()),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='reordering_rules', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='location_id', kind=None)],
                                        keywords=[],
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
                                            left=Name(id='l', ctx=Load()),
                                            ops=[NotIn()],
                                            comparators=[Name(id='locations', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='locations_names', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='locations', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='display_name', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header_lines', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='location', ctx=Store()),
                            iter=Name(id='locations', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='rr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='reordering_rules', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='r', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='r', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='location', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
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
                                    targets=[Name(id='putaways', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='product', ctx=Load()),
                                                attr='putaway_rule_ids',
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
                                                        value=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='location_in_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='location', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
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
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='putaways', ctx=Load()),
                                            Name(id='rr', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='header_lines', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='location', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='putaway', kind=None),
                                                    Constant(value='orderpoint', kind=None),
                                                ],
                                                values=[
                                                    List(elts=[], ctx=Load()),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='putaway', ctx=Store()),
                                            iter=Name(id='putaways', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='header_lines', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='location', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='putaway', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='putaway', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='r', ctx=Store()),
                                            iter=Name(id='rr', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='header_lines', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='location', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='orderpoint', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='r', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='route_lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='colors', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_route_colors',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='color_index', ctx=Store()),
                                    Name(id='route', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='routes', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='rules_to_display', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='route', ctx=Load()),
                                            attr='rule_ids',
                                            ctx=Load(),
                                        ),
                                        op=BitAnd(),
                                        right=Name(id='relevant_rules', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='rules_to_display', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='route_color', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='colors', ctx=Load()),
                                                slice=BinOp(
                                                    left=Name(id='color_index', ctx=Load()),
                                                    op=Mod(),
                                                    right=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='colors', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='color_index', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='color_index', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='rule', ctx=Store()),
                                            iter=Name(id='rules_to_display', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='rule_loc', ctx=Store())],
                                                    value=Subscript(
                                                        value=ListComp(
                                                            elt=Name(id='r', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='r', ctx=Store()),
                                                                    iter=Name(id='rules_and_loc', ctx=Load()),
                                                                    ifs=[
                                                                        Compare(
                                                                            left=Subscript(
                                                                                value=Name(id='r', ctx=Load()),
                                                                                slice=Constant(value='rule', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Name(id='rule', ctx=Load())],
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='res', ctx=Store())],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='x', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='range', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='locations_names', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='res', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[List(elts=[], ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='idx', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='locations_names', ctx=Load()),
                                                            attr='index',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='rule_loc', ctx=Load()),
                                                                    slice=Constant(value='destination', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='display_name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='tpl', ctx=Store())],
                                                    value=Tuple(
                                                        elts=[
                                                            Name(id='rule', ctx=Load()),
                                                            Constant(value='destination', kind=None),
                                                            Name(id='route_color', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Name(id='idx', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='tpl', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='idx', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='locations_names', ctx=Load()),
                                                            attr='index',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='rule_loc', ctx=Load()),
                                                                    slice=Constant(value='source', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='display_name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='tpl', ctx=Store())],
                                                    value=Tuple(
                                                        elts=[
                                                            Name(id='rule', ctx=Load()),
                                                            Constant(value='origin', kind=None),
                                                            Name(id='route_color', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Name(id='idx', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='tpl', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='route_lines', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='res', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
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
                            value=Dict(
                                keys=[
                                    Constant(value='docs', kind=None),
                                    Constant(value='locations', kind=None),
                                    Constant(value='header_lines', kind=None),
                                    Constant(value='route_lines', kind=None),
                                ],
                                values=[
                                    Name(id='product', ctx=Load()),
                                    Name(id='locations', ctx=Load()),
                                    Name(id='header_lines', ctx=Load()),
                                    Name(id='route_lines', ctx=Load()),
                                ],
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
                    name='_get_route_colors',
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
                                    Constant(value='#FFA500', kind=None),
                                    Constant(value='#800080', kind=None),
                                    Constant(value='#228B22', kind=None),
                                    Constant(value='#008B8B', kind=None),
                                    Constant(value='#4682B4', kind=None),
                                    Constant(value='#FF0000', kind=None),
                                    Constant(value='#32CD32', kind=None),
                                ],
                                ctx=Load(),
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
                    name='_get_routes',
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
                        Expr(
                            value=Constant(value=" Extract the routes to display from the wizard's content.\n        ", kind=None),
                        ),
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
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='product_id', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='warehouse_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.warehouse', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='warehouse_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Attribute(
                                        value=Name(id='product', ctx=Load()),
                                        attr='route_ids',
                                        ctx=Load(),
                                    ),
                                    op=BitOr(),
                                    right=Attribute(
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='categ_id',
                                            ctx=Load(),
                                        ),
                                        attr='total_route_ids',
                                        ctx=Load(),
                                    ),
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='warehouse_ids', ctx=Load()),
                                        attr='mapped',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='route_ids', kind=None)],
                                    keywords=[],
                                ),
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
                    name='_get_rule_loc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
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
                                    value=Name(id='rule', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='rule', kind=None),
                                    Constant(value='source', kind=None),
                                    Constant(value='destination', kind=None),
                                ],
                                values=[
                                    Name(id='rule', ctx=Load()),
                                    Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='location_src_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='_sort_locations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rules_and_loc', annotation=None, type_comment=None),
                            arg(arg='warehouses', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' We order the locations by setting first the locations of type supplier and manufacture,\n            then we add the locations grouped by warehouse and we finish by the locations of type\n            customer and the ones that were not added by the sort.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='all_src', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.location', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='concat',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=ListComp(
                                            elt=Subscript(
                                                value=Name(id='r', ctx=Load()),
                                                slice=Constant(value='source', kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='r', ctx=Store()),
                                                    iter=Name(id='rules_and_loc', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_dest', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.location', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='concat',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=ListComp(
                                            elt=Subscript(
                                                value=Name(id='r', ctx=Load()),
                                                slice=Constant(value='destination', kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='r', ctx=Store()),
                                                    iter=Name(id='rules_and_loc', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='all_locations', ctx=Store())],
                            value=BinOp(
                                left=Name(id='all_src', ctx=Load()),
                                op=BitOr(),
                                right=Name(id='all_dest', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ordered_locations', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.location', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='locations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='all_locations', ctx=Load()),
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
                                            left=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='usage',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='supplier', kind=None),
                                                        Constant(value='production', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='warehouse_id', ctx=Store()),
                            iter=Name(id='warehouses', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='all_warehouse_locations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='all_locations', ctx=Load()),
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
                                                    left=Attribute(
                                                        value=Name(id='l', ctx=Load()),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='warehouse_id', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='starting_rules', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='d', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='d', ctx=Store()),
                                                iter=Name(id='rules_and_loc', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='d', ctx=Load()),
                                                            slice=Constant(value='source', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='all_warehouse_locations', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='starting_rules', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='start_locations', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stock.location', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='concat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=ListComp(
                                                            elt=Subscript(
                                                                value=Name(id='r', ctx=Load()),
                                                                slice=Constant(value='destination', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='r', ctx=Store()),
                                                                    iter=Name(id='starting_rules', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='starting_rules', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='d', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='d', ctx=Store()),
                                                        iter=Name(id='rules_and_loc', ctx=Load()),
                                                        ifs=[
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='d', ctx=Load()),
                                                                    slice=Constant(value='source', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='all_dest', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='start_locations', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stock.location', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='concat',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Starred(
                                                        value=ListComp(
                                                            elt=Subscript(
                                                                value=Name(id='r', ctx=Load()),
                                                                slice=Constant(value='source', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='r', ctx=Store()),
                                                                    iter=Name(id='starting_rules', ctx=Load()),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='used_rules', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.rule', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='locations', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_sort_locations_by_warehouse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='rules_and_loc', ctx=Load()),
                                            Name(id='used_rules', ctx=Load()),
                                            Name(id='start_locations', ctx=Load()),
                                            Name(id='ordered_locations', ctx=Load()),
                                            Name(id='warehouse_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='location', ctx=Load()),
                                                    ops=[NotIn()],
                                                    comparators=[Name(id='locations', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='location', ctx=Store()),
                                                        iter=Name(id='all_warehouse_locations', ctx=Load()),
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
                                            targets=[Name(id='remaining_locations', ctx=Store())],
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
                                                                slice=Constant(value='stock.location', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='concat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Starred(
                                                                value=ListComp(
                                                                    elt=Subscript(
                                                                        value=Name(id='r', ctx=Load()),
                                                                        slice=Constant(value='source', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='r', ctx=Store()),
                                                                            iter=Name(id='rules_and_loc', ctx=Load()),
                                                                            ifs=[],
                                                                            is_async=0,
                                                                        ),
                                                                    ],
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
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
                                                            left=Name(id='l', ctx=Load()),
                                                            ops=[NotIn()],
                                                            comparators=[Name(id='locations', ctx=Load())],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='locations', ctx=Store()),
                                            op=BitOr(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sort_locations_by_warehouse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='rules_and_loc', ctx=Load()),
                                                    Name(id='used_rules', ctx=Load()),
                                                    Name(id='remaining_locations', ctx=Load()),
                                                    Name(id='ordered_locations', ctx=Load()),
                                                    Name(id='warehouse_id', ctx=Load()),
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
                        AugAssign(
                            target=Name(id='locations', ctx=Store()),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Name(id='all_locations', ctx=Load()),
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
                                            left=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='usage',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[Constant(value='customer', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        AugAssign(
                            target=Name(id='locations', ctx=Store()),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Name(id='all_locations', ctx=Load()),
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
                                            left=Name(id='l', ctx=Load()),
                                            ops=[NotIn()],
                                            comparators=[Name(id='locations', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='locations', ctx=Load()),
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
                    name='_sort_locations_by_warehouse',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='rules_and_loc', annotation=None, type_comment=None),
                            arg(arg='used_rules', annotation=None, type_comment=None),
                            arg(arg='start_locations', annotation=None, type_comment=None),
                            arg(arg='ordered_locations', annotation=None, type_comment=None),
                            arg(arg='warehouse_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' We order locations by putting first the locations that are not the destination of others and do it recursively.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='start_locations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='start_locations', ctx=Load()),
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
                                            left=Attribute(
                                                value=Name(id='l', ctx=Load()),
                                                attr='warehouse_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='warehouse_id', ctx=Load())],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='ordered_locations', ctx=Store()),
                            op=BitOr(),
                            value=Name(id='start_locations', ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id='rules_start', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Name(id='rules_and_loc', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='rule', ctx=Load()),
                                            slice=Constant(value='source', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='start_locations', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='rules_start', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='rule', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='used_rules', ctx=Store()),
                                            op=BitOr(),
                                            value=Subscript(
                                                value=Name(id='rule', ctx=Load()),
                                                slice=Constant(value='rule', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='rules_start', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='rules_start_dest_locations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.location', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='concat',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=ListComp(
                                                    elt=Subscript(
                                                        value=Name(id='r', ctx=Load()),
                                                        slice=Constant(value='destination', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='r', ctx=Store()),
                                                            iter=Name(id='rules_start', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='remaining_rules', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='stock.rule', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='concat',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Starred(
                                                    value=ListComp(
                                                        elt=Subscript(
                                                            value=Name(id='r', ctx=Load()),
                                                            slice=Constant(value='rule', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='r', ctx=Store()),
                                                                iter=Name(id='rules_and_loc', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Name(id='used_rules', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='remaining_rules_location', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.location', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='r', ctx=Store()),
                                    iter=Name(id='rules_and_loc', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='r', ctx=Load()),
                                                    slice=Constant(value='rule', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='remaining_rules', ctx=Load())],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='remaining_rules_location', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Subscript(
                                                        value=Name(id='r', ctx=Load()),
                                                        slice=Constant(value='destination', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='start_locations', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='rules_start_dest_locations', ctx=Load()),
                                            op=Sub(),
                                            right=Name(id='ordered_locations', ctx=Load()),
                                        ),
                                        op=Sub(),
                                        right=Name(id='remaining_rules_location', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ordered_locations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_sort_locations_by_warehouse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='rules_and_loc', ctx=Load()),
                                            Name(id='used_rules', ctx=Load()),
                                            Name(id='start_locations', ctx=Load()),
                                            Name(id='ordered_locations', ctx=Load()),
                                            Name(id='warehouse_id', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='ordered_locations', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
