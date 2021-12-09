Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='AccountMoveLine',
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
                    value=Constant(value='account.move.line', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_query_tax_details_from_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fallback', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create the tax details sub-query based on the orm domain passed as parameter.\n\n        :param domain:      An orm domain on account.move.line.\n        :param fallback:    Fallback on an approximated mapping if the mapping failed.\n        :return:            A tuple <query, params>.\n        ', kind=None),
                        ),
                        Expr(
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
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='read', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
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
                                    attr='_where_calc',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
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
                                    attr='_apply_ir_rules',
                                    ctx=Load(),
                                ),
                                args=[Name(id='query', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='tables', ctx=Store()),
                                        Name(id='where_clause', ctx=Store()),
                                        Name(id='where_params', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='query', ctx=Load()),
                                    attr='get_sql',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_query_tax_details',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tables', ctx=Load()),
                                    Name(id='where_clause', ctx=Load()),
                                    Name(id='where_params', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='fallback',
                                        value=Name(id='fallback', ctx=Load()),
                                    ),
                                ],
                            ),
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
                    name='_get_query_tax_details',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tables', annotation=None, type_comment=None),
                            arg(arg='where_clause', annotation=None, type_comment=None),
                            arg(arg='where_params', annotation=None, type_comment=None),
                            arg(arg='fallback', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Create the tax details sub-query based on the orm domain passed as parameter.\n\n        :param tables:          The 'tables' query to inject after the FROM.\n        :param where_clause:    The 'where_clause' query computed based on an orm domain.\n        :param where_params:    The params to fill the 'where_clause' query.\n        :param fallback:        Fallback on an approximated mapping if the mapping failed.\n        :return:                A tuple <query, params>.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group_taxes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.tax', kind=None),
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
                                                    Constant(value='amount_type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='group', kind=None),
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
                        Assign(
                            targets=[Name(id='group_taxes_query_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_taxes_params', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group_tax', ctx=Store()),
                            iter=Name(id='group_taxes', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='children_taxes', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='group_tax', ctx=Load()),
                                        attr='children_tax_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='children_taxes', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='children_taxes_in_query', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Constant(value='%s', kind=None),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='dummy', ctx=Store()),
                                                        iter=Name(id='children_taxes', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group_taxes_query_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='WHEN tax.id = %s THEN ARRAY[', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='children_taxes_in_query', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=']', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group_taxes_params', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='group_tax', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='group_taxes_params', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='children_taxes', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='group_taxes_query_list', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='group_taxes_query', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='UNNEST(CASE ', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Constant(value=' ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='group_taxes_query_list', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=' ELSE ARRAY[tax.id] END)', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='group_taxes_query', ctx=Store())],
                                    value=Constant(value='tax.id', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='fallback', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='fallback_query', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='\n                UNION ALL\n\n                SELECT\n                    account_move_line.id AS tax_line_id,\n                    base_line.id AS base_line_id,\n                    base_line.id AS src_line_id,\n                    base_line.balance AS base_amount,\n                    base_line.amount_currency AS base_amount_currency\n                FROM ', kind=None),
                                            FormattedValue(
                                                value=Name(id='tables', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='\n                LEFT JOIN base_tax_line_mapping ON\n                    base_tax_line_mapping.tax_line_id = account_move_line.id\n                JOIN account_move_line_account_tax_rel tax_rel ON\n                    tax_rel.account_tax_id = COALESCE(account_move_line.group_tax_id, account_move_line.tax_line_id)\n                JOIN account_move_line base_line ON\n                    base_line.id = tax_rel.account_move_line_id\n                    AND base_line.tax_repartition_line_id IS NULL\n                    AND base_line.move_id = account_move_line.move_id\n                    AND base_line.currency_id = account_move_line.currency_id\n                WHERE base_tax_line_mapping.tax_line_id IS NULL\n                AND ', kind=None),
                                            FormattedValue(
                                                value=Name(id='where_clause', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='\n            ', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fallback_params', ctx=Store())],
                                    value=Name(id='where_params', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='fallback_query', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='fallback_params', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    JoinedStr(
                                        values=[
                                            Constant(value="\n            /*\n            As example to explain the different parts of the query, we'll consider a move with the following lines:\n            Name            Tax_line_id         Tax_ids                 Debit       Credit      Base lines\n            ---------------------------------------------------------------------------------------------------\n            base_line_1                         10_affect_base, 20      1000\n            base_line_2                         10_affect_base, 5       2000\n            base_line_3                         10_affect_base, 5       3000\n            tax_line_1      10_affect_base      20                                  100         base_line_1\n            tax_line_2      20                                                      220         base_line_1\n            tax_line_3      10_affect_base      5                                   500         base_line_2/3\n            tax_line_4      5                                                       275         base_line_2/3\n            */\n\n            WITH affecting_base_tax_ids AS (\n\n                /*\n                This CTE builds a reference table based on the tax_ids field, with the following changes:\n                  - flatten the group of taxes\n                  - exclude the taxes having 'is_base_affected' set to False.\n                Those allow to match only base_line_1 when finding the base lines of tax_line_1, as we need to find\n                base lines having a 'affecting_base_tax_ids' ending with [10_affect_base, 20], not only containing\n                '10_affect_base'. Otherwise, base_line_2/3 would also be matched.\n                In our example, as all the taxes are set to be affected by previous ones affecting the base, the\n                result is similar to the table 'account_move_line_account_tax_rel':\n                Id                 Tax_ids\n                -------------------------------------------\n                base_line_1        [10_affect_base, 20]\n                base_line_2        [10_affect_base, 5]\n                base_line_3        [10_affect_base, 5]\n                */\n\n                SELECT\n                    sub.line_id AS id,\n                    ARRAY_AGG(sub.tax_id ORDER BY sub.sequence, sub.tax_id) AS tax_ids\n                FROM (\n                    SELECT\n                        tax_rel.account_move_line_id AS line_id,\n                        ", kind=None),
                                            FormattedValue(
                                                value=Name(id='group_taxes_query', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=' AS tax_id,\n                        tax.sequence\n                    FROM ', kind=None),
                                            FormattedValue(
                                                value=Name(id='tables', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='\n                    JOIN account_move_line_account_tax_rel tax_rel ON account_move_line.id = tax_rel.account_move_line_id\n                    JOIN account_tax tax ON tax.id = tax_rel.account_tax_id\n                    WHERE tax.is_base_affected\n                    AND ', kind=None),
                                            FormattedValue(
                                                value=Name(id='where_clause', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='\n                ) AS sub\n                GROUP BY sub.line_id\n            ),\n\n            base_tax_line_mapping AS (\n\n                /*\n                Create the mapping of each tax lines with their corresponding base lines.\n\n                In the example, it will give the following values:\n                    base_line_id     tax_line_id    base_amount\n                    -------------------------------------------\n                    base_line_1      tax_line_1         1000\n                    base_line_1      tax_line_2         1000\n                    base_line_2      tax_line_3         2000\n                    base_line_2      tax_line_4         2000\n                    base_line_3      tax_line_3         3000\n                    base_line_3      tax_line_4         3000\n                */\n\n                SELECT\n                    account_move_line.id AS tax_line_id,\n                    base_line.id AS base_line_id,\n                    base_line.balance AS base_amount,\n                    base_line.amount_currency AS base_amount_currency\n\n                FROM ', kind=None),
                                            FormattedValue(
                                                value=Name(id='tables', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value="\n                JOIN account_tax_repartition_line tax_rep ON\n                    tax_rep.id = account_move_line.tax_repartition_line_id\n                JOIN account_tax tax ON\n                    tax.id = account_move_line.tax_line_id\n                JOIN res_currency curr ON\n                    curr.id = account_move_line.currency_id\n                JOIN res_currency comp_curr ON\n                    comp_curr.id = account_move_line.company_currency_id\n                JOIN account_move_line_account_tax_rel tax_rel ON\n                    tax_rel.account_tax_id = COALESCE(account_move_line.group_tax_id, account_move_line.tax_line_id)\n                JOIN account_move_line base_line ON\n                    base_line.id = tax_rel.account_move_line_id\n                    AND base_line.tax_repartition_line_id IS NULL\n                    AND base_line.move_id = account_move_line.move_id\n                    AND COALESCE(base_line.partner_id, 0) = COALESCE(account_move_line.partner_id, 0)\n                    AND base_line.currency_id = account_move_line.currency_id\n                    AND (\n                        COALESCE(tax_rep.account_id, base_line.account_id) = account_move_line.account_id\n                        OR (tax.tax_exigibility = 'on_payment' AND tax.cash_basis_transition_account_id IS NOT NULL)\n                    )\n                    AND (\n                        NOT tax.analytic\n                        OR (base_line.analytic_account_id IS NULL AND account_move_line.analytic_account_id IS NULL)\n                        OR base_line.analytic_account_id = account_move_line.analytic_account_id\n                    )\n                LEFT JOIN affecting_base_tax_ids tax_line_tax_ids ON tax_line_tax_ids.id = account_move_line.id\n                JOIN affecting_base_tax_ids base_line_tax_ids ON base_line_tax_ids.id = base_line.id\n                WHERE account_move_line.tax_repartition_line_id IS NOT NULL\n                    AND ", kind=None),
                                            FormattedValue(
                                                value=Name(id='where_clause', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value="\n                    AND (\n                        -- keeping only the rows from affecting_base_tax_lines that end with the same taxes applied (see comment in affecting_base_tax_ids)\n                        NOT tax.include_base_amount\n                        OR base_line_tax_ids.tax_ids[ARRAY_LENGTH(base_line_tax_ids.tax_ids, 1) - COALESCE(ARRAY_LENGTH(tax_line_tax_ids.tax_ids, 1), 0):ARRAY_LENGTH(base_line_tax_ids.tax_ids, 1)]\n                            = ARRAY[account_move_line.tax_line_id] || COALESCE(tax_line_tax_ids.tax_ids, ARRAY[]::INTEGER[])\n                    )\n            ),\n\n\n            tax_amount_affecting_base_to_dispatch AS (\n\n                /*\n                Computes the total amount to dispatch in case of tax lines affecting the base of subsequent taxes.\n                Such tax lines are an additional base amount for others lines, that will be truly dispatch in next\n                CTE.\n\n                In the example:\n                    - tax_line_1 is an additional base of 100.0 from base_line_1 for tax_line_2.\n                    - tax_line_3 is an additional base of 2/5 * 500.0 = 200.0 from base_line_2 for tax_line_4.\n                    - tax_line_3 is an additional base of 3/5 * 500.0 = 300.0 from base_line_3 for tax_line_4.\n\n                    src_line_id    base_line_id     tax_line_id    total_base_amount\n                    -------------------------------------------------------------\n                    tax_line_1     base_line_1      tax_line_2         1000\n                    tax_line_3     base_line_2      tax_line_4         5000\n                    tax_line_3     base_line_3      tax_line_4         5000\n                */\n\n                SELECT\n                    tax_line.id AS tax_line_id,\n                    base_line.id AS base_line_id,\n                    account_move_line.id AS src_line_id,\n\n                    tax_line.company_id,\n                    comp_curr.id AS company_currency_id,\n                    comp_curr.decimal_places AS comp_curr_prec,\n                    curr.id AS currency_id,\n                    curr.decimal_places AS curr_prec,\n\n                    tax_line.tax_line_id AS tax_id,\n\n                    base_line.balance AS base_amount,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.balance < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE base_line.balance\n                        END\n                    ) OVER (PARTITION BY tax_line.id, account_move_line.id ORDER BY tax_line.tax_line_id, base_line.id) AS cumulated_base_amount,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.balance < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE base_line.balance\n                        END\n                    ) OVER (PARTITION BY tax_line.id, account_move_line.id) AS total_base_amount,\n                    account_move_line.balance AS total_tax_amount,\n\n                    base_line.amount_currency AS base_amount_currency,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.amount_currency < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE base_line.amount_currency\n                        END\n                    ) OVER (PARTITION BY tax_line.id, account_move_line.id ORDER BY tax_line.tax_line_id, base_line.id) AS cumulated_base_amount_currency,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.amount_currency < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE base_line.amount_currency\n                        END\n                    ) OVER (PARTITION BY tax_line.id, account_move_line.id) AS total_base_amount_currency,\n                    account_move_line.amount_currency AS total_tax_amount_currency\n\n                FROM ", kind=None),
                                            FormattedValue(
                                                value=Name(id='tables', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='\n                JOIN account_tax tax_include_base_amount ON\n                    tax_include_base_amount.include_base_amount\n                    AND tax_include_base_amount.id = account_move_line.tax_line_id\n                JOIN base_tax_line_mapping base_tax_line_mapping ON\n                    base_tax_line_mapping.tax_line_id = account_move_line.id\n                JOIN account_move_line_account_tax_rel tax_rel ON\n                    tax_rel.account_move_line_id = base_tax_line_mapping.tax_line_id\n                JOIN account_tax tax ON\n                    tax.id = tax_rel.account_tax_id\n                JOIN base_tax_line_mapping tax_line_matching ON\n                    tax_line_matching.base_line_id = base_tax_line_mapping.base_line_id\n                JOIN account_move_line tax_line ON\n                    tax_line.id = tax_line_matching.tax_line_id\n                    AND tax_line.tax_line_id = tax_rel.account_tax_id\n                JOIN res_currency curr ON\n                    curr.id = tax_line.currency_id\n                JOIN res_currency comp_curr ON\n                    comp_curr.id = tax_line.company_currency_id\n                JOIN account_move_line base_line ON\n                    base_line.id = base_tax_line_mapping.base_line_id\n                WHERE ', kind=None),
                                            FormattedValue(
                                                value=Name(id='where_clause', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value="\n            ),\n\n\n            base_tax_matching_base_amounts AS (\n\n                /*\n                Build here the full mapping tax lines <=> base lines containing the final base amounts.\n                This is done in a 3-parts union.\n\n                Note: src_line_id is used only to build a unique ID.\n                */\n\n                /*\n                PART 1: raw mapping computed in base_tax_line_mapping.\n                */\n\n                SELECT\n                    tax_line_id,\n                    base_line_id,\n                    base_line_id AS src_line_id,\n                    base_amount,\n                    base_amount_currency\n                FROM base_tax_line_mapping\n\n                UNION ALL\n\n                /*\n                PART 2: Dispatch the tax amount of tax lines affecting the base of subsequent ones, using\n                tax_amount_affecting_base_to_dispatch.\n\n                This will effectively add the following rows:\n                base_line_id    tax_line_id     src_line_id     base_amount\n                -------------------------------------------------------------\n                base_line_1     tax_line_2      tax_line_1      100\n                base_line_2     tax_line_4      tax_line_3      200\n                base_line_3     tax_line_4      tax_line_3      300\n                */\n\n                SELECT\n                    sub.tax_line_id,\n                    sub.base_line_id,\n                    sub.src_line_id,\n\n                    ROUND(\n                        COALESCE(sub.total_tax_amount * ABS(sub.cumulated_base_amount) / ABS(NULLIF(sub.total_base_amount, 0.0)), 0.0),\n                        sub.comp_curr_prec\n                    )\n                    - LAG(ROUND(\n                        COALESCE(sub.total_tax_amount * ABS(sub.cumulated_base_amount) / ABS(NULLIF(sub.total_base_amount, 0.0)), 0.0),\n                        sub.comp_curr_prec\n                    ), 1, 0.0)\n                    OVER (\n                        PARTITION BY sub.tax_line_id, sub.src_line_id ORDER BY sub.tax_id, sub.base_line_id\n                    ) AS base_amount,\n\n                    ROUND(\n                        COALESCE(sub.total_tax_amount_currency * ABS(sub.cumulated_base_amount_currency) / ABS(NULLIF(sub.total_base_amount_currency, 0.0)), 0.0),\n                        sub.curr_prec\n                    )\n                    - LAG(ROUND(\n                        COALESCE(sub.total_tax_amount_currency * ABS(sub.cumulated_base_amount_currency) / ABS(NULLIF(sub.total_base_amount_currency, 0.0)), 0.0),\n                        sub.curr_prec\n                    ), 1, 0.0)\n                    OVER (\n                        PARTITION BY sub.tax_line_id, sub.src_line_id ORDER BY sub.tax_id, sub.base_line_id\n                    ) AS base_amount_currency\n                FROM tax_amount_affecting_base_to_dispatch sub\n                JOIN account_move_line tax_line ON\n                    tax_line.id = sub.tax_line_id\n\n                /*\n                PART 3: In case of the matching failed because the configuration changed or some journal entries\n                have been imported, construct a simple mapping as a fallback. This mapping is super naive and only\n                build based on the 'tax_ids' and 'tax_line_id' fields, nothing else. Hence, the mapping will not be\n                exact but will give an acceptable approximation.\n\n                Skipped if the 'fallback' method parameter is False.\n                */\n                ", kind=None),
                                            FormattedValue(
                                                value=Name(id='fallback_query', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value="\n            ),\n\n\n            base_tax_matching_all_amounts AS (\n\n                /*\n                Complete base_tax_matching_base_amounts with the tax amounts (prorata):\n                base_line_id    tax_line_id     src_line_id     base_amount     tax_amount\n                --------------------------------------------------------------------------\n                base_line_1     tax_line_1      base_line_1     1000            100\n                base_line_1     tax_line_2      base_line_1     1000            (1000 / 1100) * 220 = 200\n                base_line_1     tax_line_2      tax_line_1      100             (100 / 1100) * 220 = 20\n                base_line_2     tax_line_3      base_line_2     2000            (2000 / 5000) * 500 = 200\n                base_line_2     tax_line_4      base_line_2     2000            (2000 / 5500) * 275 = 100\n                base_line_2     tax_line_4      tax_line_3      200             (200 / 5500) * 275 = 10\n                base_line_3     tax_line_3      base_line_3     3000            (3000 / 5000) * 500 = 300\n                base_line_3     tax_line_4      base_line_3     3000            (3000 / 5500) * 275 = 150\n                base_line_3     tax_line_4      tax_line_3      300             (300 / 5500) * 275 = 15\n                */\n\n                SELECT\n                    sub.tax_line_id,\n                    sub.base_line_id,\n                    sub.src_line_id,\n\n                    tax_line.tax_line_id AS tax_id,\n                    tax_line.group_tax_id,\n\n                    tax_line.company_id,\n                    comp_curr.id AS company_currency_id,\n                    comp_curr.decimal_places AS comp_curr_prec,\n                    curr.id AS currency_id,\n                    curr.decimal_places AS curr_prec,\n                    (\n                        tax.tax_exigibility != 'on_payment'\n                        OR tax_move.tax_cash_basis_rec_id IS NOT NULL\n                        OR tax_move.always_tax_exigible\n                    ) AS tax_exigible,\n                    base_line.account_id AS base_account_id,\n\n                    sub.base_amount,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.balance < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE sub.base_amount\n                        END\n                    ) OVER (PARTITION BY tax_line.id ORDER BY tax_line.tax_line_id, sub.base_line_id, sub.src_line_id) AS cumulated_base_amount,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.balance < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE sub.base_amount\n                        END\n                    ) OVER (PARTITION BY tax_line.id) AS total_base_amount,\n                    tax_line.balance AS total_tax_amount,\n\n                    sub.base_amount_currency,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.amount_currency < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE sub.base_amount_currency\n                        END\n                    ) OVER (PARTITION BY tax_line.id ORDER BY tax_line.tax_line_id, sub.base_line_id, sub.src_line_id) AS cumulated_base_amount_currency,\n                    SUM(\n                        CASE WHEN tax.amount_type = 'fixed'\n                        THEN CASE WHEN base_line.amount_currency < 0 THEN -1 ELSE 1 END * ABS(COALESCE(base_line.quantity, 1.0))\n                        ELSE sub.base_amount_currency\n                        END\n                    ) OVER (PARTITION BY tax_line.id) AS total_base_amount_currency,\n                    tax_line.amount_currency AS total_tax_amount_currency\n\n                FROM base_tax_matching_base_amounts sub\n                JOIN account_move_line tax_line ON\n                    tax_line.id = sub.tax_line_id\n                JOIN account_move tax_move ON\n                    tax_move.id = tax_line.move_id\n                JOIN account_move_line base_line ON\n                    base_line.id = sub.base_line_id\n                JOIN account_tax tax ON\n                    tax.id = tax_line.tax_line_id\n                JOIN res_currency curr ON\n                    curr.id = tax_line.currency_id\n                JOIN res_currency comp_curr ON\n                    comp_curr.id = tax_line.company_currency_id\n\n            )\n\n\n           /* Final select that makes sure to deal with rounding errors, using LAG to dispatch the last cents. */\n\n            SELECT\n                sub.tax_line_id || '-' || sub.base_line_id || '-' || sub.src_line_id AS id,\n\n                sub.base_line_id,\n                sub.tax_line_id,\n                sub.src_line_id,\n\n                sub.tax_id,\n                sub.group_tax_id,\n                sub.tax_exigible,\n                sub.base_account_id,\n\n                sub.base_amount,\n                ROUND(\n                    COALESCE(sub.total_tax_amount * ABS(sub.cumulated_base_amount) / ABS(NULLIF(sub.total_base_amount, 0.0)), 0.0),\n                    sub.comp_curr_prec\n                )\n                - LAG(ROUND(\n                    COALESCE(sub.total_tax_amount * ABS(sub.cumulated_base_amount) / ABS(NULLIF(sub.total_base_amount, 0.0)), 0.0),\n                    sub.comp_curr_prec\n                ), 1, 0.0)\n                OVER (\n                    PARTITION BY sub.tax_line_id ORDER BY sub.tax_id, sub.base_line_id\n                ) AS tax_amount,\n\n                sub.base_amount_currency,\n                ROUND(\n                    COALESCE(sub.total_tax_amount_currency * ABS(sub.cumulated_base_amount_currency) / ABS(NULLIF(sub.total_base_amount_currency, 0.0)), 0.0),\n                    sub.curr_prec\n                )\n                - LAG(ROUND(\n                    COALESCE(sub.total_tax_amount_currency * ABS(sub.cumulated_base_amount_currency) / ABS(NULLIF(sub.total_base_amount_currency, 0.0)), 0.0),\n                    sub.curr_prec\n                ), 1, 0.0)\n                OVER (\n                    PARTITION BY sub.tax_line_id ORDER BY sub.tax_id, sub.base_line_id\n                ) AS tax_amount_currency\n            FROM base_tax_matching_all_amounts sub\n        ", kind=None),
                                        ],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Name(id='group_taxes_params', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='where_params', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='where_params', ctx=Load()),
                                            ),
                                            op=Add(),
                                            right=Name(id='where_params', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='fallback_params', ctx=Load()),
                                    ),
                                ],
                                ctx=Load(),
                            ),
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
