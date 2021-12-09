Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='migrate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='cr', annotation=None, type_comment=None),
                    arg(arg='version', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='get_taxes_from_templates',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='templates', annotation=None, type_comment=None)],
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
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value="\n            SELECT array_agg(tax.id)\n            FROM account_tax tax\n            JOIN ir_model_data data\n                ON data.model = 'account.tax'\n                AND data.res_id = tax.id\n                AND data.module = 'l10n_es'\n                AND data.name ~ '^[0-9]*_(", kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Constant(value='|', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='templates', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=")\\Z'\n        ", kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='fetchone',
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
                Assign(
                    targets=[Name(id='env', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='Environment',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='cr', ctx=Load()),
                            Name(id='SUPERUSER_ID', ctx=Load()),
                            Dict(keys=[], values=[]),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='templates_mapping', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='mod_303_120', kind=None),
                            Constant(value='mod_303_122', kind=None),
                        ],
                        values=[
                            List(
                                elts=[
                                    Constant(value='account_tax_template_s_iva_ns', kind=None),
                                    Constant(value='account_tax_template_s_iva_ns_b', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            List(
                                elts=[
                                    Constant(value='account_tax_template_s_iva_e', kind=None),
                                    Constant(value='account_tax_template_s_iva0_isp', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='taxes_mapping', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='tag_name', ctx=Store()),
                            Name(id='template_names', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='templates_mapping', ctx=Load()),
                            attr='items',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='taxes_from_templates', ctx=Store())],
                            value=Call(
                                func=Name(id='get_taxes_from_templates', ctx=Load()),
                                args=[Name(id='template_names', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='taxes_from_templates', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='taxes_mapping', ctx=Load()),
                                            slice=Name(id='tag_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='taxes_from_templates', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_tag', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='env', ctx=Load()),
                            attr='ref',
                            ctx=Load(),
                        ),
                        args=[Constant(value='l10n_es.mod_303_61', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='tag_name', ctx=Store()),
                            Name(id='tax_ids', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Call(
                        func=Attribute(
                            value=Name(id='taxes_mapping', ctx=Load()),
                            attr='items',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_tag', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='env', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='l10n_es.', kind=None),
                                            FormattedValue(
                                                value=Name(id='tag_name', ctx=Load()),
                                                conversion=-1,
                                                format_spec=None,
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
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n            UPDATE account_account_tag_account_tax_repartition_line_rel tax_rep_tag\n            SET account_account_tag_id = %s\n            FROM account_account_tag new_tag, account_tax_repartition_line repln\n            WHERE tax_rep_tag.account_account_tag_id = %s\n            AND repln.id = tax_rep_tag.account_tax_repartition_line_id\n            AND COALESCE(repln.invoice_tax_id, repln.refund_tax_id) IN %s\n        ', kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='new_tag', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='old_tag', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='tax_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="\n            UPDATE account_account_tag_account_move_line_rel aml_tag\n            SET account_account_tag_id = %s\n            FROM account_move_line aml, account_move_line_account_tax_rel aml_tax\n            WHERE aml_tag.account_move_line_id = aml.id\n            AND aml_tax.account_move_line_id = aml.id\n            AND aml.date >= '2021-07-01'\n            AND aml_tax.account_tax_id IN %s\n            AND aml_tag.account_account_tag_id = %s\n        ", kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='new_tag', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[Name(id='tax_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='old_tag', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n            UPDATE account_move_line aml\n            SET tax_audit = REPLACE(tax_audit, %s, %s)\n            FROM account_account_tag_account_move_line_rel aml_tag\n            WHERE aml_tag.account_move_line_id = aml.id\n            AND aml_tag.account_account_tag_id = %s\n        ', kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='old_tag', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='new_tag', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=':', kind=None),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='new_tag', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
