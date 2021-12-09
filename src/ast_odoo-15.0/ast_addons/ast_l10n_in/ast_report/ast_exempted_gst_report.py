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
        ClassDef(
            name='L10nInExemptedReport',
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
                    value=Constant(value='l10n_in.exempted.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Exempted Gst Supplied Statistics', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='account_move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.move', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Account Move', kind=None),
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='out_supply_type', ctx=Store())],
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
                                value=Constant(value='Outward Supply Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='in_supply_type', ctx=Store())],
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
                                value=Constant(value='Inward Supply Type', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nil_rated_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Nil rated supplies', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='exempted_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Exempted', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='non_gst_supplies', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Non GST Supplies', kind=None)],
                        keywords=[],
                    ),
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
                        args=[Constant(value='Date', kind=None)],
                        keywords=[],
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='journal_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='account.journal', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Journal', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_select',
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
                            targets=[Name(id='select_str', ctx=Store())],
                            value=Constant(value="SELECT aml.id AS id,\n            aml.partner_id AS partner_id,\n            am.date,\n            aml.balance * (CASE WHEN aj.type = 'sale' THEN -1 ELSE 1 END) AS price_total,\n            am.journal_id,\n            aj.company_id,\n            aml.move_id as account_move_id,\n\n            (CASE WHEN p.state_id = cp.state_id\n                THEN (CASE WHEN p.vat IS NOT NULL\n                    THEN 'Intra-State supplies to registered persons'\n                    ELSE 'Intra-State supplies to unregistered persons'\n                    END)\n                WHEN p.state_id != cp.state_id\n                THEN (CASE WHEN p.vat IS NOT NULL\n                    THEN 'Inter-State supplies to registered persons'\n                    ELSE 'Inter-State supplies to unregistered persons'\n                    END)\n            END) AS out_supply_type,\n            (CASE WHEN p.state_id = cp.state_id\n                THEN 'Intra-State supplies'\n                WHEN p.state_id != cp.state_id\n                THEN 'Inter-State supplies'\n            END) AS in_supply_type,\n\n            (CASE WHEN (\n                SELECT MAX(account_tax_id) FROM account_move_line_account_tax_rel\n                    JOIN account_tax at ON at.id = account_tax_id\n                    WHERE account_move_line_id = aml.id AND at.tax_group_id IN\n                     ((SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name='nil_rated_group'))\n            ) IS NOT NULL\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' THEN -1 ELSE 1 END)\n                ELSE 0\n            END) AS nil_rated_amount,\n\n            (CASE WHEN (\n                SELECT MAX(account_tax_id) FROM account_move_line_account_tax_rel\n                    JOIN account_tax at ON at.id = account_tax_id\n                    WHERE account_move_line_id = aml.id AND at.tax_group_id IN\n                     ((SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name='exempt_group'))\n            ) IS NOT NULL\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' THEN -1 ELSE 1 END)\n                ELSE 0\n            END) AS exempted_amount,\n\n            (CASE WHEN (\n                SELECT MAX(account_tax_id) FROM account_move_line_account_tax_rel\n                    WHERE account_move_line_id = aml.id\n                ) IS NULL\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' THEN -1 ELSE 1 END)\n                ELSE 0\n            END) AS non_gst_supplies\n        ", kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='select_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_from',
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
                            targets=[Name(id='from_str', ctx=Store())],
                            value=Constant(value="FROM account_move_line aml\n            JOIN account_move am ON am.id = aml.move_id\n            JOIN account_account aa ON aa.id = aml.account_id\n            JOIN account_journal aj ON aj.id = am.journal_id\n            JOIN res_company c ON c.id = aj.company_id\n            LEFT JOIN res_partner cp ON cp.id = COALESCE(aj.l10n_in_gstin_partner_id, c.partner_id)\n            LEFT JOIN res_partner p ON p.id = am.partner_id\n            LEFT JOIN res_country pc ON pc.id = p.country_id\n            WHERE aa.internal_type = 'other' and aml.tax_line_id IS NULL\n        ", kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='from_str', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='CREATE OR REPLACE VIEW %s AS (%s %s)', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_table',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_select',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_from',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
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
