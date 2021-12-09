Module(
    body=[
        ImportFrom(
            module='odoo.addons.stock_landed_costs.tests.common',
            names=[alias(name='TestStockLandedCostsCommon', asname=None)],
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
            name='TestStockLandedCostsRounding',
            bases=[Name(id='TestStockLandedCostsCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_stock_landed_costs_rounding',
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
                            targets=[Name(id='product_uom_unit_round_1', ctx=Store())],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='product_uom_unit_round_1', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='rounding', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Undivisible Units', kind=None),
                                            Constant(value=1.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='product_landed_cost_3', ctx=Store())],
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
                                            Constant(value='uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='LC product 3', kind=None),
                                            Attribute(
                                                value=Name(id='product_uom_unit_round_1', ctx=Load()),
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
                                        value=Attribute(
                                            value=Name(id='product_landed_cost_3', ctx=Load()),
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
                                            value=Name(id='product_landed_cost_3', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_stock_account_input_categ_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_expense', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='product_landed_cost_3', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_stock_account_output_categ_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_revenue', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_landed_cost_4', ctx=Store())],
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
                                            Constant(value='uom_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='LC product 4', kind=None),
                                            Attribute(
                                                value=Name(id='product_uom_unit_round_1', ctx=Load()),
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
                                        value=Attribute(
                                            value=Name(id='product_landed_cost_4', ctx=Load()),
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
                                            value=Name(id='product_landed_cost_4', ctx=Load()),
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='product_landed_cost_4', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_stock_account_input_categ_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_expense', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='product_landed_cost_4', ctx=Load()),
                                            attr='product_tmpl_id',
                                            ctx=Load(),
                                        ),
                                        attr='categ_id',
                                        ctx=Load(),
                                    ),
                                    attr='property_stock_account_output_categ_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_data',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='default_account_revenue', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_default_vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stock.picking', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='fields_get',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='picking_default_vals', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='picking_type_id', kind=None),
                                                Constant(value='move_lines', kind=None),
                                            ],
                                            values=[
                                                Constant(value='LC_pick_3', kind=None),
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
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='product_id', kind=None),
                                                                        Constant(value='product_uom_qty', kind=None),
                                                                        Constant(value='product_uom', kind=None),
                                                                        Constant(value='location_id', kind=None),
                                                                        Constant(value='location_dest_id', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='product_landed_cost_3', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value=13, kind=None),
                                                                        Attribute(
                                                                            value=Name(id='product_uom_unit_round_1', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='ref',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='stock.stock_location_customers', kind=None)],
                                                                            keywords=[],
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
                                                            ctx=Load(),
                                                        ),
                                                    ],
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
                            targets=[Name(id='picking_landed_cost_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_3', ctx=Load()),
                                    attr='_onchange_picking_type',
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
                                        value=Name(id='picking_landed_cost_3', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='_onchange_product_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='picking_landed_cost_3', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='move 3', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_3', ctx=Load()),
                                    attr='_convert_to_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='picking_landed_cost_3', ctx=Load()),
                                        attr='_cache',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_landed_cost_3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='picking_default_vals', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='picking_type_id', kind=None),
                                                Constant(value='move_lines', kind=None),
                                            ],
                                            values=[
                                                Constant(value='LC_pick_4', kind=None),
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
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=0, kind=None),
                                                                Constant(value=0, kind=None),
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='product_id', kind=None),
                                                                        Constant(value='product_uom_qty', kind=None),
                                                                        Constant(value='product_uom', kind=None),
                                                                        Constant(value='location_id', kind=None),
                                                                        Constant(value='location_dest_id', kind=None),
                                                                        Constant(value='price_unit', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Attribute(
                                                                            value=Name(id='product_landed_cost_4', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value=1, kind=None),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='ref',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='ref',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='stock.stock_location_customers', kind=None)],
                                                                            keywords=[],
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
                                                                        BinOp(
                                                                            left=Constant(value=17.0, kind=None),
                                                                            op=Div(),
                                                                            right=Constant(value=12.0, kind=None),
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
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_landed_cost_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_4', ctx=Load()),
                                    attr='_onchange_picking_type',
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
                                        value=Name(id='picking_landed_cost_4', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='_onchange_product_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='picking_landed_cost_4', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='move 4', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_4', ctx=Load()),
                                    attr='_convert_to_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='picking_landed_cost_4', ctx=Load()),
                                        attr='_cache',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_landed_cost_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.picking', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='picking_landed_cost_3', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=1.0, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_3', ctx=Load()),
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
                                    value=Name(id='picking_landed_cost_3', ctx=Load()),
                                    attr='action_assign',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_3', ctx=Load()),
                                    attr='_action_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='virtual_interior_design', ctx=Store())],
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Virtual Interior Design', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_vals', ctx=Store())],
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
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='fields_get',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='default_vals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='picking_ids', kind=None),
                                            Constant(value='account_journal_id', kind=None),
                                            Constant(value='cost_lines', kind=None),
                                            Constant(value='valuation_adjustment_lines', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='picking_landed_cost_3', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='expenses_journal',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='product_id', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='virtual_interior_design', ctx=Load()),
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
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='stock_landed_cost_2', ctx=Store())],
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
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='onchange_product_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='equal split', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='split_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='equal', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=15, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost_2', ctx=Load()),
                                    attr='_convert_to_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='_cache',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stock_landed_cost_2', ctx=Store())],
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
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost_2', ctx=Load()),
                                    attr='compute_landed_cost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='valuation', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='stock_landed_cost_2', ctx=Load()),
                                attr='valuation_adjustment_lines',
                                ctx=Load(),
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
                                            Attribute(
                                                value=Name(id='valuation', ctx=Load()),
                                                attr='additional_landed_cost',
                                                ctx=Load(),
                                            ),
                                            Constant(value=15, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost_2', ctx=Load()),
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
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='done', kind=None),
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
                                        value=Name(id='stock_landed_cost_2', ctx=Load()),
                                        attr='account_move_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='picking_landed_cost_4', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value=17.0, kind=None),
                                op=Div(),
                                right=Constant(value=12.0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_4', ctx=Load()),
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
                                    value=Name(id='picking_landed_cost_4', ctx=Load()),
                                    attr='action_assign',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='picking_landed_cost_4', ctx=Load()),
                                    attr='_action_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default_vals', ctx=Store())],
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
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
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
                                                    attr='fields_get',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='default_vals', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='picking_ids', kind=None),
                                            Constant(value='account_journal_id', kind=None),
                                            Constant(value='cost_lines', kind=None),
                                            Constant(value='valuation_adjustment_lines', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='picking_landed_cost_4', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='expenses_journal',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[Constant(value='product_id', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='virtual_interior_design', ctx=Load()),
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
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='stock_landed_cost_3', ctx=Store())],
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
                                    attr='new',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='onchange_product_id',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='equal split', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='split_method',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='equal', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='cost_lines',
                                        ctx=Load(),
                                    ),
                                    attr='price_unit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=11, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost_3', ctx=Load()),
                                    attr='_convert_to_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='_cache',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stock_landed_cost_3', ctx=Store())],
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
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost_3', ctx=Load()),
                                    attr='compute_landed_cost',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='valuation', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='stock_landed_cost_3', ctx=Load()),
                                attr='valuation_adjustment_lines',
                                ctx=Load(),
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
                                            Attribute(
                                                value=Name(id='valuation', ctx=Load()),
                                                attr='additional_landed_cost',
                                                ctx=Load(),
                                            ),
                                            Constant(value=11, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stock_landed_cost_3', ctx=Load()),
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
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='state',
                                        ctx=Load(),
                                    ),
                                    Constant(value='done', kind=None),
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
                                        value=Name(id='stock_landed_cost_3', ctx=Load()),
                                        attr='account_move_id',
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
                FunctionDef(
                    name='test_stock_landed_costs_rounding_02',
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
                            value=Constant(value=' The landed costs should be correctly computed, even when the decimal accuracy\n        of the deciaml price is increased. ', kind=None),
                        ),
                        Assign(
                            targets=[
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
                                        args=[Constant(value='product.decimal_price', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='digits',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=4, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fifo_pc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='parent_id', kind=None),
                                            Constant(value='property_valuation', kind=None),
                                            Constant(value='property_cost_method', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Fifo Category', kind=None),
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
                                                    args=[Constant(value='product.product_category_all', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='real_time', kind=None),
                                            Constant(value='fifo', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Product',
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
                                                Constant(value='categ_id', kind=None),
                                                Constant(value='type', kind=None),
                                                Constant(value='standard_price', kind=None),
                                            ],
                                            values=[
                                                BinOp(
                                                    left=Constant(value='Super Product %s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='price', ctx=Load()),
                                                ),
                                                Attribute(
                                                    value=Name(id='fifo_pc', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='product', kind=None),
                                                Name(id='price', ctx=Load()),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='price', ctx=Store()),
                                                iter=List(
                                                    elts=[
                                                        Constant(value=0.91, kind=None),
                                                        Constant(value=0.93, kind=None),
                                                        Constant(value=75.17, kind=None),
                                                        Constant(value=20.54, kind=None),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='landed_product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Product',
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
                                            Constant(value='landed_cost_ok', kind=None),
                                            Constant(value='split_method_landed_cost', kind=None),
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Landed Costs', kind=None),
                                            Constant(value='service', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value='by_quantity', kind=None),
                                            Constant(value=1000.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='order_line', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='product_id', kind=None),
                                                                Constant(value='product_qty', kind=None),
                                                                Constant(value='price_unit', kind=None),
                                                            ],
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='qty', ctx=Load()),
                                                                Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='standard_price',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='product', ctx=Store()),
                                                                Name(id='qty', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Name(id='zip', ctx=Load()),
                                                            args=[
                                                                Name(id='products', ctx=Load()),
                                                                List(
                                                                    elts=[
                                                                        Constant(value=6, kind=None),
                                                                        Constant(value=6, kind=None),
                                                                        Constant(value=3, kind=None),
                                                                        Constant(value=6, kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po', ctx=Load()),
                                    attr='button_confirm',
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
                                        value=Name(id='po', ctx=Load()),
                                        attr='picking_ids',
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
                            targets=[Name(id='validate_wizard', ctx=Store())],
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
                                    value=Name(id='validate_wizard', ctx=Load()),
                                    attr='process',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lc_form', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='LandedCost',
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
                                    value=Attribute(
                                        value=Name(id='lc_form', ctx=Load()),
                                        attr='picking_ids',
                                        ctx=Load(),
                                    ),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='po', ctx=Load()),
                                        attr='picking_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='lc_form', ctx=Load()),
                                                attr='cost_lines',
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
                                    value=Name(id='landed_product', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lc_form', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='lc', ctx=Load()),
                                                        attr='valuation_adjustment_lines',
                                                        ctx=Load(),
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='additional_landed_cost', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=1000.0, kind=None),
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
