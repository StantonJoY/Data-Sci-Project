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
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ResConfigSettings',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_product_expiry', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Expiration Dates', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Track following dates on lots & serial numbers: best before, removal, end of life, alert. \n Such dates are set automatically at lot/serial number creation based on values set on the product (in days).', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_production_lot', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lots & Serial Numbers', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_production_lot', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_lot_on_delivery_slip', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Display Lots & Serial Numbers on Delivery Slips', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_lot_on_delivery_slip', kind=None),
                            ),
                            keyword(
                                arg='group',
                                value=Constant(value='base.group_user,base.group_portal', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_tracking_lot', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Packages', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_tracking_lot', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_tracking_owner', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Consignment', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_tracking_owner', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_adv_location', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Multi-Step Routes', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_adv_location', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Add and customize route operations to process product moves in your warehouse(s): e.g. unload > quality control > stock for incoming products, pick > pack > ship for outgoing products. \n You can also set putaway strategies on warehouse locations in order to send incoming products into specific child locations straight away (e.g. specific bins, racks).', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_warning_stock', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Warnings for Stock', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_warning_stock', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_sign_delivery', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Signature', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_stock_sign_delivery', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_stock_picking_batch', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Batch Transfers', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_picking_wave', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Wave Transfers', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_stock_picking_wave', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Group your move operations in wave transfer to process them together', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_stock_barcode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Barcode Scanner', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_move_email_validation', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.stock_move_email_validation', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_mail_confirmation_template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.stock_mail_confirmation_template_id', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_stock_sms', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='SMS Confirmation', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Delivery Methods', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_dhl', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='DHL USA Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_fedex', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='FedEx Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_ups', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='UPS Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_usps', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='USPS Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_bpost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='bpost Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_easypost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Easypost Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_quality_control', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quality', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_quality_control_worksheet', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quality Worksheet', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_multi_locations', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Storage Locations', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_stock_multi_locations', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Store products in specific locations of your warehouse (e.g. bins, racks) and to track inventory accordingly.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_storage_categories', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Storage Categories', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_stock_storage_categories', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='annual_inventory_month', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.annual_inventory_month', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='annual_inventory_day', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.annual_inventory_day', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_reception_report', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reception Report', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_reception_report', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_stock_auto_reception_report', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Show Reception Report at Validation', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='stock.group_auto_reception_report', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_group_stock_multi_locations',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='group_stock_multi_locations',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_stock_adv_location',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_stock_storage_categories',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='group_stock_multi_locations', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_group_stock_production_lot',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='group_stock_production_lot',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_lot_on_delivery_slip',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='group_stock_production_lot', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_adv_location',
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_stock_adv_location',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_stock_multi_locations',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_stock_multi_locations',
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='group_stock_adv_location', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='set_values',
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
                            targets=[Name(id='warehouse_grp', ctx=Store())],
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
                                args=[Constant(value='stock.group_stock_multi_warehouses', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='location_grp', ctx=Store())],
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
                                args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_user', ctx=Store())],
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
                                args=[Constant(value='base.group_user', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_stock_multi_locations',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Compare(
                                        left=Name(id='location_grp', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='base_user', ctx=Load()),
                                                attr='implied_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Name(id='warehouse_grp', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='base_user', ctx=Load()),
                                                attr='implied_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="You can't desactivate the multi-location if you have more than once warehouse by company", kind=None)],
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
                        Assign(
                            targets=[Name(id='storage_cate_grp', ctx=Store())],
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
                                args=[Constant(value='stock.group_stock_storage_categories', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='PutawayRule', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.putaway.rule', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_stock_storage_categories',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='storage_cate_grp', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='base_user', ctx=Load()),
                                                attr='implied_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='putaway_rules', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='PutawayRule', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='active', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='storage_category_id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
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
                                            value=Name(id='putaway_rules', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='active', kind=None)],
                                                values=[Constant(value=True, kind=None)],
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
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='group_stock_storage_categories',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Name(id='storage_cate_grp', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='base_user', ctx=Load()),
                                                        attr='implied_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='putaway_rules', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='PutawayRule', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='storage_category_id', kind=None),
                                                                    Constant(value='!=', kind=None),
                                                                    Constant(value=False, kind=None),
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
                                                    value=Name(id='putaway_rules', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[Constant(value=False, kind=None)],
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
                        Assign(
                            targets=[Name(id='previous_group', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='group_stock_multi_locations', kind=None),
                                            Constant(value='group_stock_production_lot', kind=None),
                                            Constant(value='group_stock_tracking_lot', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResConfigSettings', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='set_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='stock.group_stock_manager', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='warehouse_obj', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.warehouse', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='group_stock_multi_locations',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='previous_group', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='group_stock_multi_locations', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='warehouse_obj', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='active_test',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[List(elts=[], ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='int_type_id', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='active', kind=None)],
                                                values=[Constant(value=True, kind=None)],
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
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='group_stock_multi_locations',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='previous_group', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='group_stock_multi_locations', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='warehouse_obj', ctx=Load()),
                                                                    attr='search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='reception_steps', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='one_step', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='delivery_steps', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='ship_only', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='int_type_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='active', kind=None)],
                                                        values=[Constant(value=False, kind=None)],
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
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=BoolOp(
                                            op=And(),
                                            values=[
                                                Subscript(
                                                    value=Name(id='self', ctx=Load()),
                                                    slice=Name(id='group', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='prev_value', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='group', ctx=Store()),
                                                        Name(id='prev_value', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='previous_group', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
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
                                    targets=[Name(id='picking_types', ctx=Store())],
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
                                                        slice=Constant(value='stock.picking.type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='code', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value='incoming', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='show_operations', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='picking_types', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='show_operations', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
