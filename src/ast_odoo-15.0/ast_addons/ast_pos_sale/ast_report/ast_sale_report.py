Module(
    body=[
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
            name='SaleReport',
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
                    value=Constant(value='sale.report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_done_states',
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
                            targets=[Name(id='done_states', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='SaleReport', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_done_states',
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
                                    value=Name(id='done_states', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='pos_done', kind=None),
                                            Constant(value='invoiced', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='done_states', ctx=Load()),
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
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='pos_draft', kind=None),
                                                Constant(value='New', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='paid', kind=None),
                                                Constant(value='Paid', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='pos_done', kind=None),
                                                Constant(value='Posted', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='invoiced', kind=None),
                                                Constant(value='Invoiced', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Status', kind=None),
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
                    name='_select_pos',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fields', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='select_', ctx=Store())],
                            value=Constant(value="\n            MIN(l.id) AS id,\n            l.product_id AS product_id,\n            t.uom_id AS product_uom,\n            sum(l.qty) AS product_uom_qty,\n            sum(l.qty) AS qty_delivered,\n            0 as qty_to_deliver,\n            CASE WHEN pos.state = 'invoiced' THEN sum(l.qty) ELSE 0 END AS qty_invoiced,\n            CASE WHEN pos.state != 'invoiced' THEN sum(l.qty) ELSE 0 END AS qty_to_invoice,\n            SUM(l.price_subtotal_incl) / MIN(CASE COALESCE(pos.currency_rate, 0) WHEN 0 THEN 1.0 ELSE pos.currency_rate END) AS price_total,\n            SUM(l.price_subtotal) / MIN(CASE COALESCE(pos.currency_rate, 0) WHEN 0 THEN 1.0 ELSE pos.currency_rate END) AS price_subtotal,\n            (CASE WHEN pos.state != 'invoiced' THEN SUM(l.price_subtotal_incl) ELSE 0 END) / MIN(CASE COALESCE(pos.currency_rate, 0) WHEN 0 THEN 1.0 ELSE pos.currency_rate END) AS amount_to_invoice,\n            (CASE WHEN pos.state = 'invoiced' THEN SUM(l.price_subtotal_incl) ELSE 0 END) / MIN(CASE COALESCE(pos.currency_rate, 0) WHEN 0 THEN 1.0 ELSE pos.currency_rate END) AS amount_invoiced,\n            count(*) AS nbr,\n            pos.name AS name,\n            pos.date_order AS date,\n            CASE WHEN pos.state = 'draft' THEN 'pos_draft' WHEN pos.state = 'done' THEN 'pos_done' else pos.state END AS state,\n            pos.partner_id AS partner_id,\n            pos.user_id AS user_id,\n            pos.company_id AS company_id,\n            NULL AS campaign_id,\n            NULL AS medium_id,\n            NULL AS source_id,\n            extract(epoch from avg(date_trunc('day',pos.date_order)-date_trunc('day',pos.create_date)))/(24*60*60)::decimal(16,2) AS delay,\n            t.categ_id AS categ_id,\n            pos.pricelist_id AS pricelist_id,\n            NULL AS analytic_account_id,\n            pos.crm_team_id AS team_id,\n            p.product_tmpl_id,\n            partner.country_id AS country_id,\n            partner.industry_id AS industry_id,\n            partner.commercial_partner_id AS commercial_partner_id,\n            (sum(t.weight) * l.qty / u.factor) AS weight,\n            (sum(t.volume) * l.qty / u.factor) AS volume,\n            l.discount as discount,\n            sum((l.price_unit * l.discount * l.qty / 100.0 / CASE COALESCE(pos.currency_rate, 0) WHEN 0 THEN 1.0 ELSE pos.currency_rate END)) as discount_amount,\n            NULL as order_id\n        ", kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='fields', ctx=Load()),
                                    attr='keys',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='select_', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Constant(value=', NULL AS %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='field', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='select_', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_from_pos',
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
                            targets=[Name(id='from_', ctx=Store())],
                            value=Constant(value='\n            pos_order_line l\n                  join pos_order pos on (l.order_id=pos.id)\n                  left join res_partner partner ON (pos.partner_id = partner.id OR pos.partner_id = NULL)\n                    left join product_product p on (l.product_id=p.id)\n                    left join product_template t on (p.product_tmpl_id=t.id)\n                    LEFT JOIN uom_uom u ON (u.id=t.uom_id)\n                    LEFT JOIN pos_session session ON (session.id = pos.session_id)\n                    LEFT JOIN pos_config config ON (config.id = session.config_id)\n                left join product_pricelist pp on (pos.pricelist_id = pp.id)\n        ', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='from_', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_where_pos',
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
                            targets=[Name(id='where_', ctx=Store())],
                            value=Constant(value='l.sale_order_line_id is NULL', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='where_', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_group_by_pos',
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
                            targets=[Name(id='groupby_', ctx=Store())],
                            value=Constant(value='\n            l.order_id,\n            l.product_id,\n            l.price_unit,\n            l.discount,\n            l.qty,\n            t.uom_id,\n            t.categ_id,\n            pos.name,\n            pos.date_order,\n            pos.partner_id,\n            pos.user_id,\n            pos.state,\n            pos.company_id,\n            pos.pricelist_id,\n            p.product_tmpl_id,\n            partner.country_id,\n            partner.industry_id,\n            partner.commercial_partner_id,\n            u.factor,\n            pos.crm_team_id\n        ', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='groupby_', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_query',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='with_clause', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='from_clause', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='', kind=None),
                            Constant(value='', kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='fields', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fields', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_query',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='with_clause', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                    Name(id='from_clause', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='(SELECT %s FROM %s WHERE %s GROUP BY %s)', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_select_pos',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='fields', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_from_pos',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_where_pos',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_group_by_pos',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s UNION ALL %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='res', ctx=Load()),
                                        Name(id='current', ctx=Load()),
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
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
