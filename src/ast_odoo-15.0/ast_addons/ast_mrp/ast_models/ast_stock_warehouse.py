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
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
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
                    targets=[Name(id='manufacture_to_resupply', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Manufacture to Resupply', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When products are manufactured, they can be manufactured in this warehouse.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='manufacture_pull_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.rule', kind=None),
                            Constant(value='Manufacture Rule', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='manufacture_mto_pull_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.rule', kind=None),
                            Constant(value='Manufacture MTO Rule', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pbm_mto_pull_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.rule', kind=None),
                            Constant(value='Picking Before Manufacturing MTO Rule', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sam_rule_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.rule', kind=None),
                            Constant(value='Stock After Manufacturing Rule', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='manu_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Manufacturing Operation Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('code', '=', 'mrp_operation'), ('company_id', '=', company_id)]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pbm_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Picking Before Manufacturing Operation Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sam_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Stock After Manufacturing Operation Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='manufacture_steps', ctx=Store())],
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
                                            Constant(value='mrp_one_step', kind=None),
                                            Constant(value='Manufacture (1 step)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='pbm', kind=None),
                                            Constant(value='Pick components and then manufacture (2 steps)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='pbm_sam', kind=None),
                                            Constant(value='Pick components, manufacture and then store products (3 steps)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Manufacture', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='mrp_one_step', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Produce : Move the components to the production location        directly and start the manufacturing process.\nPick / Produce : Unload        the components from the Stock to Input location first, and then        transfer it to the Production location.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pbm_route_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location.route', kind=None),
                            Constant(value='Picking Before Manufacturing Route', kind=None),
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
                    targets=[Name(id='pbm_loc_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='Picking before Manufacturing Location', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sam_loc_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='Stock after Manufacturing Location', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
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
                                                keys=[
                                                    Constant(value='mrp_one_step', kind=None),
                                                    Constant(value='pbm', kind=None),
                                                    Constant(value='pbm_sam', kind=None),
                                                ],
                                                values=[
                                                    List(elts=[], ctx=Load()),
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
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='pbm_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='pbm_type_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='pull', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='Routing',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='pbm_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='production_location_id', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='manu_type_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='pull', kind=None),
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
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='pbm_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='pbm_type_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='pull', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='Routing',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='pbm_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='production_location_id', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='manu_type_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='pull', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='Routing',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='sam_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='lot_stock_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='sam_type_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='push', kind=None),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='warehouse', ctx=Load()),
                                                    attr='_get_receive_rules_dict',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_production_location',
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
                            targets=[Name(id='location', ctx=Store())],
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='usage', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='production', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
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
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='location', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Can't find any production location.", kind=None)],
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
                            value=Name(id='location', ctx=Load()),
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
                                        keys=[Constant(value='pbm_route_id', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='routing_key', kind=None),
                                                    Constant(value='depends', kind=None),
                                                    Constant(value='route_update_values', kind=None),
                                                    Constant(value='route_create_values', kind=None),
                                                    Constant(value='rules_values', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='manufacture_steps',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='manufacture_steps', kind=None),
                                                            Constant(value='manufacture_to_resupply', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='active', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_routename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='route_type',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='manufacture_steps',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manufacture_steps',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='mrp_one_step', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_categ_selectable', kind=None),
                                                            Constant(value='warehouse_selectable', kind=None),
                                                            Constant(value='product_selectable', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='sequence', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=True, kind=None),
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
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[Constant(value=True, kind=None)],
                                                    ),
                                                ],
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
                                    value=Name(id='routes', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_receive_routes_values',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='manufacture_to_resupply', kind=None)],
                                        keywords=[],
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
                    name='_get_route_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='route_type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='names', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='mrp_one_step', kind=None),
                                    Constant(value='pbm', kind=None),
                                    Constant(value='pbm_sam', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Manufacture (1 step)', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Pick components and then manufacture', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Pick components, manufacture and then store products (3 steps)', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='route_type', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='names', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Name(id='names', ctx=Load()),
                                        slice=Name(id='route_type', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
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
                                            attr='_get_route_name',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='route_type', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                            targets=[Name(id='location_src', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='manufacture_steps',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='mrp_one_step', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_stock_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='pbm_loc_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='production_location', ctx=Store())],
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
                        Assign(
                            targets=[Name(id='location_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='manufacture_steps',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='pbm_sam', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sam_loc_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lot_stock_id',
                                        ctx=Load(),
                                    ),
                                ],
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
                                            Constant(value='manufacture_pull_id', kind=None),
                                            Constant(value='manufacture_mto_pull_id', kind=None),
                                            Constant(value='pbm_mto_pull_id', kind=None),
                                            Constant(value='sam_rule_id', kind=None),
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
                                                        elts=[
                                                            Constant(value='manufacture_steps', kind=None),
                                                            Constant(value='manufacture_to_resupply', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='action', kind=None),
                                                            Constant(value='procure_method', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='picking_type_id', kind=None),
                                                            Constant(value='route_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='manufacture', kind=None),
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
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manu_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_find_global_route',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='mrp.route_warehouse0_manufacture', kind=None),
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Manufacture', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='active', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='location_id', kind=None),
                                                            Constant(value='propagate_cancel', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='manufacture_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_rulename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='location_id', ctx=Load()),
                                                                    Constant(value=False, kind=None),
                                                                    Constant(value='Production', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='location_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manufacture_steps',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='pbm_sam', kind=None)],
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
                                                        elts=[
                                                            Constant(value='manufacture_steps', kind=None),
                                                            Constant(value='manufacture_to_resupply', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='procure_method', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='action', kind=None),
                                                            Constant(value='auto', kind=None),
                                                            Constant(value='route_id', kind=None),
                                                            Constant(value='location_id', kind=None),
                                                            Constant(value='location_src_id', kind=None),
                                                            Constant(value='picking_type_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='mts_else_mto', kind=None),
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
                                                            Attribute(
                                                                value=Name(id='production_location', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='location_src', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manu_type_id',
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
                                                            Constant(value='active', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_format_rulename',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='location_src', ctx=Load()),
                                                                    Name(id='production_location', ctx=Load()),
                                                                    Constant(value='MTO', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='manufacture_to_resupply',
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
                                                        elts=[
                                                            Constant(value='manufacture_steps', kind=None),
                                                            Constant(value='manufacture_to_resupply', kind=None),
                                                        ],
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
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='pbm_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='MTO', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='pbm_loc_id',
                                                                    ctx=Load(),
                                                                ),
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
                                                                    attr='pbm_type_id',
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
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='manufacture_steps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotEq()],
                                                                        comparators=[Constant(value='mrp_one_step', kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='manufacture_to_resupply',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                                        elts=[
                                                            Constant(value='manufacture_steps', kind=None),
                                                            Constant(value='manufacture_to_resupply', kind=None),
                                                        ],
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
                                                                        Constant(value='mrp.route_warehouse0_manufacture', kind=None),
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Manufacture', kind=None)],
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
                                                                        attr='sam_loc_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='lot_stock_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                keywords=[],
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
                                                                    attr='sam_loc_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sam_type_id',
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
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='manufacture_steps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='pbm_sam', kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='manufacture_to_resupply',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                    name='_get_locations_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
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
                                    attr='_get_locations_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='code',
                                        value=Name(id='code', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='def_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='manufacture_steps', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='manufacture_steps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='manufacture_steps', kind=None),
                                    Subscript(
                                        value=Name(id='def_values', ctx=Load()),
                                        slice=Constant(value='manufacture_steps', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='code', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='company_id', kind=None),
                                    Subscript(
                                        value=Name(id='def_values', ctx=Load()),
                                        slice=Constant(value='company_id', kind=None),
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
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='pbm_loc_id', kind=None),
                                            Constant(value='sam_loc_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='active', kind=None),
                                                    Constant(value='usage', kind=None),
                                                    Constant(value='barcode', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Pre-Production', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Name(id='manufacture_steps', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='pbm', kind=None),
                                                                    Constant(value='pbm_sam', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value='internal', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_valid_barcode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='code', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value='-PREPRODUCTION', kind=None),
                                                            ),
                                                            Name(id='company_id', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='active', kind=None),
                                                    Constant(value='usage', kind=None),
                                                    Constant(value='barcode', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Post-Production', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Name(id='manufacture_steps', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='pbm_sam', kind=None)],
                                                    ),
                                                    Constant(value='internal', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_valid_barcode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='code', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value='-POSTPRODUCTION', kind=None),
                                                            ),
                                                            Name(id='company_id', ctx=Load()),
                                                        ],
                                                        keywords=[],
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
                                            Constant(value='pbm_type_id', kind=None),
                                            Constant(value='sam_type_id', kind=None),
                                            Constant(value='manu_type_id', kind=None),
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
                                                            args=[Constant(value='Sequence picking before manufacturing', kind=None)],
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
                                                        right=Constant(value='/PC/', kind=None),
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
                                                            args=[Constant(value='Sequence stock after manufacturing', kind=None)],
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
                                                        right=Constant(value='/SFP/', kind=None),
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
                                                            args=[Constant(value='Sequence production', kind=None)],
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
                                                        right=Constant(value='/MO/', kind=None),
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
                                            Constant(value='pbm_type_id', kind=None),
                                            Constant(value='sam_type_id', kind=None),
                                            Constant(value='manu_type_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='use_create_lots', kind=None),
                                                    Constant(value='use_existing_lots', kind=None),
                                                    Constant(value='default_location_src_id', kind=None),
                                                    Constant(value='default_location_dest_id', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='sequence_code', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Pick Components', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='internal', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=True, kind=None),
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
                                                            attr='pbm_loc_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BinOp(
                                                        left=Name(id='next_sequence', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value='PC', kind=None),
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
                                                    Constant(value='default_location_src_id', kind=None),
                                                    Constant(value='default_location_dest_id', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='sequence_code', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Store Finished Product', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='internal', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=True, kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sam_loc_id',
                                                            ctx=Load(),
                                                        ),
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
                                                    BinOp(
                                                        left=Name(id='next_sequence', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=3, kind=None),
                                                    ),
                                                    Constant(value='SFP', kind=None),
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
                                                    Constant(value='sequence', kind=None),
                                                    Constant(value='sequence_code', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Manufacturing', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='mrp_operation', kind=None),
                                                    Constant(value=True, kind=None),
                                                    Constant(value=True, kind=None),
                                                    BinOp(
                                                        left=Name(id='next_sequence', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=2, kind=None),
                                                    ),
                                                    Constant(value='MO', kind=None),
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
                                            Constant(value='pbm_type_id', kind=None),
                                            Constant(value='sam_type_id', kind=None),
                                            Constant(value='manu_type_id', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='barcode', kind=None),
                                                ],
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='manufacture_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manufacture_steps',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='pbm', kind=None),
                                                                            Constant(value='pbm_sam', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='active',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                        right=Constant(value='-PC', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='barcode', kind=None),
                                                ],
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='manufacture_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manufacture_steps',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='pbm_sam', kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='active',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                        right=Constant(value='-SFP', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='default_location_src_id', kind=None),
                                                    Constant(value='default_location_dest_id', kind=None),
                                                ],
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='manufacture_to_resupply',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='active',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='manufacture_steps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[In()],
                                                                        comparators=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='pbm', kind=None),
                                                                                    Constant(value='pbm_sam', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='pbm_loc_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='manufacture_steps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='pbm_sam', kind=None)],
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='sam_loc_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                            value=Name(id='data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Name(id='field', ctx=Load()),
                                            ops=[In()],
                                            comparators=[Name(id='vals', ctx=Load())],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='field', ctx=Store()),
                                                iter=Tuple(
                                                    elts=[
                                                        Constant(value='manufacture_steps', kind=None),
                                                        Constant(value='manufacture_to_resupply', kind=None),
                                                    ],
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
                                For(
                                    target=Name(id='warehouse', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='warehouse', ctx=Load()),
                                                    attr='_update_location_manufacture',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='manufacture_steps', kind=None),
                                                            Attribute(
                                                                value=Name(id='warehouse', ctx=Load()),
                                                                attr='manufacture_steps',
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
                                    orelse=[],
                                    type_comment=None,
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
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_all_routes',
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
                                    attr='_get_all_routes',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='routes', ctx=Store()),
                            op=BitOr(),
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
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
                                                            args=[arg(arg='self', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manufacture_to_resupply',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='manufacture_pull_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='manufacture_pull_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='route_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='manufacture_pull_id', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='route_id', kind=None)],
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
                    name='_update_location_manufacture',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_manufacture_step', annotation=None, type_comment=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='pbm_loc_id', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[
                                            Compare(
                                                left=Name(id='new_manufacture_step', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='mrp_one_step', kind=None)],
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sam_loc_id', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[
                                            Compare(
                                                left=Name(id='new_manufacture_step', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='pbm_sam', kind=None)],
                                            ),
                                        ],
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
                    name='_update_name_and_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
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
                                            Name(id='StockWarehouse', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_update_name_and_code',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='code', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='warehouse', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='warehouse', ctx=Load()),
                                                attr='manufacture_pull_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='warehouse', ctx=Load()),
                                                        attr='manufacture_pull_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='name', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='warehouse', ctx=Load()),
                                                                            attr='manufacture_pull_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='warehouse', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='name', ctx=Load()),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
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
                            type_comment=None,
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
        ClassDef(
            name='Orderpoint',
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
                    value=Constant(value='stock.warehouse.orderpoint', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_product_is_not_kit',
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
                            test=Call(
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='&', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_tmpl_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='phantom', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='count',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='A product with a kit-type bill of materials can not have a reordering rule.', kind=None)],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
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
