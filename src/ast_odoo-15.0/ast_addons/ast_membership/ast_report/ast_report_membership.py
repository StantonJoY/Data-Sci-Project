Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='STATE', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='none', kind=None),
                            Constant(value='Non Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='canceled', kind=None),
                            Constant(value='Cancelled Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='old', kind=None),
                            Constant(value='Old Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='waiting', kind=None),
                            Constant(value='Waiting Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='invoiced', kind=None),
                            Constant(value='Invoiced Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='free', kind=None),
                            Constant(value='Free Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='paid', kind=None),
                            Constant(value='Paid Member', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ReportMembership',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Membership Analysis', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.membership', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Membership Analysis', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='start_date', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='start_date', ctx=Store())],
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
                                value=Constant(value='Start Date', kind=None),
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
                    targets=[Name(id='date_to', ctx=Store())],
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
                                value=Constant(value='End Date', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='End membership date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='num_waiting', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Waiting', kind=None),
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
                    targets=[Name(id='num_invoiced', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Invoiced', kind=None),
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
                    targets=[Name(id='num_paid', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='# Paid', kind=None),
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
                    targets=[Name(id='tot_pending', ctx=Store())],
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
                                value=Constant(value='Pending Amount', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value=0, kind=None),
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
                    targets=[Name(id='tot_earned', ctx=Store())],
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
                                value=Constant(value='Earned Amount', kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value=0, kind=None),
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
                                value=Constant(value='Member', kind=None),
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
                    targets=[Name(id='associate_member_id', ctx=Store())],
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
                                value=Constant(value='Associate Member', kind=None),
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
                    targets=[Name(id='membership_id', ctx=Store())],
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
                                value=Constant(value='Membership Product', kind=None),
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
                    targets=[Name(id='membership_state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='STATE', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Current Membership State', kind=None),
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
                                value=Constant(value='Salesperson', kind=None),
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
                                value=Constant(value='Company', kind=None),
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
                    targets=[Name(id='quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
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
                            value=Constant(value='Create the view', kind=None),
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
                                args=[
                                    BinOp(
                                        left=Constant(value="\n        CREATE OR REPLACE VIEW %s AS (\n        SELECT\n        MIN(id) AS id,\n        partner_id,\n        count(membership_id) as quantity,\n        user_id,\n        membership_state,\n        associate_member_id,\n        membership_amount,\n        date_to,\n        start_date,\n        COUNT(num_waiting) AS num_waiting,\n        COUNT(num_invoiced) AS num_invoiced,\n        COUNT(num_paid) AS num_paid,\n        SUM(tot_pending) AS tot_pending,\n        SUM(tot_earned) AS tot_earned,\n        membership_id,\n        company_id\n        FROM\n        (SELECT\n            MIN(p.id) AS id,\n            p.id AS partner_id,\n            p.user_id AS user_id,\n            p.membership_state AS membership_state,\n            p.associate_member AS associate_member_id,\n            p.membership_amount AS membership_amount,\n            p.membership_stop AS date_to,\n            p.membership_start AS start_date,\n            CASE WHEN ml.state = 'waiting'  THEN ml.id END AS num_waiting,\n            CASE WHEN ml.state = 'invoiced' THEN ml.id END AS num_invoiced,\n            CASE WHEN ml.state = 'paid'     THEN ml.id END AS num_paid,\n            CASE WHEN ml.state IN ('waiting', 'invoiced') THEN SUM(aml.price_subtotal) ELSE 0 END AS tot_pending,\n            CASE WHEN ml.state = 'paid' OR p.membership_state = 'old' THEN SUM(aml.price_subtotal) ELSE 0 END AS tot_earned,\n            ml.membership_id AS membership_id,\n            p.company_id AS company_id\n            FROM res_partner p\n            LEFT JOIN membership_membership_line ml ON (ml.partner = p.id)\n            LEFT JOIN account_move_line aml ON (ml.account_invoice_line = aml.id)\n            LEFT JOIN account_move am ON (aml.move_id = am.id)\n            WHERE p.membership_state != 'none' and p.active = 'true'\n            GROUP BY\n              p.id,\n              p.user_id,\n              p.membership_state,\n              p.associate_member,\n              p.membership_amount,\n              p.membership_start,\n              ml.membership_id,\n              p.company_id,\n              ml.state,\n              ml.id\n        ) AS foo\n        GROUP BY\n            start_date,\n            date_to,\n            partner_id,\n            user_id,\n            membership_id,\n            company_id,\n            membership_state,\n            associate_member_id,\n            membership_amount\n        )", kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
