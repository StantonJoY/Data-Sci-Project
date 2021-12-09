Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Datetime', asname='FieldDateTime')],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='AND', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountClosing',
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
                    value=Constant(value='\n    This object holds an interval total and a grand total of the accounts of type receivable for a company,\n    as well as the last account_move that has been counted in a previous object\n    It takes its earliest brother to infer from when the computation needs to be done\n    in order to compute its own data.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='account.sale.closing', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='date_closing_stop desc, sequence_number desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Sale Closing', kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Frequency and unique sequence number', kind=None),
                            ),
                            keyword(
                                arg='required',
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
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_closing_stop', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Closing Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Date to which the values are computed', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date_closing_start', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Starting Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Date from which the total interval is computed', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='frequency', ctx=Store())],
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
                                value=Constant(value='Closing Type', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='daily', kind=None),
                                                Constant(value='Daily', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='monthly', kind=None),
                                                Constant(value='Monthly', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='annually', kind=None),
                                                Constant(value='Annual', kind=None),
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
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total_interval', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Period Total', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Total in receivable accounts during the interval, excluding overlapping periods', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cumulative_total', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Cumulative Grand Total', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Total in receivable accounts since the beginnig of times', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sequence #', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='last_order_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='pos.order', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Last Pos Order', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Last Pos order included in the grand total', kind=None),
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
                    targets=[Name(id='last_order_hash', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value="Last Order entry's inalteralbility hash", kind=None),
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
                                value=Constant(value='Currency', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="The company's currency", kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_query_for_aml',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='first_move_sequence_number', annotation=None, type_comment=None),
                            arg(arg='date_start', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='company_id', kind=None)],
                                values=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value="WITH aggregate AS (SELECT m.id AS move_id,\n                    aml.balance AS balance,\n                    aml.id as line_id\n            FROM account_move_line aml\n            JOIN account_journal j ON aml.journal_id = j.id\n            JOIN account_account acc ON acc.id = aml.account_id\n            JOIN account_account_type t ON (t.id = acc.user_type_id AND t.type = 'receivable')\n            JOIN account_move m ON m.id = aml.move_id\n            WHERE j.type = 'sale'\n                AND aml.company_id = %(company_id)s\n                AND m.state = 'posted' ", kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='first_move_sequence_number', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=False, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='first_move_sequence_number', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='params', ctx=Load()),
                                            slice=Constant(value='first_move_sequence_number', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='first_move_sequence_number', ctx=Load()),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='query', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='AND m.secure_sequence_number > %(first_move_sequence_number)s', kind=None),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='date_start', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='params', ctx=Load()),
                                                    slice=Constant(value='date_start', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='date_start', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='query', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value='AND m.date >= %(date_start)s', kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        AugAssign(
                            target=Name(id='query', ctx=Store()),
                            op=Add(),
                            value=Constant(value=' ORDER BY m.secure_sequence_number DESC) ', kind=None),
                        ),
                        AugAssign(
                            target=Name(id='query', ctx=Store()),
                            op=Add(),
                            value=Constant(value='SELECT array_agg(move_id) AS move_ids,\n                           array_agg(line_id) AS line_ids,\n                           sum(balance) AS balance\n                    FROM aggregate', kind=None),
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
                                    Name(id='query', ctx=Load()),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
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
                                        attr='dictfetchall',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_amounts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frequency', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Method used to compute all the business data of the new object.\n        It will search for previous closings of the same frequency to infer the move from which\n        account move lines should be fetched.\n        @param {string} frequency: a valid value of the selection field on the object (daily, monthly, annually)\n            frequencies are literal (daily means 24 hours and so on)\n        @param {recordset} company: the company for which the closing is done\n        @return {dict} containing {field: value} for each business field of the object\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='interval_dates', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_interval_dates',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='frequency', ctx=Load()),
                                    Name(id='company', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_closing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='frequency', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='frequency', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='company', ctx=Load()),
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
                                    keyword(
                                        arg='order',
                                        value=Constant(value='sequence_number desc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_order', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='pos.order', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_start', ctx=Store())],
                            value=Subscript(
                                value=Name(id='interval_dates', ctx=Load()),
                                slice=Constant(value='interval_from', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cumulative_total', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='previous_closing', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='first_order', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='previous_closing', ctx=Load()),
                                        attr='last_order_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='date_start', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='previous_closing', ctx=Load()),
                                        attr='create_date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='cumulative_total', ctx=Store()),
                                    op=Add(),
                                    value=Attribute(
                                        value=Name(id='previous_closing', ctx=Load()),
                                        attr='cumulative_total',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='paid', kind=None),
                                                    Constant(value='done', kind=None),
                                                    Constant(value='invoiced', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='first_order', ctx=Load()),
                                            attr='l10n_fr_secure_sequence_number',
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=False, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='first_order', ctx=Load()),
                                            attr='l10n_fr_secure_sequence_number',
                                            ctx=Load(),
                                        ),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='AND', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='domain', ctx=Load()),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='l10n_fr_secure_sequence_number', kind=None),
                                                                    Constant(value='>', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='first_order', ctx=Load()),
                                                                        attr='l10n_fr_secure_sequence_number',
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='date_start', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='AND', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='date_order', kind=None),
                                                                            Constant(value='>=', kind=None),
                                                                            Name(id='date_start', ctx=Load()),
                                                                        ],
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='orders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='pos.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='date_order desc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_interval', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='orders', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='amount_total', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='cumulative_total', ctx=Store()),
                            op=Add(),
                            value=Name(id='total_interval', ctx=Load()),
                        ),
                        Assign(
                            targets=[Name(id='last_order', ctx=Store())],
                            value=Name(id='first_order', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='orders', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='last_order', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='orders', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='total_interval', kind=None),
                                    Constant(value='cumulative_total', kind=None),
                                    Constant(value='last_order_id', kind=None),
                                    Constant(value='last_order_hash', kind=None),
                                    Constant(value='date_closing_stop', kind=None),
                                    Constant(value='date_closing_start', kind=None),
                                    Constant(value='name', kind=None),
                                ],
                                values=[
                                    Name(id='total_interval', ctx=Load()),
                                    Name(id='cumulative_total', ctx=Load()),
                                    Attribute(
                                        value=Name(id='last_order', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='last_order', ctx=Load()),
                                        attr='l10n_fr_secure_sequence_number',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='interval_dates', ctx=Load()),
                                        slice=Constant(value='date_stop', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='date_start', ctx=Load()),
                                    BinOp(
                                        left=BinOp(
                                            left=Subscript(
                                                value=Name(id='interval_dates', ctx=Load()),
                                                slice=Constant(value='name_interval', kind=None),
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=' - ', kind=None),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Subscript(
                                                value=Name(id='interval_dates', ctx=Load()),
                                                slice=Constant(value='date_stop', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=10, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_interval_dates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frequency', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Method used to compute the theoretical date from which account move lines should be fetched\n        @param {string} frequency: a valid value of the selection field on the object (daily, monthly, annually)\n            frequencies are literal (daily means 24 hours and so on)\n        @param {recordset} company: the company for which the closing is done\n        @return {dict} the theoretical date from which account move lines are fetched.\n            date_stop date to which the move lines are fetched, always now()\n            the dates are in their Odoo Database string representation\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='date_stop', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='datetime', ctx=Load()),
                                    attr='utcnow',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='interval_from', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='name_interval', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='frequency', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='daily', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='interval_from', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='date_stop', ctx=Load()),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='name_interval', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Daily Closing', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='frequency', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='monthly', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='month_target', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='date_stop', ctx=Load()),
                                                                    attr='month',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='date_stop', ctx=Load()),
                                                                    attr='month',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value=12, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='year_target', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='month_target', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Constant(value=12, kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='date_stop', ctx=Load()),
                                                                attr='year',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='date_stop', ctx=Load()),
                                                            attr='year',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='interval_from', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='date_stop', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='year',
                                                        value=Name(id='year_target', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='month',
                                                        value=Name(id='month_target', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='name_interval', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Monthly Closing', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='frequency', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='annually', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='year_target', ctx=Store())],
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='date_stop', ctx=Load()),
                                                            attr='year',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='interval_from', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='date_stop', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='year',
                                                                value=Name(id='year_target', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='name_interval', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Annual Closing', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='interval_from', kind=None),
                                    Constant(value='date_stop', kind=None),
                                    Constant(value='name_interval', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='FieldDateTime', ctx=Load()),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='interval_from', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='FieldDateTime', ctx=Load()),
                                            attr='to_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='date_stop', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='name_interval', ctx=Load()),
                                ],
                            ),
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
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Sale Closings are not meant to be written or deleted under any circumstances.', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_unlink_never',
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
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Sale Closings are not meant to be written or deleted under any circumstances.', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='at_uninstall',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_automated_closing',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frequency', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='daily', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='To be executed by the CRON to create an object of the given frequency for each company that needs it\n        @param {string} frequency: a valid value of the selection field on the object (daily, monthly, annually)\n            frequencies are literal (daily means 24 hours and so on)\n        @return {recordset} all the objects created for the given frequency\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res_company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='account_closings', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='account.sale.closing', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='company', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='res_company', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='c', ctx=Load()),
                                                attr='_is_accounting_unalterable',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_sequence_number', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='l10n_fr_closing_sequence_id',
                                                ctx=Load(),
                                            ),
                                            attr='next_by_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compute_amounts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='frequency', ctx=Load()),
                                            Name(id='company', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='frequency', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='frequency', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='sequence_number', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='new_sequence_number', ctx=Load()),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='account_closings', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='account_closings', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='account_closings', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
