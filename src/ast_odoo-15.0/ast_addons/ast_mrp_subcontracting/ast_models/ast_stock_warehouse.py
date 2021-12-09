Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='StockWarehouse',
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
                    value=Constant(value='stock.warehouse', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subcontracting_to_resupply', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Resupply Subcontractors', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Resupply subcontractors with components', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subcontracting_mto_pull_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.rule', kind=None),
                            Constant(value='Subcontracting MTO Rule', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subcontracting_pull_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.rule', kind=None),
                            Constant(value='Subcontracting MTS Rule', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subcontracting_route_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location.route', kind=None),
                            Constant(value='Resupply Subcontractor', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subcontracting_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Subcontracting Operation Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='code', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='mrp_operation', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='subcontracting_resupply_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Subcontracting Resupply Operation Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='code', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value='outgoing', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_rules_dict',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_rules_dict',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subcontract_location_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_subcontracting_location',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='warehouse', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='warehouse', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='subcontract', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='Routing',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='lot_stock_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='subcontract_location_id', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='subcontracting_resupply_type_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='pull', kind=None),
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
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_routes_values',
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
                            targets=[Name(id='routes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_routes_values',
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
                                    value=Name(id='routes', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='subcontracting_route_id', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='routing_key', kind=None),
                                                    Constant(value='depends', kind=None),
                                                    Constant(value='route_create_values', kind=None),
                                                    Constant(value='route_update_values', kind=None),
                                                    Constant(value='rules_values', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='subcontract', kind=None),
                                                    List(
                                                        elts=[Constant(value='subcontracting_to_resupply', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_categ_selectable', kind=None),
                                                            Constant(value='warehouse_selectable', kind=None),
                                                            Constant(value='product_selectable', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='sequence', kind=None),
                                                            Constant(value='name', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value=True, kind=None),
                                                            Constant(value=False, kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=10, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_routename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='name',
                                                                        value=Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Resupply Subcontractor', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='subcontracting_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='subcontracting_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='routes', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_global_route_rules_values',
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
                            targets=[Name(id='rules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_global_route_rules_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subcontract_location_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_subcontracting_location',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='production_location_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_production_location',
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
                                    value=Name(id='rules', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subcontracting_mto_pull_id', kind=None),
                                            Constant(value='subcontracting_pull_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='depends', kind=None),
                                                    Constant(value='create_values', kind=None),
                                                    Constant(value='update_values', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Constant(value='subcontracting_to_resupply', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='procure_method', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='action', kind=None),
                                                            Constant(value='auto', kind=None),
                                                            Constant(value='route_id', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='location_id', kind=None),
                                                            Constant(value='location_src_id', kind=None),
                                                            Constant(value='picking_type_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='make_to_order', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='pull', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_find_global_route',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='stock.route_warehouse0_mto', kind=None),
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Make To Order', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_rulename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='lot_stock_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='subcontract_location_id', ctx=Load()),
                                                                    Constant(value='MTO', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='subcontract_location_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='lot_stock_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='subcontracting_resupply_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='subcontracting_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='depends', kind=None),
                                                    Constant(value='create_values', kind=None),
                                                    Constant(value='update_values', kind=None),
                                                ],
                                                values=[
                                                    List(
                                                        elts=[Constant(value='subcontracting_to_resupply', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='procure_method', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='action', kind=None),
                                                            Constant(value='auto', kind=None),
                                                            Constant(value='route_id', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='location_id', kind=None),
                                                            Constant(value='location_src_id', kind=None),
                                                            Constant(value='picking_type_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='make_to_order', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='pull', kind=None),
                                                            Constant(value='manual', kind=None),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_find_global_route',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='mrp_subcontracting.route_resupply_subcontractor_mto', kind=None),
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Resupply Subcontractor on Order', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_rulename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='lot_stock_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='subcontract_location_id', ctx=Load()),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='production_location_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='subcontract_location_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='subcontracting_resupply_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='subcontracting_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='rules', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_picking_type_create_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='max_sequence', annotation=None, type_comment=None),
                        ],
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
                                        Name(id='data', ctx=Store()),
                                        Name(id='next_sequence', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_picking_type_create_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='max_sequence', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subcontracting_type_id', kind=None),
                                            Constant(value='subcontracting_resupply_type_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='use_create_components_lots', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='sequence_code', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Subcontracting', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='mrp_operation', kind=None),
                                                    Constant(value=True, kind=None),
                                                    BinOp(
                                                        left=Name(id='next_sequence', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                    Constant(value='SBC', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='use_create_lots', kind=None),
                                                    Constant(value='use_existing_lots', kind=None),
                                                    Constant(value='default_location_dest_id', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='sequence_code', kind=None),
                                                    Constant(value='print_label', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Resupply Subcontractor', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='outgoing', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=True, kind=None),
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_get_subcontracting_location',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Name(id='next_sequence', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=3, kind=None),
                                                    ),
                                                    Constant(value='RES', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='data', ctx=Load()),
                                    BinOp(
                                        left=Name(id='max_sequence', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=4, kind=None),
                                    ),
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
                    name='_get_sequence_values',
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
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_sequence_values',
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
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subcontracting_type_id', kind=None),
                                            Constant(value='subcontracting_resupply_type_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='prefix', kind=None),
                                                    Constant(value='padding', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=' ', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Sequence subcontracting', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='/SBC/', kind=None),
                                                    ),
                                                    Constant(value=5, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='prefix', kind=None),
                                                    Constant(value='padding', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=' ', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Sequence Resupply Subcontractor', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='code',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='/RES/', kind=None),
                                                    ),
                                                    Constant(value=5, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_picking_type_update_values',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_picking_type_update_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subcontract_location_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_subcontracting_location',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='production_location_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_production_location',
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
                                    value=Name(id='data', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='subcontracting_type_id', kind=None),
                                            Constant(value='subcontracting_resupply_type_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='default_location_src_id', kind=None),
                                                    Constant(value='default_location_dest_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Attribute(
                                                        value=Name(id='subcontract_location_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='production_location_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='default_location_src_id', kind=None),
                                                    Constant(value='default_location_dest_id', kind=None),
                                                    Constant(value='barcode', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='production_location_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='subcontract_location_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='replace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value=' ', kind=None),
                                                                        Constant(value='', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='upper',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value='-RESUPPLY', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_subcontracting_location',
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
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='subcontracting_location_id',
                                ctx=Load(),
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
