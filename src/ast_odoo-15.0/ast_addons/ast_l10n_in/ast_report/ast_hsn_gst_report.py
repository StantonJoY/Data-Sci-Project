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
            name='L10nInProductHsnReport',
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
                    value=Constant(value='l10n_in.product.hsn.report', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Product HSN Statistics', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_auto', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='date desc', kind=None),
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='uom_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='uom.uom', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='UOM', kind=None),
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
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product Qty', kind=None),
                            ),
                        ],
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price_total', ctx=Store())],
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
                                value=Constant(value='Taxable Value', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='total', ctx=Store())],
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
                                value=Constant(value='Total Value', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='igst_amount', ctx=Store())],
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
                                value=Constant(value='Integrated Tax Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cgst_amount', ctx=Store())],
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
                                value=Constant(value='Central Tax Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sgst_amount', ctx=Store())],
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
                                value=Constant(value='State/UT Tax Amount', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cess_amount', ctx=Store())],
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
                                value=Constant(value='Cess Amount', kind=None),
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
                Assign(
                    targets=[Name(id='hsn_code', ctx=Store())],
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
                                value=Constant(value='HSN', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='hsn_description', ctx=Store())],
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
                                value=Constant(value='HSN description', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_in_uom_code', ctx=Store())],
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
                                value=Constant(value='UQC', kind=None),
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
                            value=Constant(value="SELECT aml.id AS id,\n            aml.move_id AS account_move_id,\n            aml.partner_id AS partner_id,\n            aml.product_id,\n            aml.product_uom_id AS uom_id,\n            am.date,\n            am.journal_id,\n            aj.company_id,\n            CASE WHEN pt.l10n_in_hsn_code IS NULL THEN '' ELSE pt.l10n_in_hsn_code END AS hsn_code,\n            CASE WHEN pt.l10n_in_hsn_description IS NULL THEN '' ELSE pt.l10n_in_hsn_description END AS hsn_description,\n            CASE WHEN uom.l10n_in_code IS NULL THEN '' ELSE uom.l10n_in_code END AS l10n_in_uom_code,\n            CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_sgst', 'tax_report_line_sgst_rc')) OR at.l10n_in_reverse_charge = True\n                THEN 0\n                ELSE aml.quantity\n                END * (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS quantity,\n            CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_igst', 'tax_report_line_igst_rc'))\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' and am.move_type != 'out_refund' THEN -1 ELSE 1 END)\n                ELSE 0\n                END * (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS igst_amount,\n            CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_cgst', 'tax_report_line_cgst_rc'))\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' and am.move_type != 'out_refund' THEN -1 ELSE 1 END)\n                ELSE 0\n                END * (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS cgst_amount,\n            CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_sgst', 'tax_report_line_sgst_rc'))\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' and am.move_type != 'out_refund' THEN -1 ELSE 1 END)\n                ELSE 0\n                END * (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS  sgst_amount,\n            CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_cess', 'tax_report_line_cess_rc'))\n                THEN aml.balance * (CASE WHEN aj.type = 'sale' and am.move_type != 'out_refund' THEN -1 ELSE 1 END)\n                ELSE 0\n                END * (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS cess_amount,\n            CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_sgst', 'tax_report_line_sgst_rc'))\n                THEN 0\n                ELSE (CASE WHEN aml.tax_line_id IS NOT NULL THEN aml.tax_base_amount ELSE aml.balance * (CASE WHEN aj.type = 'sale' THEN -1 ELSE 1 END) END)\n                END * (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS price_total,\n            ((CASE WHEN tag_rep_ln.account_tax_report_line_id IN\n                (SELECT res_id FROM ir_model_data WHERE module='l10n_in' AND name in ('tax_report_line_sgst', 'tax_report_line_sgst_rc'))\n                THEN 0\n                ELSE (CASE WHEN aml.tax_line_id IS NOT NULL THEN aml.tax_base_amount ELSE 1 END)\n                    END) + (aml.balance * (CASE WHEN aj.type = 'sale' and am.move_type != 'out_refund' THEN -1 ELSE 1 END))\n                 )* (CASE WHEN am.move_type in ('in_refund','out_refund') THEN -1 ELSE 1 END)\n                AS total\n        ", kind=None),
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
                            value=Constant(value="FROM account_move_line aml\n            JOIN account_move am ON am.id = aml.move_id\n            JOIN account_account aa ON aa.id = aml.account_id\n            JOIN account_journal aj ON aj.id = am.journal_id\n            JOIN product_product pp ON pp.id = aml.product_id\n            JOIN product_template pt ON pt.id = pp.product_tmpl_id\n            LEFT JOIN account_tax at ON at.id = aml.tax_line_id\n            LEFT JOIN account_account_tag_account_move_line_rel aat_aml_rel ON aat_aml_rel.account_move_line_id = aml.id\n            LEFT JOIN account_account_tag aat ON aat.id = aat_aml_rel.account_account_tag_id\n            LEFT JOIN account_tax_report_line_tags_rel tag_rep_ln ON aat.id = tag_rep_ln.account_account_tag_id\n            LEFT JOIN account_move_line_account_tax_rel mt ON mt.account_move_line_id = aml.id\n            LEFT JOIN uom_uom uom ON uom.id = aml.product_uom_id\n            WHERE aa.internal_type = 'other' AND (aml.tax_line_id IS NOT NULL OR mt.account_tax_id IS NULL)\n              AND am.state = 'posted'\n        ", kind=None),
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
