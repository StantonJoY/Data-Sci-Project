Module(
    body=[
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='FleetReport',
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
                    value=Constant(value='fleet.vehicle.cost.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Fleet Analysis Report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='date_start desc', kind=None),
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
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='Company', kind=None),
                        ],
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
                    targets=[Name(id='vehicle_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='fleet.vehicle', kind=None),
                            Constant(value='Vehicle', kind=None),
                        ],
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
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Vehicle Name', kind=None)],
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
                    targets=[Name(id='driver_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='Driver', kind=None),
                        ],
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
                    targets=[Name(id='fuel_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Fuel', kind=None)],
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
                    targets=[Name(id='date_start', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Date', kind=None)],
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
                    targets=[Name(id='vehicle_type', ctx=Store())],
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
                                            Constant(value='car', kind=None),
                                            Constant(value='Car', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='bike', kind=None),
                                            Constant(value='Bike', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
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
                    targets=[Name(id='cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Cost', kind=None)],
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
                    targets=[Name(id='cost_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Cost Type', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='contract', kind=None),
                                                Constant(value='Contract', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='service', kind=None),
                                                Constant(value='Service', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
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
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value="\nWITH service_costs AS (\n    SELECT\n        ve.id AS vehicle_id,\n        ve.company_id AS company_id,\n        ve.name AS name,\n        ve.driver_id AS driver_id,\n        ve.fuel_type AS fuel_type,\n        date(date_trunc('month', d)) AS date_start,\n        vem.vehicle_type as vehicle_type,\n        COALESCE(sum(se.amount), 0) AS\n        COST,\n        'service' AS cost_type\n    FROM\n        fleet_vehicle ve\n    JOIN\n        fleet_vehicle_model vem ON vem.id = ve.model_id\n    CROSS JOIN generate_series((\n            SELECT\n                min(date)\n                FROM fleet_vehicle_log_services), CURRENT_DATE + '1 month'::interval, '1 month') d\n        LEFT JOIN fleet_vehicle_log_services se ON se.vehicle_id = ve.id\n            AND date_trunc('month', se.date) = date_trunc('month', d)\n    WHERE\n        ve.active AND se.active AND se.state != 'cancelled'\n    GROUP BY\n        ve.id,\n        ve.company_id,\n        vem.vehicle_type,\n        ve.name,\n        date_start,\n        d\n    ORDER BY\n        ve.id,\n        date_start\n),\ncontract_costs AS (\n    SELECT\n        ve.id AS vehicle_id,\n        ve.company_id AS company_id,\n        ve.name AS name,\n        ve.driver_id AS driver_id,\n        ve.fuel_type AS fuel_type,\n        date(date_trunc('month', d)) AS date_start,\n        vem.vehicle_type as vehicle_type,\n        (COALESCE(sum(co.amount), 0) + COALESCE(sum(cod.cost_generated * extract(day FROM least (date_trunc('month', d) + interval '1 month', cod.expiration_date) - greatest (date_trunc('month', d), cod.start_date))), 0) + COALESCE(sum(com.cost_generated), 0) + COALESCE(sum(coy.cost_generated), 0)) AS\n        COST,\n        'contract' AS cost_type\n    FROM\n        fleet_vehicle ve\n    JOIN\n        fleet_vehicle_model vem ON vem.id = ve.model_id\n    CROSS JOIN generate_series((\n            SELECT\n                min(acquisition_date)\n                FROM fleet_vehicle), CURRENT_DATE + '1 month'::interval, '1 month') d\n        LEFT JOIN fleet_vehicle_log_contract co ON co.vehicle_id = ve.id\n            AND date_trunc('month', co.date) = date_trunc('month', d)\n        LEFT JOIN fleet_vehicle_log_contract cod ON cod.vehicle_id = ve.id\n            AND date_trunc('month', cod.start_date) <= date_trunc('month', d)\n            AND date_trunc('month', cod.expiration_date) >= date_trunc('month', d)\n            AND cod.cost_frequency = 'daily'\n    LEFT JOIN fleet_vehicle_log_contract com ON com.vehicle_id = ve.id\n        AND date_trunc('month', com.start_date) <= date_trunc('month', d)\n        AND date_trunc('month', com.expiration_date) >= date_trunc('month', d)\n        AND com.cost_frequency = 'monthly'\n    LEFT JOIN fleet_vehicle_log_contract coy ON coy.vehicle_id = ve.id\n        AND date_trunc('month', coy.date) = date_trunc('month', d)\n        AND date_trunc('month', coy.start_date) <= date_trunc('month', d)\n        AND date_trunc('month', coy.expiration_date) >= date_trunc('month', d)\n        AND coy.cost_frequency = 'yearly'\n    WHERE\n        ve.active\n    GROUP BY\n        ve.id,\n        ve.company_id,\n        vem.vehicle_type,\n        ve.name,\n        date_start,\n        d\n    ORDER BY\n        ve.id,\n        date_start\n)\nSELECT\n    vehicle_id AS id,\n    company_id,\n    vehicle_id,\n    name,\n    driver_id,\n    fuel_type,\n    date_start,\n    vehicle_type,\n    COST,\n    'service' as cost_type\nFROM\n    service_costs sc\nUNION ALL (\n    SELECT\n        vehicle_id AS id,\n        company_id,\n        vehicle_id,\n        name,\n        driver_id,\n        fuel_type,\n        date_start,\n        vehicle_type,\n        COST,\n        'contract' as cost_type\n    FROM\n        contract_costs cc)\n", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='drop_view_if_exists',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_table',
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
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='CREATE or REPLACE VIEW {} as ({})', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='Identifier',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_table',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='sql', ctx=Load()),
                                                    attr='SQL',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='query', ctx=Load())],
                                                keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
