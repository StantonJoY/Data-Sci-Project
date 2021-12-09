Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ReportStockQuantity',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.stock.quantity', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock Quantity Report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_tmpl_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.template', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
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
                                            Constant(value='forecast', kind=None),
                                            Constant(value='Forecasted Stock', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='in', kind=None),
                                            Constant(value='Forecasted Receipts', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='out', kind=None),
                                            Constant(value='Forecasted Deliveries', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='State', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_qty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Quantity', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='stock.move', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='warehouse_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='stock.warehouse', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                                    value=Name(id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    Constant(value='report_stock_quantity', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value="\nCREATE or REPLACE VIEW report_stock_quantity AS (\nSELECT\n    MIN(id) as id,\n    product_id,\n    product_tmpl_id,\n    state,\n    date,\n    sum(product_qty) as product_qty,\n    company_id,\n    warehouse_id\nFROM (SELECT\n        m.id,\n        m.product_id,\n        pt.id as product_tmpl_id,\n        CASE\n            WHEN whs.id IS NOT NULL AND whd.id IS NULL THEN 'out'\n            WHEN whd.id IS NOT NULL AND whs.id IS NULL THEN 'in'\n        END AS state,\n        m.date::date AS date,\n        CASE\n            WHEN whs.id IS NOT NULL AND whd.id IS NULL THEN -m.product_qty\n            WHEN whd.id IS NOT NULL AND whs.id IS NULL THEN m.product_qty\n        END AS product_qty,\n        m.company_id,\n        CASE\n            WHEN whs.id IS NOT NULL AND whd.id IS NULL THEN whs.id\n            WHEN whd.id IS NOT NULL AND whs.id IS NULL THEN whd.id\n        END AS warehouse_id\n    FROM\n        stock_move m\n    LEFT JOIN stock_location ls on (ls.id=m.location_id)\n    LEFT JOIN stock_location ld on (ld.id=m.location_dest_id)\n    LEFT JOIN stock_warehouse whs ON ls.parent_path like concat('%/', whs.view_location_id, '/%')\n    LEFT JOIN stock_warehouse whd ON ld.parent_path like concat('%/', whd.view_location_id, '/%')\n    LEFT JOIN product_product pp on pp.id=m.product_id\n    LEFT JOIN product_template pt on pt.id=pp.product_tmpl_id\n    WHERE\n        pt.type = 'product' AND\n        m.product_qty != 0 AND\n        (whs.id IS NOT NULL OR whd.id IS NOT NULL) AND\n        (whs.id IS NULL OR whd.id IS NULL OR whs.id != whd.id) AND\n        m.state NOT IN ('cancel', 'draft', 'done')\n    UNION ALL\n    SELECT\n        -q.id as id,\n        q.product_id,\n        pp.product_tmpl_id,\n        'forecast' as state,\n        date.*::date,\n        q.quantity as product_qty,\n        q.company_id,\n        wh.id as warehouse_id\n    FROM\n        GENERATE_SERIES((now() at time zone 'utc')::date - interval '3month',\n        (now() at time zone 'utc')::date + interval '3 month', '1 day'::interval) date,\n        stock_quant q\n    LEFT JOIN stock_location l on (l.id=q.location_id)\n    LEFT JOIN stock_warehouse wh ON l.parent_path like concat('%/', wh.view_location_id, '/%')\n    LEFT JOIN product_product pp on pp.id=q.product_id\n    WHERE\n        (l.usage = 'internal' AND wh.id IS NOT NULL) OR\n        l.usage = 'transit'\n    UNION ALL\n    SELECT\n        m.id,\n        m.product_id,\n        pt.id as product_tmpl_id,\n        'forecast' as state,\n        GENERATE_SERIES(\n        CASE\n            WHEN m.state = 'done' THEN (now() at time zone 'utc')::date - interval '3month'\n            ELSE m.date::date\n        END,\n        CASE\n            WHEN m.state != 'done' THEN (now() at time zone 'utc')::date + interval '3 month'\n            ELSE m.date::date - interval '1 day'\n        END, '1 day'::interval)::date date,\n        CASE\n            WHEN whs.id IS NOT NULL AND whd.id IS NULL AND m.state = 'done' THEN m.product_qty\n            WHEN whd.id IS NOT NULL AND whs.id IS NULL AND m.state = 'done' THEN -m.product_qty\n            WHEN whs.id IS NOT NULL AND whd.id IS NULL THEN -m.product_qty\n            WHEN whd.id IS NOT NULL AND whs.id IS NULL THEN m.product_qty\n        END AS product_qty,\n        m.company_id,\n        CASE\n            WHEN whs.id IS NOT NULL AND whd.id IS NULL THEN whs.id\n            WHEN whd.id IS NOT NULL AND whs.id IS NULL THEN whd.id\n        END AS warehouse_id\n    FROM\n        stock_move m\n    LEFT JOIN stock_location ls on (ls.id=m.location_id)\n    LEFT JOIN stock_location ld on (ld.id=m.location_dest_id)\n    LEFT JOIN stock_warehouse whs ON ls.parent_path like concat('%/', whs.view_location_id, '/%')\n    LEFT JOIN stock_warehouse whd ON ld.parent_path like concat('%/', whd.view_location_id, '/%')\n    LEFT JOIN product_product pp on pp.id=m.product_id\n    LEFT JOIN product_template pt on pt.id=pp.product_tmpl_id\n    WHERE\n        pt.type = 'product' AND\n        m.product_qty != 0 AND\n        (whs.id IS NOT NULL OR whd.id IS NOT NULL) AND\n        (whs.id IS NULL or whd.id IS NULL OR whs.id != whd.id) AND\n        m.state NOT IN ('cancel', 'draft')) as forecast_qty\nGROUP BY product_id, product_tmpl_id, state, date, company_id, warehouse_id\n);\n", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Name(id='query', ctx=Load())],
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
