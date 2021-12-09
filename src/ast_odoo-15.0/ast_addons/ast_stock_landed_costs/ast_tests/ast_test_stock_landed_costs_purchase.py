Module(
    body=[
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.stock_landed_costs.tests.common',
            names=[alias(name='TestStockLandedCostsCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.stock_landed_costs.tests.test_stockvaluationlayer',
            names=[alias(name='TestStockValuationLCCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.stock_account.tests.test_stockvaluation',
            names=[alias(name='_create_accounting_data', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='tagged', asname=None),
                alias(name='Form', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestLandedCosts',
            bases=[Name(id='TestStockLandedCostsCommon', ctx=Load())],
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
                                            Name(id='TestLandedCosts', ctx=Load()),
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='picking_in',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Picking',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='picking_type_id', kind=None),
                                            Constant(value='location_id', kind=None),
                                            Constant(value='location_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='supplier_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='in_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='supplier_location_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lot_stock_id',
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Move',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='picking_id', kind=None),
                                            Constant(value='location_id', kind=None),
                                            Constant(value='location_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_refrigerator',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_refrigerator',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=5, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_refrigerator',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='picking_in',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='supplier_location_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lot_stock_id',
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
                                        attr='Move',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='picking_id', kind=None),
                                            Constant(value='location_id', kind=None),
                                            Constant(value='location_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_oven',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_oven',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=10, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_oven',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='picking_in',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='supplier_location_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lot_stock_id',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='picking_out',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Picking',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='picking_type_id', kind=None),
                                            Constant(value='location_id', kind=None),
                                            Constant(value='location_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='customer_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='out_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lot_stock_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='customer_location_id',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Move',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='product_id', kind=None),
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='product_uom', kind=None),
                                            Constant(value='picking_id', kind=None),
                                            Constant(value='location_id', kind=None),
                                            Constant(value='location_dest_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_refrigerator',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_refrigerator',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_refrigerator',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='picking_out',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='warehouse',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lot_stock_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='customer_location_id',
                                                ctx=Load(),
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
                    name='test_00_landed_costs_on_incoming_shipment',
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
                            value=Constant(value=' Test landed cost on incoming shipment ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='income_ship', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_incoming_shipment',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stock_landed_cost', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_landed_costs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='equal_price_unit', kind=None),
                                            Constant(value='quantity_price_unit', kind=None),
                                            Constant(value='weight_price_unit', kind=None),
                                            Constant(value='volume_price_unit', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=150, kind=None),
                                            Constant(value=250, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                    ),
                                    Name(id='income_ship', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost', ctx=Load()),
                                    attr='compute_landed_cost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='valid_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='equal', kind=None),
                                    Constant(value='by_quantity_refrigerator', kind=None),
                                    Constant(value='by_quantity_oven', kind=None),
                                    Constant(value='by_weight_refrigerator', kind=None),
                                    Constant(value='by_weight_oven', kind=None),
                                    Constant(value='by_volume_refrigerator', kind=None),
                                    Constant(value='by_volume_oven', kind=None),
                                ],
                                values=[
                                    Constant(value=5.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    Constant(value=100.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    Constant(value=200, kind=None),
                                    Constant(value=5.0, kind=None),
                                    Constant(value=15.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_validate_additional_landed_cost_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='stock_landed_cost', ctx=Load()),
                                    Name(id='valid_vals', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost', ctx=Load()),
                                    attr='button_validate',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='stock_landed_cost', ctx=Load()),
                                        attr='account_move_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Landed costs should be available account move lines', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='account_entry', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='account.move.line', kind=None),
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
                                                        Constant(value='move_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='stock_landed_cost', ctx=Load()),
                                                                attr='account_move_id',
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
                                        List(
                                            elts=[
                                                Constant(value='debit', kind=None),
                                                Constant(value='credit', kind=None),
                                                Constant(value='move_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='move_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
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
                                    Subscript(
                                        value=Name(id='account_entry', ctx=Load()),
                                        slice=Constant(value='debit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='account_entry', ctx=Load()),
                                        slice=Constant(value='credit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Debit and credit are not equal', kind=None),
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
                                        value=Name(id='account_entry', ctx=Load()),
                                        slice=Constant(value='debit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=430.0, kind=None),
                                    Constant(value='Wrong Account Entry', kind=None),
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
                    name='test_01_negative_landed_costs_on_incoming_shipment',
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
                            value=Constant(value=' Test negative landed cost on incoming shipment ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='income_ship', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_incoming_shipment',
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
                                    attr='_process_outgoing_shipment',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='stock_landed_cost', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_landed_costs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='equal_price_unit', kind=None),
                                            Constant(value='quantity_price_unit', kind=None),
                                            Constant(value='weight_price_unit', kind=None),
                                            Constant(value='volume_price_unit', kind=None),
                                        ],
                                        values=[
                                            Constant(value=10, kind=None),
                                            Constant(value=150, kind=None),
                                            Constant(value=250, kind=None),
                                            Constant(value=20, kind=None),
                                        ],
                                    ),
                                    Name(id='income_ship', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost', ctx=Load()),
                                    attr='compute_landed_cost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='valid_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='equal', kind=None),
                                    Constant(value='by_quantity_refrigerator', kind=None),
                                    Constant(value='by_quantity_oven', kind=None),
                                    Constant(value='by_weight_refrigerator', kind=None),
                                    Constant(value='by_weight_oven', kind=None),
                                    Constant(value='by_volume_refrigerator', kind=None),
                                    Constant(value='by_volume_oven', kind=None),
                                ],
                                values=[
                                    Constant(value=5.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    Constant(value=100.0, kind=None),
                                    Constant(value=50.0, kind=None),
                                    Constant(value=200.0, kind=None),
                                    Constant(value=5.0, kind=None),
                                    Constant(value=15.0, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_validate_additional_landed_cost_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='stock_landed_cost', ctx=Load()),
                                    Name(id='valid_vals', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost', ctx=Load()),
                                    attr='button_validate',
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='stock_landed_cost', ctx=Load()),
                                        attr='account_move_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Landed costs should be available account move lines', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='stock_negative_landed_cost', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_landed_costs',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='equal_price_unit', kind=None),
                                            Constant(value='quantity_price_unit', kind=None),
                                            Constant(value='weight_price_unit', kind=None),
                                            Constant(value='volume_price_unit', kind=None),
                                        ],
                                        values=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=5, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=50, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=50, kind=None),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=5, kind=None),
                                            ),
                                        ],
                                    ),
                                    Name(id='income_ship', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                    attr='compute_landed_cost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='valid_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='equal', kind=None),
                                    Constant(value='by_quantity_refrigerator', kind=None),
                                    Constant(value='by_quantity_oven', kind=None),
                                    Constant(value='by_weight_refrigerator', kind=None),
                                    Constant(value='by_weight_oven', kind=None),
                                    Constant(value='by_volume_refrigerator', kind=None),
                                    Constant(value='by_volume_oven', kind=None),
                                ],
                                values=[
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=2.5, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=16.67, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=33.33, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=10.0, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=40.0, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1.25, kind=None),
                                    ),
                                    UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=3.75, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_validate_additional_landed_cost_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='stock_negative_landed_cost', ctx=Load()),
                                    Name(id='valid_vals', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                    attr='button_validate',
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
                                        value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='done', kind=None),
                                    Constant(value='Negative landed costs should be in done state', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                        attr='account_move_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Landed costs should be available account move lines', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='account_entry', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='account.move.line', kind=None),
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
                                                        Constant(value='move_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                                                attr='account_move_id',
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
                                        List(
                                            elts=[
                                                Constant(value='debit', kind=None),
                                                Constant(value='credit', kind=None),
                                                Constant(value='move_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        List(
                                            elts=[Constant(value='move_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
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
                                    Subscript(
                                        value=Name(id='account_entry', ctx=Load()),
                                        slice=Constant(value='debit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='account_entry', ctx=Load()),
                                        slice=Constant(value='credit', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Debit and credit are not equal', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_lines', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by volume - Microwave Oven', kind=None),
                                            Constant(value=3.75, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by volume - Microwave Oven', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=3.75, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by weight - Microwave Oven', kind=None),
                                            Constant(value=40.0, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by weight - Microwave Oven', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=40.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by quantity - Microwave Oven', kind=None),
                                            Constant(value=33.33, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by quantity - Microwave Oven', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=33.33, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='equal split - Microwave Oven', kind=None),
                                            Constant(value=2.5, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='equal split - Microwave Oven', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=2.5, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by volume - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=0.5, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by volume - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=0.5, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by weight - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=4.0, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by weight - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=4.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by weight - Refrigerator', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=10.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by weight - Refrigerator', kind=None),
                                            Constant(value=10.0, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by volume - Refrigerator', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=1.25, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by volume - Refrigerator', kind=None),
                                            Constant(value=1.25, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by quantity - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=6.67, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by quantity - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=6.67, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by quantity - Refrigerator', kind=None),
                                            Constant(value=16.67, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='split by quantity - Refrigerator', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=16.67, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='equal split - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=1.0, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='equal split - Refrigerator: 2.0 already out', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='equal split - Refrigerator', kind=None),
                                            Constant(value=2.5, kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='debit', kind=None),
                                            Constant(value='credit', kind=None),
                                        ],
                                        values=[
                                            Constant(value='equal split - Refrigerator', kind=None),
                                            Constant(value=0.0, kind=None),
                                            Constant(value=2.5, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                        attr='account_move_id',
                                        ctx=Load(),
                                    ),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='anglo_saxon_accounting',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='move_lines', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='split by volume - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=0.5, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='split by volume - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=0.5, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='split by weight - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=4.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='split by weight - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=4.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='split by quantity - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=6.67, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='split by quantity - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=6.67, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='equal split - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=1.0, kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='debit', kind=None),
                                                    Constant(value='credit', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='equal split - Refrigerator: 2.0 already out', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                    Constant(value=1.0, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='stock_negative_landed_cost', ctx=Load()),
                                                    attr='account_move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='line_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='d', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Tuple(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='d', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='d', ctx=Load()),
                                                                slice=Constant(value='debit', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='move_lines', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='d', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Tuple(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='d', ctx=Load()),
                                                                slice=Constant(value='name', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='d', ctx=Load()),
                                                                slice=Constant(value='debit', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
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
                    name='_process_incoming_shipment',
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
                            value=Constant(value=' Two product incoming shipment. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_in',
                                        ctx=Load(),
                                    ),
                                    attr='action_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_dict', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_in',
                                        ctx=Load(),
                                    ),
                                    attr='button_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Call(
                                                            func=Attribute(
                                                                value=Name(id='res_dict', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='res_model', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='res_dict', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='context', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='process',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='picking_in',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_process_outgoing_shipment',
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
                            value=Constant(value=' One product Outgoing shipment. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_out',
                                        ctx=Load(),
                                    ),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_out',
                                        ctx=Load(),
                                    ),
                                    attr='action_assign',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_dict', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_out',
                                        ctx=Load(),
                                    ),
                                    attr='button_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='wizard', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Call(
                                                            func=Attribute(
                                                                value=Name(id='res_dict', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='res_model', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='res_dict', ctx=Load()),
                                                        slice=Constant(value='context', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                                    value=Name(id='wizard', ctx=Load()),
                                    attr='process',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_landed_costs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='picking_in', annotation=None, type_comment=None),
                        ],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='LandedCost',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='picking_ids',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=6, kind=None),
                                                                Constant(value=0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='picking_in', ctx=Load()),
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
                                            ),
                                            keyword(
                                                arg='account_journal_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='expenses_journal',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='cost_lines',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='split_method', kind=None),
                                                                        Constant(value='price_unit', kind=None),
                                                                        Constant(value='product_id', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value='equal split', kind=None),
                                                                        Constant(value='equal', kind=None),
                                                                        Subscript(
                                                                            value=Name(id='value', ctx=Load()),
                                                                            slice=Constant(value='equal_price_unit', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='landed_cost',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
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
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='split_method', kind=None),
                                                                        Constant(value='price_unit', kind=None),
                                                                        Constant(value='product_id', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value='split by quantity', kind=None),
                                                                        Constant(value='by_quantity', kind=None),
                                                                        Subscript(
                                                                            value=Name(id='value', ctx=Load()),
                                                                            slice=Constant(value='quantity_price_unit', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='brokerage_quantity',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
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
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='split_method', kind=None),
                                                                        Constant(value='price_unit', kind=None),
                                                                        Constant(value='product_id', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value='split by weight', kind=None),
                                                                        Constant(value='by_weight', kind=None),
                                                                        Subscript(
                                                                            value=Name(id='value', ctx=Load()),
                                                                            slice=Constant(value='weight_price_unit', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='transportation_weight',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
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
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='split_method', kind=None),
                                                                        Constant(value='price_unit', kind=None),
                                                                        Constant(value='product_id', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value='split by volume', kind=None),
                                                                        Constant(value='by_volume', kind=None),
                                                                        Subscript(
                                                                            value=Name(id='value', ctx=Load()),
                                                                            slice=Constant(value='volume_price_unit', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='packaging_volume',
                                                                                ctx=Load(),
                                                                            ),
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
                    name='_validate_additional_landed_cost_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stock_landed_cost', annotation=None, type_comment=None),
                            arg(arg='valid_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='valuation', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='stock_landed_cost', ctx=Load()),
                                attr='valuation_adjustment_lines',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='add_cost', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='valuation', ctx=Load()),
                                        attr='additional_landed_cost',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='split_method', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='valuation', ctx=Load()),
                                            attr='cost_line_id',
                                            ctx=Load(),
                                        ),
                                        attr='split_method',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='valuation', ctx=Load()),
                                            attr='move_id',
                                            ctx=Load(),
                                        ),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='split_method', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='equal', kind=None)],
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
                                                    Name(id='add_cost', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='valid_vals', ctx=Load()),
                                                        slice=Constant(value='equal', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_error_message',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                slice=Constant(value='equal', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='add_cost', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='split_method', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='by_quantity', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='product', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_refrigerator',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                                                            Name(id='add_cost', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                slice=Constant(value='by_quantity_refrigerator', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_error_message',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='valid_vals', ctx=Load()),
                                                                        slice=Constant(value='by_quantity_refrigerator', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='add_cost', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='split_method', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='by_quantity', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='product', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='product_oven',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                                                    Name(id='add_cost', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='valid_vals', ctx=Load()),
                                                                        slice=Constant(value='by_quantity_oven', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_error_message',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                                slice=Constant(value='by_quantity_oven', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='add_cost', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='split_method', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='by_weight', kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='product', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='product_refrigerator',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                                                            Name(id='add_cost', ctx=Load()),
                                                                            Subscript(
                                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                                slice=Constant(value='by_weight_refrigerator', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_error_message',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='valid_vals', ctx=Load()),
                                                                                        slice=Constant(value='by_weight_refrigerator', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='add_cost', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='split_method', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='by_weight', kind=None)],
                                                                            ),
                                                                            Compare(
                                                                                left=Name(id='product', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='product_oven',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
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
                                                                                    Name(id='add_cost', ctx=Load()),
                                                                                    Subscript(
                                                                                        value=Name(id='valid_vals', ctx=Load()),
                                                                                        slice=Constant(value='by_weight_oven', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='_error_message',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                                                slice=Constant(value='by_weight_oven', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Name(id='add_cost', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Name(id='split_method', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='by_volume', kind=None)],
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Name(id='product', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
                                                                                            Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='product_refrigerator',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
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
                                                                                            Name(id='add_cost', ctx=Load()),
                                                                                            Subscript(
                                                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                                                slice=Constant(value='by_volume_refrigerator', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='_error_message',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Subscript(
                                                                                                        value=Name(id='valid_vals', ctx=Load()),
                                                                                                        slice=Constant(value='by_volume_refrigerator', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Name(id='add_cost', ctx=Load()),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Name(id='split_method', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[Constant(value='by_volume', kind=None)],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Name(id='product', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='product_oven',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
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
                                                                                                    Name(id='add_cost', ctx=Load()),
                                                                                                    Subscript(
                                                                                                        value=Name(id='valid_vals', ctx=Load()),
                                                                                                        slice=Constant(value='by_volume_oven', kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='_error_message',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Subscript(
                                                                                                                value=Name(id='valid_vals', ctx=Load()),
                                                                                                                slice=Constant(value='by_volume_oven', kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Name(id='add_cost', ctx=Load()),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
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
                                        ),
                                    ],
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
                    name='_error_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='actucal_cost', annotation=None, type_comment=None),
                            arg(arg='computed_cost', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Constant(value='Additional Landed Cost should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='actucal_cost', ctx=Load()),
                                        Name(id='computed_cost', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
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
        ClassDef(
            name='TestLandedCostsWithPurchaseAndInv',
            bases=[Name(id='TestStockValuationLCCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_invoice_after_lc',
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
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='anglo_saxon_accounting',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product1',
                                                ctx=Load(),
                                            ),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_cost_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='fifo', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product1',
                                                ctx=Load(),
                                            ),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_valuation',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='real_time', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='price_diff_account',
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
                                        slice=Constant(value='account.account', kind=None),
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
                                            Constant(value='user_type_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='price diff account', kind=None),
                                            Constant(value='price diff account', kind=None),
                                            Attribute(
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
                                                    args=[Constant(value='account.data_account_type_current_assets', kind=None)],
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product1',
                                        ctx=Load(),
                                    ),
                                    attr='property_account_creditor_price_difference',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='price_diff_account',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order', kind=None),
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
                                    value=Name(id='po_form', ctx=Load()),
                                    attr='partner_id',
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
                                        slice=Constant(value='res.partner', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='vendor', kind=None)],
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
                                            value=Attribute(
                                                value=Name(id='po_form', ctx=Load()),
                                                attr='order_line',
                                                ctx=Load(),
                                            ),
                                            attr='new',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='po_line', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='po_line', ctx=Load()),
                                            attr='product_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product1',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='po_line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='po_line', ctx=Load()),
                                            attr='price_unit',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=455.0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po_form', ctx=Load()),
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
                                    value=Name(id='order', ctx=Load()),
                                    attr='button_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='receipt', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='order', ctx=Load()),
                                    attr='picking_ids',
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
                                    value=Attribute(
                                        value=Name(id='receipt', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='quantity_done',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='receipt', ctx=Load()),
                                    attr='button_validate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='svl', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.valuation.layer', kind=None),
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
                                                    Constant(value='stock_move_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='receipt', ctx=Load()),
                                                            attr='move_lines',
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
                                keywords=[],
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
                                    Attribute(
                                        value=Name(id='svl', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=455, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='aml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move.line', kind=None),
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
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_stock_valuation', kind=None),
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
                                keywords=[],
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
                                    Attribute(
                                        value=Name(id='aml', ctx=Load()),
                                        attr='debit',
                                        ctx=Load(),
                                    ),
                                    Constant(value=455, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.landed.cost', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='picking_ids',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=6, kind=None),
                                                                Constant(value=0, kind=None),
                                                                List(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='receipt', ctx=Load()),
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
                                            ),
                                            keyword(
                                                arg='account_journal_id',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='stock_journal',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='cost_lines',
                                                value=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='split_method', kind=None),
                                                                        Constant(value='price_unit', kind=None),
                                                                        Constant(value='product_id', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value='equal split', kind=None),
                                                                        Constant(value='equal', kind=None),
                                                                        Constant(value=99, kind=None),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='productlc1',
                                                                                ctx=Load(),
                                                                            ),
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
                                    value=Name(id='lc', ctx=Load()),
                                    attr='compute_landed_cost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lc', ctx=Load()),
                                    attr='button_validate',
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
                                    attr='assertAlmostEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='lc', ctx=Load()),
                                            attr='valuation_adjustment_lines',
                                            ctx=Load(),
                                        ),
                                        attr='final_cost',
                                        ctx=Load(),
                                    ),
                                    Constant(value=554, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='svl', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.valuation.layer', kind=None),
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
                                                    Constant(value='stock_move_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='receipt', ctx=Load()),
                                                            attr='move_lines',
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
                                        arg='order',
                                        value=Constant(value='id desc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
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
                                    Attribute(
                                        value=Name(id='svl', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value=99, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='aml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move.line', kind=None),
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
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='default_account_stock_valuation', kind=None),
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
                                        arg='order',
                                        value=Constant(value='id desc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
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
                                    Attribute(
                                        value=Name(id='aml', ctx=Load()),
                                        attr='debit',
                                        ctx=Load(),
                                    ),
                                    Constant(value=99, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='move_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='account.move', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='in_invoice', kind=None),
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
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='invoice_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='move_form', ctx=Load()),
                                attr='date',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='order', ctx=Load()),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='move_form', ctx=Load()),
                                    attr='purchase_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='order', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='move_form', ctx=Load()),
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
                                    value=Name(id='move', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='price_diff_aml', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move.line', kind=None),
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
                                                    Constant(value='account_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='price_diff_account',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='move_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='price_diff_aml', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='No line should have been generated in the price difference account.', kind=None),
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
