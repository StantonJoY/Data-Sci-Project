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
            name='ProfitabilityAnalysis',
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
                    value=Constant(value='project.profitability.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Project Profitability Report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='project_id, sale_line_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='analytic_account_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.analytic.account', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Analytic Account', kind=None),
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
                    targets=[Name(id='project_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.project', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Project', kind=None),
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
                    targets=[Name(id='task_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='project.task', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Task', kind=None),
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
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.currency', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Project Currency', kind=None),
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
                                arg='string',
                                value=Constant(value='Project Company', kind=None),
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
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Project Manager', kind=None),
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
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.partner', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Customer', kind=None),
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
                    targets=[Name(id='line_date', ctx=Store())],
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
                    targets=[Name(id='timesheet_unit_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Timesheet Duration', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='timesheet_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Timesheet Cost', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expense_cost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Other Costs', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='order_confirmation_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sales Order Confirmation Date', kind=None)],
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
                    targets=[Name(id='sale_line_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sale.order.line', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sale Order Line', kind=None),
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
                    targets=[Name(id='sale_order_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sale.order', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Sale Order', kind=None),
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
                    targets=[Name(id='amount_untaxed_to_invoice', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Amount to Invoice', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount_untaxed_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Amount Invoiced', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expense_amount_untaxed_to_invoice', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Amount to Re-invoice', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='expense_amount_untaxed_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Amount Re-invoiced', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='other_revenues', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Other Revenues', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='All revenues that are not from timesheets and that are linked to the analytic account of the project.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Margin', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Tuple(
                                    elts=[
                                        Constant(value=16, kind=None),
                                        Constant(value=2, kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='group_operator',
                                value=Constant(value='sum', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_depends', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='sale.order.line', kind=None),
                            Constant(value='sale.order', kind=None),
                        ],
                        values=[
                            List(
                                elts=[
                                    Constant(value='order_id', kind=None),
                                    Constant(value='invoice_status', kind=None),
                                    Constant(value='price_reduce', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='qty_invoiced', kind=None),
                                    Constant(value='untaxed_amount_invoiced', kind=None),
                                    Constant(value='untaxed_amount_to_invoice', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='is_downpayment', kind=None),
                                    Constant(value='project_id', kind=None),
                                    Constant(value='task_id', kind=None),
                                    Constant(value='qty_delivered_method', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            List(
                                elts=[
                                    Constant(value='date_order', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='currency_id', kind=None),
                                    Constant(value='analytic_account_id', kind=None),
                                    Constant(value='order_line', kind=None),
                                    Constant(value='invoice_status', kind=None),
                                    Constant(value='amount_untaxed', kind=None),
                                    Constant(value='currency_rate', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='project_id', kind=None),
                                ],
                                ctx=Load(),
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_table',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=BinOp(
                                left=Constant(value="\n            CREATE VIEW %s AS (\n                SELECT\n                    sub.id as id,\n                    sub.project_id as project_id,\n                    sub.task_id as task_id,\n                    sub.user_id as user_id,\n                    sub.sale_line_id as sale_line_id,\n                    sub.analytic_account_id as analytic_account_id,\n                    sub.partner_id as partner_id,\n                    sub.company_id as company_id,\n                    sub.currency_id as currency_id,\n                    sub.sale_order_id as sale_order_id,\n                    sub.order_confirmation_date as order_confirmation_date,\n                    sub.product_id as product_id,\n                    sub.sale_qty_delivered_method as sale_qty_delivered_method,\n                    sub.expense_amount_untaxed_to_invoice as expense_amount_untaxed_to_invoice,\n                    sub.expense_amount_untaxed_invoiced as expense_amount_untaxed_invoiced,\n                    sub.amount_untaxed_to_invoice as amount_untaxed_to_invoice,\n                    sub.amount_untaxed_invoiced as amount_untaxed_invoiced,\n                    sub.timesheet_unit_amount as timesheet_unit_amount,\n                    sub.timesheet_cost as timesheet_cost,\n                    sub.expense_cost as expense_cost,\n                    sub.other_revenues as other_revenues,\n                    sub.line_date as line_date,\n                    (sub.expense_amount_untaxed_to_invoice + sub.expense_amount_untaxed_invoiced + sub.amount_untaxed_to_invoice +\n                        sub.amount_untaxed_invoiced + sub.other_revenues + sub.timesheet_cost + sub.expense_cost)\n                        as margin\n                FROM (\n                    SELECT\n                        ROW_NUMBER() OVER (ORDER BY P.id, SOL.id) AS id,\n                        P.id AS project_id,\n                        P.user_id AS user_id,\n                        SOL.id AS sale_line_id,\n                        SOL.task_id AS task_id,\n                        P.analytic_account_id AS analytic_account_id,\n                        P.partner_id AS partner_id,\n                        C.id AS company_id,\n                        C.currency_id AS currency_id,\n                        S.id AS sale_order_id,\n                        S.date_order AS order_confirmation_date,\n                        SOL.product_id AS product_id,\n                        SOL.qty_delivered_method AS sale_qty_delivered_method,\n                        COST_SUMMARY.expense_amount_untaxed_to_invoice AS expense_amount_untaxed_to_invoice,\n                        COST_SUMMARY.expense_amount_untaxed_invoiced AS expense_amount_untaxed_invoiced,\n                        COST_SUMMARY.amount_untaxed_to_invoice AS amount_untaxed_to_invoice,\n                        COST_SUMMARY.amount_untaxed_invoiced AS amount_untaxed_invoiced,\n                        COST_SUMMARY.timesheet_unit_amount AS timesheet_unit_amount,\n                        COST_SUMMARY.timesheet_cost AS timesheet_cost,\n                        COST_SUMMARY.expense_cost AS expense_cost,\n                        COST_SUMMARY.other_revenues AS other_revenues,\n                        COST_SUMMARY.line_date::date AS line_date\n                    FROM project_project P\n                        JOIN res_company C ON C.id = P.company_id\n                        LEFT JOIN (\n                            -- Each costs and revenues will be retrieved individually by sub-requests\n                            -- This is required to able to get the date\n                            SELECT\n                                project_id,\n                                analytic_account_id,\n                                sale_line_id,\n                                SUM(timesheet_unit_amount) AS timesheet_unit_amount,\n                                SUM(timesheet_cost) AS timesheet_cost,\n                                SUM(expense_cost) AS expense_cost,\n                                SUM(other_revenues) AS other_revenues,\n                                SUM(expense_amount_untaxed_to_invoice) AS expense_amount_untaxed_to_invoice,\n                                SUM(expense_amount_untaxed_invoiced) AS expense_amount_untaxed_invoiced,\n                                SUM(amount_untaxed_to_invoice) AS amount_untaxed_to_invoice,\n                                SUM(amount_untaxed_invoiced) AS amount_untaxed_invoiced,\n                                line_date AS line_date\n                            FROM (\n                                -- Get the timesheet costs\n                                SELECT\n                                    P.id AS project_id,\n                                    P.analytic_account_id AS analytic_account_id,\n                                    TS.so_line AS sale_line_id,\n                                    TS.unit_amount AS timesheet_unit_amount,\n                                    TS.amount AS timesheet_cost,\n                                    0.0 AS other_revenues,\n                                    0.0 AS expense_cost,\n                                    0.0 AS expense_amount_untaxed_to_invoice,\n                                    0.0 AS expense_amount_untaxed_invoiced,\n                                    0.0 AS amount_untaxed_to_invoice,\n                                    0.0 AS amount_untaxed_invoiced,\n                                    TS.date AS line_date\n                                FROM account_analytic_line TS, project_project P\n                                WHERE TS.project_id IS NOT NULL AND P.id = TS.project_id AND P.active = 't' AND P.allow_timesheets = 't'\n\n                                UNION ALL\n\n                                -- Get the other revenues (products that are not services)\n                                SELECT\n                                    P.id AS project_id,\n                                    P.analytic_account_id AS analytic_account_id,\n                                    AAL.so_line AS sale_line_id,\n                                    0.0 AS timesheet_unit_amount,\n                                    0.0 AS timesheet_cost,\n                                    AAL.amount AS other_revenues,\n                                    0.0 AS expense_cost,\n                                    0.0 AS expense_amount_untaxed_to_invoice,\n                                    0.0 AS expense_amount_untaxed_invoiced,\n                                    0.0 AS amount_untaxed_to_invoice,\n                                    0.0 AS amount_untaxed_invoiced,\n                                    AAL.date AS line_date\n                                FROM project_project P\n                                    JOIN account_analytic_account AA ON P.analytic_account_id = AA.id\n                                    JOIN account_analytic_line AAL ON AAL.account_id = AA.id\n                                    LEFT JOIN sale_order_line_invoice_rel SOINV ON SOINV.invoice_line_id = AAL.move_id\n                                    LEFT JOIN sale_order_line SOL ON SOINV.order_line_id = SOL.id\n                                WHERE AAL.amount > 0.0 AND AAL.project_id IS NULL AND P.active = 't'\n                                    AND P.allow_timesheets = 't'\n                                    AND (SOL.id IS NULL\n                                        OR (SOL.is_expense IS NOT TRUE AND SOL.is_downpayment IS NOT TRUE AND SOL.is_service IS NOT TRUE))\n\n                                UNION ALL\n\n                                -- Get the expense costs from account analytic line\n                                SELECT\n                                    P.id AS project_id,\n                                    P.analytic_account_id AS analytic_account_id,\n                                    AAL.so_line AS sale_line_id,\n                                    0.0 AS timesheet_unit_amount,\n                                    0.0 AS timesheet_cost,\n                                    0.0 AS other_revenues,\n                                    AAL.amount AS expense_cost,\n                                    0.0 AS expense_amount_untaxed_to_invoice,\n                                    0.0 AS expense_amount_untaxed_invoiced,\n                                    0.0 AS amount_untaxed_to_invoice,\n                                    0.0 AS amount_untaxed_invoiced,\n                                    AAL.date AS line_date\n                                FROM project_project P\n                                    JOIN account_analytic_account AA ON P.analytic_account_id = AA.id\n                                    JOIN account_analytic_line AAL ON AAL.account_id = AA.id\n                                    LEFT JOIN account_move_line RINVL ON AAL.move_id = RINVL.id\n                                                                     AND RINVL.parent_state = 'posted'\n                                                                     AND RINVL.exclude_from_invoice_tab = 'f'\n                                    -- Check if the AAL is not related to a reversed credit note\n                                    LEFT JOIN account_move RINV ON RINV.id = RINVL.move_id\n                                    LEFT JOIN account_move_line INVL ON INVL.move_id = RINV.reversed_entry_id\n                                                                    AND INVL.parent_state = 'posted'\n                                                                    AND INVL.exclude_from_invoice_tab = 'f'\n                                                                    AND INVL.product_id = RINVL.product_id\n                                    LEFT JOIN sale_order_line_invoice_rel SOINV ON SOINV.invoice_line_id = INVL.id\n                                    LEFT JOIN sale_order_line SOL ON SOINV.order_line_id = SOL.id\n                                                                 AND SOL.product_id = AAL.product_id\n                                    -- Check if the AAL is not related to a consumed downpayment (when the SOL is fully invoiced - with downpayment discounted.)\n                                    LEFT JOIN sale_order_line_invoice_rel SOINVDOWN ON SOINVDOWN.invoice_line_id = RINVL.id\n                                    LEFT JOIN sale_order_line SOLDOWN on SOINVDOWN.order_line_id = SOLDOWN.id AND SOLDOWN.is_downpayment = 't'\n                                WHERE AAL.amount < 0.0 AND AAL.project_id IS NULL\n                                  AND SOL.id IS NULL AND SOLDOWN.id IS NULL -- Not linked to a credit note and not a downpayment\n                                  AND P.active = 't' AND P.allow_timesheets = 't'\n\n                                UNION ALL\n\n                                -- Get the following values: expense amount untaxed to invoice/invoiced, amount untaxed to invoice/invoiced\n                                -- These values have to be computed from all the records retrieved just above but grouped by project and sale order line\n                                SELECT\n                                    AMOUNT_UNTAXED.project_id AS project_id,\n                                    AMOUNT_UNTAXED.analytic_account_id AS analytic_account_id,\n                                    AMOUNT_UNTAXED.sale_line_id AS sale_line_id,\n                                    0.0 AS timesheet_unit_amount,\n                                    0.0 AS timesheet_cost,\n                                    0.0 AS other_revenues,\n                                    0.0 AS expense_cost,\n                                    CASE\n                                        WHEN SOL.qty_delivered_method = 'analytic' THEN (SOL.untaxed_amount_to_invoice / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)\n                                        ELSE 0.0\n                                    END AS expense_amount_untaxed_to_invoice,\n                                    CASE\n                                        WHEN SOL.qty_delivered_method = 'analytic' AND SOL.invoice_status = 'invoiced'\n                                        THEN\n                                            CASE\n                                                WHEN T.expense_policy = 'sales_price'\n                                                THEN (SOL.untaxed_amount_invoiced / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)\n                                                ELSE -AMOUNT_UNTAXED.expense_cost\n                                            END\n                                        ELSE 0.0\n                                    END AS expense_amount_untaxed_invoiced,\n                                    CASE\n                                        WHEN SOL.qty_delivered_method IN ('timesheet', 'manual') THEN (SOL.untaxed_amount_to_invoice / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)\n                                        ELSE 0.0\n                                    END AS amount_untaxed_to_invoice,\n                                    CASE\n                                        WHEN SOL.qty_delivered_method IN ('timesheet', 'manual') THEN (SOL.untaxed_amount_invoiced / CASE COALESCE(S.currency_rate, 0) WHEN 0 THEN 1.0 ELSE S.currency_rate END)\n                                        ELSE 0.0\n                                    END AS amount_untaxed_invoiced,\n                                    S.date_order AS line_date\n                                FROM project_project P\n                                    JOIN res_company C ON C.id = P.company_id\n                                    LEFT JOIN (\n                                        -- Gets SOL linked to timesheets\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            AAL.so_line AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM account_analytic_line AAL, project_project P\n                                        WHERE AAL.project_id IS NOT NULL AND P.id = AAL.project_id AND P.active = 't'\n                                        GROUP BY P.id, AAL.so_line\n                                        UNION\n                                        -- Service SOL linked to a project task AND not yet timesheeted\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            SOL.id AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM sale_order_line SOL\n                                        JOIN project_task T ON T.sale_line_id = SOL.id\n                                        JOIN project_project P ON T.project_id = P.id\n                                        LEFT JOIN account_analytic_line AAL ON AAL.task_id = T.id\n                                        WHERE SOL.is_service = 't'\n                                          AND AAL.id IS NULL -- not timesheeted\n                                          AND P.active = 't' AND P.allow_timesheets = 't'\n                                        GROUP BY P.id, SOL.id\n                                        UNION\n                                        -- Service SOL linked to project AND not yet timesheeted\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            SOL.id AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM sale_order_line SOL\n                                        JOIN project_project P ON P.sale_line_id = SOL.id\n                                        LEFT JOIN account_analytic_line AAL ON AAL.project_id = P.id\n                                        LEFT JOIN project_task T ON T.sale_line_id = SOL.id\n                                        WHERE SOL.is_service = 't'\n                                          AND AAL.id IS NULL -- not timesheeted\n                                          AND (T.id IS NULL OR T.project_id != P.id) -- not linked to a task in this project\n                                          AND P.active = 't' AND P.allow_timesheets = 't'\n                                        GROUP BY P.id, SOL.id\n                                        UNION\n                                        -- Service SOL linked to analytic account AND not yet timesheeted\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            SOL.id AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM sale_order_line SOL\n                                        JOIN sale_order SO ON SO.id = SOL.order_id\n                                        JOIN account_analytic_account AA ON AA.id = SO.analytic_account_id\n                                        JOIN project_project P ON P.analytic_account_id = AA.id\n                                        LEFT JOIN project_project PSOL ON PSOL.sale_line_id = SOL.id\n                                        LEFT JOIN project_task TSOL ON TSOL.sale_line_id = SOL.id\n                                        LEFT JOIN account_analytic_line AAL ON AAL.so_line = SOL.id\n                                        WHERE SOL.is_service = 't'\n                                          AND AAL.id IS NULL -- not timesheeted\n                                          AND TSOL.id IS NULL -- not linked to a task\n                                          AND PSOL.id IS NULL -- not linked to a project\n                                          AND P.active = 't' AND P.allow_timesheets = 't'\n                                        GROUP BY P.id, SOL.id\n                                        UNION\n\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            AAL.so_line AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM project_project P\n                                            LEFT JOIN account_analytic_account AA ON P.analytic_account_id = AA.id\n                                            LEFT JOIN account_analytic_line AAL ON AAL.account_id = AA.id\n                                        WHERE AAL.amount > 0.0 AND AAL.project_id IS NULL AND P.active = 't' AND P.allow_timesheets = 't'\n                                        GROUP BY P.id, AA.id, AAL.so_line\n                                        UNION\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            AAL.so_line AS sale_line_id,\n                                            SUM(AAL.amount) AS expense_cost\n                                        FROM project_project P\n                                            LEFT JOIN account_analytic_account AA ON P.analytic_account_id = AA.id\n                                            LEFT JOIN account_analytic_line AAL ON AAL.account_id = AA.id\n                                        WHERE AAL.amount < 0.0 AND AAL.project_id IS NULL AND P.active = 't' AND P.allow_timesheets = 't'\n                                        GROUP BY P.id, AA.id, AAL.so_line\n                                        UNION\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            SOLDOWN.id AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM project_project P\n                                            LEFT JOIN sale_order_line SOL ON P.sale_line_id = SOL.id\n                                            LEFT JOIN sale_order SO ON SO.id = SOL.order_id OR SO.analytic_account_id = P.analytic_account_id\n                                            LEFT JOIN sale_order_line SOLDOWN ON SOLDOWN.order_id = SO.id AND SOLDOWN.is_downpayment = 't'\n                                            LEFT JOIN sale_order_line_invoice_rel SOINV ON SOINV.order_line_id = SOLDOWN.id\n                                            LEFT JOIN account_move_line INVL ON SOINV.invoice_line_id = INVL.id\n                                                                            AND INVL.parent_state = 'posted'\n                                                                            AND INVL.exclude_from_invoice_tab = 'f'\n                                            LEFT JOIN account_move RINV ON INVL.move_id = RINV.reversed_entry_id\n                                            LEFT JOIN account_move_line RINVL ON RINV.id = RINVL.move_id\n                                                                            AND RINVL.parent_state = 'posted'\n                                                                            AND RINVL.exclude_from_invoice_tab = 'f'\n                                                                            AND RINVL.product_id = SOLDOWN.product_id\n                                            LEFT JOIN account_analytic_line ANLI ON ANLI.move_id = RINVL.id AND ANLI.amount < 0.0\n                                        WHERE ANLI.id IS NULL -- there are no credit note for this downpayment\n                                          AND P.active = 't' AND P.allow_timesheets = 't'\n                                        GROUP BY P.id, SOLDOWN.id\n                                        UNION\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            SOL.id AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM sale_order_line SOL\n                                            INNER JOIN project_project P ON SOL.project_id = P.id\n                                        WHERE P.active = 't' AND P.allow_timesheets = 't'\n                                        UNION\n                                        SELECT\n                                            P.id AS project_id,\n                                            P.analytic_account_id AS analytic_account_id,\n                                            SOL.id AS sale_line_id,\n                                            0.0 AS expense_cost\n                                        FROM sale_order_line SOL\n                                            INNER JOIN project_task T ON SOL.task_id = T.id\n                                            INNER JOIN project_project P ON P.id = T.project_id\n                                        WHERE P.active = 't' AND P.allow_timesheets = 't'\n                                    ) AMOUNT_UNTAXED ON AMOUNT_UNTAXED.project_id = P.id\n                                    LEFT JOIN sale_order_line SOL ON AMOUNT_UNTAXED.sale_line_id = SOL.id\n                                    LEFT JOIN sale_order S ON SOL.order_id = S.id\n                                    LEFT JOIN product_product PP on (SOL.product_id = PP.id)\n                                    LEFT JOIN product_template T on (PP.product_tmpl_id = T.id)\n                                    WHERE P.active = 't' AND P.analytic_account_id IS NOT NULL\n                            ) SUB_COST_SUMMARY\n                            GROUP BY project_id, analytic_account_id, sale_line_id, line_date\n                        ) COST_SUMMARY ON COST_SUMMARY.project_id = P.id\n                        LEFT JOIN sale_order_line SOL ON COST_SUMMARY.sale_line_id = SOL.id\n                        LEFT JOIN sale_order S ON SOL.order_id = S.id\n                        WHERE P.active = 't' AND P.analytic_account_id IS NOT NULL\n                    ) AS sub\n            )\n        ", kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_table',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
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
